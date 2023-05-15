"""
Provides all functions to analyze the behavior of the crane under load
"""
import numpy as np

class Conditions:
    """Conditions of parts of the crane"""
    Ur = []
    dof_condition = np.ones_like(0)
    p = np.zeros_like(0)


kN = 1e3

def generate_conditions(nodes):
    """Generates conditions for the crane"""
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

    # Applied forces
    p = np.zeros_like(nodes)
    # TODO change indices
    # Force on jib
    p[16, 2] = -250 * kN
    p[17, 2] = -250 * kN
    # Force on counter jib
    p[20, 2] = -100 * kN
    p[21, 2] = -100 * kN
    Conditions.p = p


def apply_gravity(nodes, beams, A, density):
    """Applies gravity to each node"""
    for i in range(len(nodes)):
        print(f'Run {i}')
        fitting_beams_lc = np.where(beams[:, 0] == 0)[0]
        fitting_beams_rc = np.where(beams[:, 1] == 0)[0]
        fitting_beams = np.concatenate((fitting_beams_lc, fitting_beams_rc), axis=None)
        length = 0
        for j in range(len(fitting_beams)):
            start_float = np.array(beams[fitting_beams[j], 0]).astype(float)
            end_float = np.array(beams[fitting_beams[j], 1]).astype(float)
            length += np.linalg.norm(end_float - start_float)
        Conditions.p[i, 2] += - ((length / 2) / 1000 * A * density * 9.81) * kN


def remove_gravity(nodes):
    """Resets nodes to default applied forces"""
    p = np.zeros_like(nodes)
    # TODO change indices
    # Force on jib
    p[16, 2] = -250 * kN
    p[17, 2] = -250 * kN
    # Force on counter jib
    p[20, 2] = -100 * kN
    p[21, 2] = -100 * kN
    Conditions.p = p


def analyze(nodes, beams, E, A):
    """Perform truss structural analysis"""
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
