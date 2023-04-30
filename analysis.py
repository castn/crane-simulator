"""
Provides all functions to analyze the behavior of the crane under load
"""
import numpy as np

from direct_stiffness_3d import E, A, nodes

# Applied forces
p = np.zeros_like(nodes)
p[16, 2] = -500
p[17, 2] = -500
p[20, 2] = -100
p[21, 2] = -100

# Support Displacement
Ur = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Condition of DOF (0 = fixed, 1 = free)
dof_condition = np.ones_like(nodes).astype(int)
dof_condition[0, :] = 0
dof_condition[1, :] = 0
dof_condition[2, :] = 0
dof_condition[3, :] = 0


def analyze(nodes, bars, dof_condition):
    """Performe truss structural analysis"""
    number_of_nodes = len(nodes)
    number_of_elements = len(bars)
    # Degree of freedom
    dof = 3
    total_number_of_dof = dof * number_of_nodes
    # structural analysis
    distance = nodes[bars[:, 1], :] - nodes[bars[:, 0], :]  # Distance between joints of the bar
    L = np.sqrt((distance ** 2).sum(axis=1))  # Length of each bar
    angle = distance.transpose() / L  # Angle matrix
    transformation_vector = np.concatenate((-angle.transpose(), angle.transpose()), axis=1) #Transformation vector
    K = np.zeros([total_number_of_dof, total_number_of_dof])  # Global stiffness matrix
    for k in range(number_of_elements):
        aux = dof * bars[k, :]
        index = np.r_[aux[0]:aux[0] + dof, aux[1]:aux[1] + dof]  # Save dof at each node
        ES = np.dot(transformation_vector[k][np.newaxis].transpose() * E * A, transformation_vector[k][np.newaxis]) / L[k]  # Stiffness for each element (Local stiffness for each element)
        K[np.ix_(index, index)] = K[np.ix_(index, index)] + ES
    free_dof = dof_condition.flatten().nonzero()[0]  # Get all DOF that are not defined as Zero (They can move)
    support_dof = (dof_condition.flatten() == 0).nonzero()[0]  # Get all DOF that are defined as Zero (Can not move, are manully defined above)
    Kff = K[np.ix_(free_dof, free_dof)]  # Teil der Globalen Steifigkeitsmatrix https://youtu.be/Y-ILnLMZYMw?t=2381
    Kfr = K[np.ix_(free_dof, support_dof)]  # Siehe Kff
    Krf = Kfr.transpose()  # Siehe Kff
    Krr = K[np.ix_(support_dof, support_dof)]  # Siehe Kff
    p_flatten = p.flatten()[free_dof]  # Flatten only free_dof
    Uf = np.linalg.solve(Kff, p_flatten)  # Internal forces? https://youtu.be/Y-ILnLMZYMw?t=2640
    U = dof_condition.astype(float).flatten()  # Contains all the deformation data
    U[free_dof] = Uf
    U[support_dof] = Ur
    U = U.reshape(number_of_nodes, dof)  # Deformation Vector for each element?
    u = np.concatenate((U[bars[:, 0]], U[bars[:, 1]]), axis=1)  # Deformed nodes for each bar? https://youtu.be/Y-ILnLMZYMw?t=3013
    N = E * A / L[:] * (transformation_vector[:] + u[:]).sum(axis=1)
    reaction_force = (Krf[:] * Uf).sum(axis=1) + (Krr[:] * Ur).sum(axis=1)  # Reaction force
    reaction_force = reaction_force.reshape(4, dof)
    return np.array(N), np.array(reaction_force), U
