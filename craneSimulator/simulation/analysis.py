"""
Provides all functions to analyze the behavior of the crane under load
"""
import numpy as np


class Conditions:
    """Conditions of parts of the crane"""
    Ur = []
    dof_condition = np.ones_like(0)
    p = np.zeros_like(0)


class Comps():
    nodes = []


class Dims():
    TOWER_END = 0
    JIB_END = 0
    COUNTERJIB_END = 0


kN = 1e3


def generate_conditions(nodes):
    """Generates conditions for the crane"""
    Comps.nodes = nodes

    # Support Displacement
    Conditions.Ur = [0, 0, 0,
                     0, 0, 0,
                     0, 0, 0,
                     0, 0, 0]  # nodes 0-4 in xyz

    # Condition of DOF (0 = fixed, 1 = free)
    dof_condition = np.ones_like(nodes).astype(int)
    # Anchoring the crane to the ground
    dof_condition[0, :] = 0
    dof_condition[1, :] = 0
    dof_condition[2, :] = 0
    dof_condition[3, :] = 0
    Conditions.dof_condition = dof_condition


def apply_forces(window, nodes, end_tower, end_jib):
    """Applies user-entered forces"""
    Comps.nodes = nodes
    Dims.TOWER_END = end_tower
    Dims.JIB_END = end_jib
    Dims.COUNTERJIB_END = len(nodes)

    # Applied forces
    p = np.zeros_like(nodes)
    # TODO change indices
    # Force on jib
    p[Dims.JIB_END - 2, 2] = window.jib_left_spinBox.value() * kN
    p[Dims.JIB_END - 1, 2] = window.jib_right_spinBox.value() * kN
    # Force on counter jib
    p[Dims.COUNTERJIB_END - 2, 2] = window.counterjib_left_spinBox.value() * kN
    p[Dims.COUNTERJIB_END - 1, 2] = window.counterjib_left_spinBox.value() * kN
    Conditions.p = p


def apply_gravity(nodes, beams, A, density, grav_const):
    """Applies gravity to each node"""
    for i in range(len(nodes)):
        fitting_beams_lc = np.where(beams[:, 0] == i)[0]
        fitting_beams_rc = np.where(beams[:, 1] == i)[0]
        fitting_beams = np.concatenate((fitting_beams_lc, fitting_beams_rc), axis=None)
        length = 0
        for j in range(len(fitting_beams)):
            start_float = np.array(beams[fitting_beams[j], 0]).astype(float)
            end_float = np.array(beams[fitting_beams[j], 1]).astype(float)
            length += np.linalg.norm(end_float - start_float)
        Conditions.p[i, 2] += - ((length / 2) / 1000 * A * density * grav_const) * kN


def apply_wind(direc, force, cj_sup_type, cj_end):
    """Applies wind in specified direction with specified force to the crane"""
    print(f'{direc} - {force}')
    if direc == 'front':
        apply_wind_front(force, cj_sup_type, cj_end)
    elif direc == 'right':
        apply_wind_right(force)
    elif direc == 'back':
        apply_wind_back(force, cj_sup_type, cj_end)
    elif direc == 'left':
        apply_wind_left(force, cj_sup_type)


def apply_wind_front(force, cj_sup_type, cj_end):
    # force in north dir
    # y dir
    # tower: all odd nodes
    for t_n in range(int(Dims.TOWER_END / 2)):
        Conditions.p[(1 + 2 * t_n), 1] = force * kN
    # jib: 0+3n (top), 2+3n (bot)
    for j_n in range(int(Dims.TOWER_END), int(Dims.JIB_END / 3)):
        Conditions.p[(0 + 3 * j_n), 1] = force * kN
        Conditions.p[(2 + 3 * j_n), 1] = force * kN
    # counterjib: top center for 1-2 towers, rest just for truss
    for cj_n in range(int(Dims.JIB_END), int(cj_end / 2)):
        Conditions.p[Dims.JIB_END + (1 + 2 * j_n), 1] = force * kN
    if cj_sup_type == 'Truss':
        for cj_n in range(cj_end, int(Dims.COUNTERJIB_END)):
            Conditions.p[cj_n, 1] = force * kN
    elif cj_sup_type == 'Single tower':
        Conditions.p[int(Dims.COUNTERJIB_END), 1] = force * kN
    elif cj_sup_type == 'Twin towers':
        Conditions.p[int(Dims.COUNTERJIB_END) - 1, 1] = force * kN


