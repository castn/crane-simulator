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
                     0, 0, 0] # nodes 0-4 in xyz

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


def apply_gravity(nodes, beams, A, density):
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
        Conditions.p[i, 2] += - ((length / 2) / 1000 * A * density * 9.81) * kN


def apply_wind(direc, force):
    """Applies wind in specified direction with specified force to the crane"""
    print(f'{direc} - {force}')
    if direc == 'from front':
        # force in north dir
        # -y dir
        # tower: all odd nodes
        print(Dims.TOWER_END / 2)
        for t_n in range(int(Dims.TOWER_END / 2)):
            Conditions.p[(2 * t_n + 1), 1] = - force * kN
        # jib: 0+3n (top), 2+3n (bot)
        print(Dims.JIB_END / 3)
        for j_n in range(int(Dims.TOWER_END), int(Dims.JIB_END / 3)):
            Conditions.p[(0 + 3 * j_n), 1] = - force * kN
            Conditions.p[(2 + 3 * j_n), 1] = - force * kN
        # counterjib: top center for 1-2 towers, rest just for truss
    elif direc == 'from right':
        # force in east dir
        # -x
        # tower: 2+4n, 3+4n
        print()
    elif direc == 'from back':
        # force in south dir
        # +y dir
        # tower: all even nodes
        for t_n in range(Dims.TOWER_END):
            Conditions.p[2 * t_n, 1] = force * kN
        # jib: 0+3n (top), 1+3n (bot)
        for j_n in range(Dims.TOWER_END, Dims.JIB_END):
            Conditions.p[(0 + 3 * j_n), 1] = force * kN
            Conditions.p[(1 + 3 * j_n), 1] = force * kN
        print()
    elif direc == 'from left':
        # force in west dir
        # +x dir
        print()
    print('Hm not a valid direction')


def analyze(nodes, beams, E, A):
    """Perform truss structural analysis"""
    print('Forces')
    print(Conditions.p)
    number_of_nodes = len(nodes)
    number_of_elements = len(beams)

    # Degrees of freedom
    dof = 3
    total_number_of_dof = dof * number_of_nodes

    # structural analysis
    distance = nodes[beams[:, 1], :] - nodes[beams[:, 0], :]                                                                # Distance between joints of the beam
    L = np.sqrt((distance ** 2).sum(axis=1))                                                                                # Length of each beam
    angle = distance.transpose() / L                                                                                        # Angle matrix
    transformation_vector = np.concatenate((- angle.transpose(), angle.transpose()), axis=1)                                # Transformation vector
    K = np.zeros([total_number_of_dof, total_number_of_dof])                                                                # Global stiffness matrix
    for k in range(number_of_elements):
        aux = dof * beams[k, :]
        index = np.r_[aux[0]:aux[0] + dof, aux[1]:aux[1] + dof]  # Save dof at each node
        ES = np.dot(transformation_vector[k][np.newaxis].transpose() * E * A, transformation_vector[k][np.newaxis]) / L[k]  # Stiffness for each element (Local stiffness for each element)
        K[np.ix_(index, index)] = K[np.ix_(index, index)] + ES
    
    free_dof = Conditions.dof_condition.flatten().nonzero()[0]                                                              # Get all DOF that are NOT defined as zero (can move)
    support_dof = (Conditions.dof_condition.flatten() == 0).nonzero()[0]                                                    # Get all DOF that are defined as zero (can't move; manully defined above)
    
    K_topleft = K[np.ix_(free_dof, free_dof)]                                                                               # Teil der Globalen Steifigkeitsmatrix https://youtu.be/Y-ILnLMZYMw?t=2381
    K_topright = K[np.ix_(free_dof, support_dof)]                                                                           # Siehe K_topleft
    K_bottomleft = K_topright.transpose()                                                                                   # Siehe K_topleft
    K_bottomright = K[np.ix_(support_dof, support_dof)]                                                                     # Siehe K_topleft
    
    p_flatten = Conditions.p.flatten()[free_dof]                                                                            # Flatten only free_dof
    Uf = np.linalg.lstsq(K_topleft, p_flatten, rcond=None)[0]                                                               # Deformation at all nodes with free DOF
    U = Conditions.dof_condition.astype(float).flatten()                                                                    # Contains all the deformation data
    U[free_dof] = Uf
    U[support_dof] = Conditions.Ur
    U = U.reshape(number_of_nodes, dof)                                                                                     # Deformation vector for each node
    u = np.concatenate((U[beams[:, 0]], U[beams[:, 1]]), axis=1)                                                            # Deformed nodes for each beam? https://youtu.be/Y-ILnLMZYMw?t=3013
    N = E * A / L[:] * (transformation_vector[:] + u[:]).sum(axis=1)
    reaction_force = (K_bottomleft[:] * Uf).sum(axis=1) + (K_bottomright[:] * Conditions.Ur).sum(axis=1)                    # Reaction force
    reaction_force = reaction_force.reshape(4, dof)
    return np.array(N), np.array(reaction_force), U
