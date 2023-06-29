"""
Provides all functions to analyze the behavior of the crane under load
"""
import numpy as np


class Conditions:
    """Conditions of parts of the crane"""
    def_fixed_nodes = []
    dof_condition = np.ones_like(0)
    forces = np.zeros_like(0)
    area_per_beam = 0
    abs_max_tension = 2e+8


class Comps():
    nodes = []


class Dims():
    TOWER_END = 0
    JIB_END = 0
    COUNTERJIB_END = 0
    length_of_each_beam = 0


def get_length_of_each_beam():
    return Dims.length_of_each_beam


kN = 1e3


def generate_conditions(nodes, beams):
    """Generates conditions for the crane"""
    Comps.nodes = nodes

    # Support Displacement
    Conditions.def_fixed_nodes = [0, 0, 0,
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

    Conditions.area_per_beam = np.full((len(beams)), 0.0025)


def apply_forces(window, nodes, end_tower, end_jib):
    """Applies user-entered forces"""
    Comps.nodes = nodes
    Dims.TOWER_END = end_tower
    Dims.JIB_END = end_jib
    Dims.COUNTERJIB_END = len(nodes)

    # Applied forces
    p = np.zeros_like(nodes)
    # Force on jib
    p[Dims.JIB_END - 2, 2] = window.jib_left_spinBox.value() * kN
    p[Dims.JIB_END - 1, 2] = window.jib_right_spinBox.value() * kN
    # Force on counter jib
    p[Dims.COUNTERJIB_END - 2, 2] = window.counterjib_left_spinBox.value() * kN
    p[Dims.COUNTERJIB_END - 1, 2] = window.counterjib_left_spinBox.value() * kN
    Conditions.forces = p


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
        Conditions.forces[i, 2] += - ((length / 2) / 1000 * A * density * grav_const) * kN


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
        Conditions.forces[(1 + 2 * t_n), 1] = force * kN
    # jib: 0+3n (top), 2+3n (bot)
    for j_n in range(int(Dims.TOWER_END), int(Dims.JIB_END / 3)):
        Conditions.forces[(0 + 3 * j_n), 1] = force * kN
        Conditions.forces[(2 + 3 * j_n), 1] = force * kN
    # counterjib: top center for 1-2 towers, rest just for truss
    for cj_n in range(int(Dims.JIB_END), int(cj_end / 2)):
        Conditions.forces[Dims.JIB_END + (1 + 2 * j_n), 1] = force * kN
    if cj_sup_type == 'Truss':
        for cj_n in range(cj_end, int(Dims.COUNTERJIB_END)):
            Conditions.forces[cj_n, 1] = force * kN
    elif cj_sup_type == 'Single tower':
        Conditions.forces[int(Dims.COUNTERJIB_END), 1] = force * kN
    elif cj_sup_type == 'Twin towers':
        Conditions.forces[int(Dims.COUNTERJIB_END) - 1, 1] = force * kN


def apply_wind_right(force):
    # force in east dir
    # -x
    # tower: 2+4n, 3+4n
    for t_n in range(int(Dims.TOWER_END / 4) - 1):
        Conditions.forces[(2 + 4 * t_n), 0] = - force * kN
        Conditions.forces[(3 + 4 * t_n), 0] = - force * kN
    # jib: last 3
    for j_n in range(int(Dims.JIB_END) - 3, int(Dims.JIB_END)):
        Conditions.forces[j_n, 0] = - force * kN
    # counterjib: none


def apply_wind_back(force, cj_sup_type, cj_end):
    # force in south dir
    # -y dir
    # tower: all even nodes
    for t_n in range(Dims.TOWER_END):
        Conditions.forces[2 * t_n, 1] = - force * kN
    print('Completed tower')
    # jib: 0+3n (top), 1+3n (bot)
    for j_n in range(Dims.TOWER_END, int(Dims.JIB_END / 3)):
        Conditions.forces[(0 + 3 * j_n), 1] = - force * kN
        Conditions.forces[(1 + 3 * j_n), 1] = - force * kN
    print('Completed jib')
    # counterjib: top center for 1-2 towers, rest just for truss
    for cj_n in range(int(Dims.JIB_END), int(cj_end / 2)):
        Conditions.forces[Dims.JIB_END + (0 + 2 * j_n), 1] = - force * kN
    if cj_sup_type == 'Truss':
        for cj_n in range(cj_end, int(Dims.COUNTERJIB_END)):
            Conditions.forces[cj_n, 1] = - force * kN
    elif cj_sup_type == 'Single tower' or cj_sup_type == 'Twin towers':
        Conditions.forces[int(Dims.COUNTERJIB_END), 1] = - force * kN


def apply_wind_left(force, cj_sup_type):
    # force in west dir
    # +x dir
    # tower: 2+4n, 3+4n
    for t_n in range(int(Dims.TOWER_END / 4) - 1):
        Conditions.forces[(0 + 4 * t_n), 0] = force * kN
        Conditions.forces[(1 + 4 * t_n), 0] = force * kN
    # jib: none
    # counterjib: truss last 3; last 2 plus tower
    if cj_sup_type == 'Twin towers':
        start_cj_n = int(Dims.COUNTERJIB_END) - 4
    elif cj_sup_type == 'None':
        start_cj_n = int(Dims.COUNTERJIB_END) - 2
    else:
        start_cj_n = int(Dims.COUNTERJIB_END) - 3
    for cj_n in range(start_cj_n, int(Dims.COUNTERJIB_END)):
        Conditions.forces[cj_n, 0] = force * kN


def first_euler_buckling_case(length, flexural_strength):
    return ((np.pi ** 2) / (4 * length ** 2)) * flexural_strength


def second_euler_buckling_case(length, flexural_strength):
    return ((np.pi ** 2) / length ** 2) * flexural_strength


def third_euler_buckling_case(length, flexural_strength):
    return ((np.pi ** 2) / (0.7 * length) ** 2) * flexural_strength


def fourth_euler_buckling_case(length, flexural_strength):
    return (4 * (np.pi ** 2) / length ** 2) * flexural_strength


def is_euler_buckling_rod(E, A, DENSITY, length, force):
    """Checks if rod buckles"""
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


def analyze(nodes, beams, E, DENSITY):
    """Perform truss structural analysis"""
    number_of_nodes = len(nodes)
    number_of_elements = len(beams)

    # Degrees of freedom
    dof = 3
    total_number_of_dof = dof * number_of_nodes
    free_dof, support_dof = get_DOFs()

    # Structural analysis
    distance = nodes[beams[:, 1], :] - nodes[beams[:, 0], :]                                            # Distance between joints of the beam
    L = np.sqrt((distance ** 2).sum(axis=1))                                                            # Length of each beam in meters
    Dims.length_of_each_beam = L
    rotation = distance.transpose() / L                                                                 # rotation matrix
    transformation_vector = np.concatenate((- rotation.transpose(), rotation.transpose()), axis=1)      # Transformation vector

    # Stiffness
    K = calculate_global_stiffness(E, L, beams, dof, number_of_elements, total_number_of_dof, transformation_vector)
    K_bottomleft, K_bottomright, K_topleft = get_components_of_global_stiffness(K, free_dof, support_dof)

    # Deformation
    forces_flatten = Conditions.forces.flatten()[free_dof]                                              # Flatten only free_dof
    def_free_nodes = np.linalg.lstsq(K_topleft, forces_flatten, rcond=None)[0]                          # Deformation at all nodes with free DOF
    deformation, u = calculate_deformation(def_free_nodes, beams, dof, free_dof, number_of_nodes, support_dof)
    
    # Calculate axial forces for each beam
    axial_force = (E * Conditions.area_per_beam / L[:]) * (transformation_vector[:] * u[:]).sum(axis=1)

    # Test each beam for euler buckling
    for i in range(number_of_elements):
        n = axial_force[i]
        l = L[i]
        A = Conditions.area_per_beam[i]
        if is_euler_buckling_rod(E, A, DENSITY, l, n):
            print(f"{i} is euler buckling rod!")

    # Calculate all reaction forces
    reaction_force = calculate_reaction_forces(K_bottomleft, K_bottomright, def_free_nodes, dof)

    return np.array(axial_force), np.array(reaction_force), deformation
    # Uf: deformation of all nodes allowed to deform (new coords) -> def_free_nodes
    # Ur: coords of nodes that aren't allowed to move (same coords) -> def_fixed_nodes


def get_DOFs():
    """Returns the free and fixed degrees of freedom"""
    free_dof = Conditions.dof_condition.flatten().nonzero()[0]              # Get all DOF that are NOT defined as zero (can move)
    support_dof = (Conditions.dof_condition.flatten() == 0).nonzero()[0]    # Get all DOF that are defined as zero (can't move; manully defined above)
    return free_dof, support_dof


def calculate_reaction_forces(K_bottomleft, K_bottomright, def_free_nodes, dof):
    """Calculates reaction forces in fixed nodes caused by deformation"""
    reaction_force = (K_bottomleft[:] * def_free_nodes).sum(axis=1) + (K_bottomright[:] * Conditions.def_fixed_nodes).sum(axis=1)    # Reaction forces in fixed nodes
    reaction_force = reaction_force.reshape(4, dof)
    return reaction_force


def calculate_deformation(def_free_nodes, beams, dof, free_dof, number_of_nodes, support_dof):
    """Combines individual deformations into a single matrix"""
    deformation = Conditions.dof_condition.astype(float).flatten()                      # Matrix containing all the deformation data
    deformation[free_dof] = def_free_nodes                                              # Deformation of all nodes that are free to move
    deformation[support_dof] = Conditions.def_fixed_nodes                               # Deformation of all nodes that are fixed
    deformation = deformation.reshape(number_of_nodes, dof)                             # Deformation vector for each node
    u = np.concatenate((deformation[beams[:, 0]], deformation[beams[:, 1]]), axis=1)    # Deformed nodes for each beam? https://youtu.be/Y-ILnLMZYMw?t=3013
    return deformation, u


def calculate_global_stiffness(E, L, beams, dof, number_of_elements, total_number_of_dof, transformation_vector):
    """Calculates the global stiffness matrix"""
    # Empty matrix with required dimension for the stiffness matrix
    K = np.zeros([total_number_of_dof, total_number_of_dof])
    # Fill global stiffness matrix
    for k in range(number_of_elements):
        tmp = dof * beams[k, :]
        # (Local) Stiffness for each element
        elem_stiffness = np.dot(transformation_vector[k][np.newaxis].transpose() * E * Conditions.area_per_beam[k],
                                transformation_vector[k][np.newaxis]) / L[k]
        # Index where local stiffness should be placed in global stiffness
        index = np.r_[tmp[0]:tmp[0] + dof, tmp[1]:tmp[1] + dof]
        K[np.ix_(index, index)] = K[np.ix_(index, index)] + elem_stiffness
    return K


def get_components_of_global_stiffness(K, free_dof, support_dof):
    """Splits up the global stiffness matrix into 4 components"""
    K_topleft = K[np.ix_(free_dof, free_dof)]               # Part of global stiffness matrix
    K_topright = K[np.ix_(free_dof, support_dof)]           # See K_topleft
    K_bottomleft = K_topright.transpose()                   # See K_topleft
    K_bottomright = K[np.ix_(support_dof, support_dof)]     # See K_topleft
    return K_bottomleft, K_bottomright, K_topleft


def optimize(nodes, beams, E, DENSITY):
    """Optimizes the crane to try to be within given specifications"""
    for _ in range(4):
        axial_force = analyze(nodes, beams, E, DENSITY)
        adjust_cross_section_area(axial_force[0])
    axial_force, reaction_force, deformation = analyze(nodes, beams, E, DENSITY)
    return axial_force, reaction_force, deformation, Conditions.area_per_beam


def get_area_per_beam():
    """Returns array containing the areas of each beam"""
    return Conditions.area_per_beam


def adjust_cross_section_area(axial_force):
    for i in range(len(Conditions.area_per_beam)):
        current_tension = abs(axial_force[i] / Conditions.area_per_beam[i])
        if current_tension > Conditions.abs_max_tension:
            # Bad news, violates the requirements
            # Fix it by increasing the area
            # a = axial_force[i] / abs_max_tension
            Conditions.area_per_beam[i] += 3 * Conditions.area_per_beam[i]  # increase side length by 5cm