def apply_wind_right(force):
    # force in east dir
    # -x
    # tower: 2+4n, 3+4n
    for t_n in range(int(Dims.TOWER_END / 4) - 1):
        Conditions.p[(2 + 4 * t_n), 0] = - force * kN
        Conditions.p[(3 + 4 * t_n), 0] = - force * kN
    # jib: last 3
    for j_n in range(int(Dims.JIB_END) - 3, int(Dims.JIB_END)):
        Conditions.p[j_n, 0] = - force * kN
    # counterjib: none


def apply_wind_back(force, cj_sup_type, cj_end):
    # force in south dir
    # -y dir
    # tower: all even nodes
    for t_n in range(Dims.TOWER_END):
        Conditions.p[2 * t_n, 1] = - force * kN
    print('Completed tower')
    # jib: 0+3n (top), 1+3n (bot)
    for j_n in range(Dims.TOWER_END, int(Dims.JIB_END / 3)):
        Conditions.p[(0 + 3 * j_n), 1] = - force * kN
        Conditions.p[(1 + 3 * j_n), 1] = - force * kN
    print('Completed jib')
    # counterjib: top center for 1-2 towers, rest just for truss
    for cj_n in range(int(Dims.JIB_END), int(cj_end / 2)):
        Conditions.p[Dims.JIB_END + (0 + 2 * j_n), 1] = - force * kN
    if cj_sup_type == 'Truss':
        for cj_n in range(cj_end, int(Dims.COUNTERJIB_END)):
            Conditions.p[cj_n, 1] = - force * kN
    elif cj_sup_type == 'Single tower' or cj_sup_type == 'Twin towers':
        Conditions.p[int(Dims.COUNTERJIB_END), 1] = - force * kN


def apply_wind_left(force, cj_sup_type):
    # force in west dir
    # +x dir
    # tower: 2+4n, 3+4n
    for t_n in range(int(Dims.TOWER_END / 4) - 1):
        Conditions.p[(0 + 4 * t_n), 0] = force * kN
        Conditions.p[(1 + 4 * t_n), 0] = force * kN
    # jib: none
    # counterjib: truss last 3; last 2 plus tower
    if cj_sup_type == 'Twin towers':
        start_cj_n = int(Dims.COUNTERJIB_END) - 4
    elif cj_sup_type == 'None':
        start_cj_n = int(Dims.COUNTERJIB_END) - 2
    else:
        start_cj_n = int(Dims.COUNTERJIB_END) - 3
    for cj_n in range(start_cj_n, int(Dims.COUNTERJIB_END)):
        Conditions.p[cj_n, 0] = force * kN


def first_euler_buckling_case(length, flexural_strength):
    return ((np.pi ** 2) / (4 * length ** 2)) * flexural_strength


def second_euler_buckling_case(length, flexural_strength):
    return ((np.pi ** 2) / length ** 2) * flexural_strength


def third_euler_buckling_case(length, flexural_strength):
    return ((np.pi ** 2) / (0.7 * length) ** 2) * flexural_strength


def fourth_euler_buckling_case(length, flexural_strength):
    return (4 * (np.pi ** 2) / length ** 2) * flexural_strength


