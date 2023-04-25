"""
Provides all functions to build a crane plot the crane and deform it
"""

import matplotlib.pyplot as plt
import numpy as np

import tower
import jib

# Constants
E = 1e4
A = 0.111

# Create Tower
tower.create(1, True, True, tower.Style.DIAGONAL)
print(len(tower.get_nodes()), ' - ', len(tower.get_bars()))
# jib.create(0, 2000, 6000, 3)
jib.create_connected(tower.get_nodes_raw(), tower.get_bars_raw(), 2000, 2000, 2000, 1)
print(len(jib.get_nodes()), ' - ', len(jib.get_bars()))

# Override Python arrays with Numpy arrays, nodes are of type float64
# nodes = tower.get_nodes()
# bars = tower.get_bars()
nodes = jib.get_nodes()
bars = jib.get_bars()

# Applied forces
P = np.zeros_like(nodes)
# P[0, 0] = 1
# P[0, 1] = -10
# P[0, 2] = -10
# P[1, 1] = -10
# P[1, 2] = -10
# P[2, 0] = 0.5
# P[5, 0] = 0.6

# Support Displacement
Ur = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Condition of DOF (0 = fixed, 1 = free)
DOFCON = np.ones_like(nodes).astype(int)
DOFCON[0, :] = 0
DOFCON[1, :] = 0
DOFCON[2, :] = 0
DOFCON[3, :] = 0


def truss_analysis():
    """Performe truss structural analysis"""
    NN = len(nodes)
    NE = len(bars)
    DOF = 3
    NDOF = DOF * NN
    # structural analysis
    d = nodes[bars[:, 1], :] - nodes[bars[:, 0], :]
    L = np.sqrt((d ** 2).sum(axis=1))
    angle = d.T / L
    a = np.concatenate((-angle.T, angle.T), axis=1)
    K = np.zeros([NDOF, NDOF])
    for k in range(NE):
        aux = DOF * bars[k, :]
        index = np.r_[aux[0]:aux[0] + DOF, aux[1]:aux[1] + DOF]
        ES = np.dot(a[k][np.newaxis].T * E * A, a[k][np.newaxis]) / L[k]
        K[np.ix_(index, index)] = K[np.ix_(index, index)] + ES
    freeDOF = DOFCON.flatten().nonzero()[0]
    supportDOF = (DOFCON.flatten() == 0).nonzero()[0]
    Kff = K[np.ix_(freeDOF, freeDOF)]
    Kfr = K[np.ix_(freeDOF, supportDOF)]
    Krf = Kfr.T
    Krr = K[np.ix_(supportDOF, supportDOF)]
    Pf = P.flatten()[freeDOF]
    Uf = np.linalg.solve(Kff, Pf)
    U = DOFCON.astype(float).flatten()
    U[freeDOF] = Uf
    U[supportDOF] = Ur
    U = U.reshape(NN, DOF)
    u = np.concatenate((U[bars[:, 0]], U[bars[:, 1]]), axis=1)
    N = E * A / L[:] * (a[:] + u[:]).sum(axis=1)
    R = (Krf[:] * Uf).sum(axis=1) + (Krr[:] * Ur).sum(axis=1)
    R = R.reshape(4, DOF)
    return np.array(N), np.array(R), U


def plot(nodes, color, line_style, pen_width, label):
    """
    Plot nodes using matplotlib
    :param nodes: Numpy array containing the coordinates of each node in three-dimensional space
    :param color: Color of the edge
    :param line_style: Style of the edge
    :param pen_width: Width of the edge
    :param label: Name of the edge and what it should represent
    """
    # Create 3d environment
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # temp plot scaling
    # ax.set_box_aspect(aspect = (1, 1, 5)) # for tower
    # ax.set_box_aspect(aspect = (3, 1, 1)) # for jib

    for i in range(len(bars)):
        # Create initial and final coordinates
        xi, xf = nodes[bars[i, 0], 0], nodes[bars[i, 1], 0]
        yi, yf = nodes[bars[i, 0], 1], nodes[bars[i, 1], 1]
        zi, zf = nodes[bars[i, 0], 2], nodes[bars[i, 1], 2]
        # Create a Line3D object in list
        line = ax.plot([xi, xf], [yi, yf], [zi, zf], color=color, linestyle=line_style, linewidth=pen_width)
        # Override list with first element in list, always the Line3D object.
        line = line[0]
    line.set_label(label)
    plt.legend(prop={'size': 10})


# Run test with known data
# N, R, U = TrussAnalysis()
# print('Axial Forces (positive = tension, negative = compression)')
# print(N[np.newaxis].T)
# print('Reaction Forces (positive = upward, negative = downward)')
# print(R)
# print('Deformation at nodes')
# print(U)
plot(nodes, 'gray', '--', 1, 'Undeformed')
# scale = 1 #increase to make more evident in plot
# Dnodes = U * scale + nodes
# Plot(Dnodes, 'red', '-', 2, 'Deformed')
plt.axis("equal")
plt.show()