def is_euler_buckling_rod(E, A, DENSITY, length, force):
    mass = length * A * DENSITY
    # around where do we actually rotate? not the end?
    I_mid = (1 / 12) * mass * length ** 2
    I_end = (1 / 3) * mass * length ** 2
    flexural_strength = E * I_mid

    if force >= first_euler_buckling_case(length, flexural_strength):
        return True
    elif force >= second_euler_buckling_case(length, flexural_strength):
        return True
    elif force >= third_euler_buckling_case(length, flexural_strength):
        return True
    elif force >= fourth_euler_buckling_case(length, flexural_strength):
        return True
    else:
        return False


def analyze(nodes, beams, E, A, DENSITY):
    """Perform truss structural analysis"""
    # Adjust coordinates to m instead of mm
    # nodes = nodes / 1000

    number_of_nodes = len(nodes)
    number_of_elements = len(beams)

    # Degrees of freedom
    dof = 3
    total_number_of_dof = dof * number_of_nodes

    # structural analysis
    distance = nodes[beams[:, 1], :] - nodes[beams[:, 0], :]  # Distance between joints of the beam
    L = np.sqrt((distance ** 2).sum(axis=1))  # Length of each beam in meters
    angle = distance.transpose() / L  # Angle matrix
    transformation_vector = np.concatenate((- angle.transpose(), angle.transpose()), axis=1)  # Transformation vector
    K = np.zeros([total_number_of_dof, total_number_of_dof])  # Global stiffness matrix
    for k in range(number_of_elements):
        aux = dof * beams[k, :]
        index = np.r_[aux[0]:aux[0] + dof, aux[1]:aux[1] + dof]  # Save dof at each node
        elem_stiffness = np.dot(transformation_vector[k][np.newaxis].transpose() * E * A,
                                transformation_vector[k][np.newaxis]) / L[
                             k]  # Stiffness for each element (Local stiffness for each element)
        K[np.ix_(index, index)] = K[np.ix_(index, index)] + elem_stiffness

    free_dof = Conditions.dof_condition.flatten().nonzero()[0]  # Get all DOF that are NOT defined as zero (can move)
    support_dof = (Conditions.dof_condition.flatten() == 0).nonzero()[
        0]  # Get all DOF that are defined as zero (can't move; manully defined above)

    K_topleft = K[np.ix_(free_dof, free_dof)]  # Part of global stiffness matrix https://youtu.be/Y-ILnLMZYMw?t=2381
    K_topright = K[np.ix_(free_dof, support_dof)]  # See K_topleft
    K_bottomleft = K_topright.transpose()  # See K_topleft
    K_bottomright = K[np.ix_(support_dof, support_dof)]  # See K_topleft

    p_flatten = Conditions.p.flatten()[free_dof]  # Flatten only free_dof
    Uf = np.linalg.lstsq(K_topleft, p_flatten, rcond=None)[0]  # Deformation at all nodes with free DOF
    deformation = Conditions.dof_condition.astype(float).flatten()  # Contains all the deformation data
    deformation[free_dof] = Uf  # Deformation of all nodes that are free to move
    deformation[support_dof] = Conditions.Ur  # Deformation of all nodes that are fixed
    deformation = deformation.reshape(number_of_nodes, dof)  # Deformation vector for each node
    u = np.concatenate((deformation[beams[:, 0]], deformation[beams[:, 1]]),
                       axis=1)  # Deformed nodes for each beam? https://youtu.be/Y-ILnLMZYMw?t=3013
    axial_force = (E * A / L[:]) * (transformation_vector[:] * u[:]).sum(axis=1)  # Axial forces for each beam
    reaction_force = (K_bottomleft[:] * Uf).sum(axis=1) + (K_bottomright[:] * Conditions.Ur).sum(
        axis=1)  # Reaction forces in fixed nodes
    reaction_force = reaction_force.reshape(4, dof)

    for i in range(number_of_elements):
        n = axial_force[i]
        l = L[i]
        if is_euler_buckling_rod(E, A, DENSITY, l, n):
            print(f"{i} is euler buckling rod!")

    return np.array(axial_force), np.array(reaction_force), deformation


def optimize(nodes, beams, axial_force, E, A, DENSITY):
    area_per_rod = np.zeros(len(beams))
    # Make all rods have the same area
    for i in range(len(beams)):
        area_per_rod[i] = A
        current_tension = axial_force[i] / area_per_rod[i]
        max_tension = 2e+8
        min_tension = max_tension * (-1)
        if current_tension > max_tension:
            # Bad news, violates the requirements
            # Fix it by increasing the area
            a = axial_force[i] / max_tension
            area_per_rod[i] = axial_force[i] / max_tension
        elif current_tension < min_tension:
            a = axial_force[i] / min_tension
            area_per_rod[i] = axial_force[i] / min_tension

    number_of_nodes = len(nodes)
    number_of_elements = len(beams)

    # Degrees of freedom
    dof = 3
    total_number_of_dof = dof * number_of_nodes

    # structural analysis
    distance = nodes[beams[:, 1], :] - nodes[beams[:, 0], :]  # Distance between joints of the beam
    L = np.sqrt((distance ** 2).sum(axis=1))  # Length of each beam in meters
    angle = distance.transpose() / L  # Angle matrix
    transformation_vector = np.concatenate((- angle.transpose(), angle.transpose()), axis=1)  # Transformation vector
    K = np.zeros([total_number_of_dof, total_number_of_dof])  # Global stiffness matrix
    for k in range(number_of_elements):
        aux = dof * beams[k, :]
        index = np.r_[aux[0]:aux[0] + dof, aux[1]:aux[1] + dof]  # Save dof at each node
        elem_stiffness = np.dot(transformation_vector[k][np.newaxis].transpose() * E * area_per_rod[k],
                                transformation_vector[k][np.newaxis]) / L[
                             k]  # Stiffness for each element (Local stiffness for each element)
        K[np.ix_(index, index)] = K[np.ix_(index, index)] + elem_stiffness

    free_dof = Conditions.dof_condition.flatten().nonzero()[0]  # Get all DOF that are NOT defined as zero (can move)
    support_dof = (Conditions.dof_condition.flatten() == 0).nonzero()[
        0]  # Get all DOF that are defined as zero (can't move; manully defined above)

    K_topleft = K[np.ix_(free_dof, free_dof)]  # Part of global stiffness matrix https://youtu.be/Y-ILnLMZYMw?t=2381
    K_topright = K[np.ix_(free_dof, support_dof)]  # See K_topleft
    K_bottomleft = K_topright.transpose()  # See K_topleft
    K_bottomright = K[np.ix_(support_dof, support_dof)]  # See K_topleft

    p_flatten = Conditions.p.flatten()[free_dof]  # Flatten only free_dof
    Uf = np.linalg.lstsq(K_topleft, p_flatten, rcond=None)[0]  # Deformation at all nodes with free DOF
    deformation = Conditions.dof_condition.astype(float).flatten()  # Contains all the deformation data
    deformation[free_dof] = Uf  # Deformation of all nodes that are free to move
    deformation[support_dof] = Conditions.Ur  # Deformation of all nodes that are fixed
    deformation = deformation.reshape(number_of_nodes, dof)  # Deformation vector for each node
    u = np.concatenate((deformation[beams[:, 0]], deformation[beams[:, 1]]),
                       axis=1)  # Deformed nodes for each beam? https://youtu.be/Y-ILnLMZYMw?t=3013
    axial_force = (E * A / L[:]) * (transformation_vector[:] * u[:]).sum(axis=1)  # Axial forces for each beam
    reaction_force = (K_bottomleft[:] * Uf).sum(axis=1) + (K_bottomright[:] * Conditions.Ur).sum(
        axis=1)  # Reaction forces in fixed nodes
    reaction_force = reaction_force.reshape(4, dof)

    for i in range(number_of_elements):
        n = axial_force[i]
        l = L[i]
        if is_euler_buckling_rod(E, A, DENSITY, l, n):
            print(f"{i} is euler buckling rod!")

    return np.array(axial_force), np.array(reaction_force), deformation


    print(area_per_rod)
