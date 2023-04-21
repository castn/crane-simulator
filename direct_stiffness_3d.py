import matplotlib.pyplot as plt
import numpy as np

# Constants
E = 1e4
A = 0.111
SEGMENT_WIDTH = 2000
SEGMENT_HEIGHT = 2000

nodes = []
bars = []


def create_tower(number_of_segments, is_hollow):
    create_segments(number_of_segments)
    create_beams(is_hollow, number_of_segments)


def create_beams(is_hollow, number_of_segments):
    for i in range(number_of_segments + 1):
        print(f'Create segment: {i}')
        create_horizontal_beams(i)
        if not is_hollow:
            bars.append([0 + 4 * i, 2 + 4 * i])
        if i < number_of_segments:
            create_vertical_beams(i)
            create_diagonal_beams(i)


def create_diagonal_beams(i):
    bars.append([0 + 4 * i, 5 + 4 * i])  # front face
    bars.append([5 + 4 * i, 2 + 4 * i])  # right face
    bars.append([2 + 4 * i, 7 + 4 * i])  # rear face
    bars.append([7 + 4 * i, 0 + 4 * i])  # left face


def create_vertical_beams(i):
    bars.append([0 + 4 * i, 4 + 4 * i])  # front_left_vertical beam
    bars.append([1 + 4 * i, 5 + 4 * i])  # front_right_vertical beam
    bars.append([3 + 4 * i, 7 + 4 * i])  # rear_left_vertical beam
    bars.append([2 + 4 * i, 6 + 4 * i])  # rear_right_vertical beam


def create_horizontal_beams(i):
    bars.append([0 + 4 * i, 1 + 4 * i])  # front_horizontal beam
    bars.append([1 + 4 * i, 2 + 4 * i])  # right_horizontal beam
    bars.append([2 + 4 * i, 3 + 4 * i])  # rear_horizontal beam
    bars.append([3 + 4 * i, 0 + 4 * i])  # left_horizontal beam


def create_segments(number_of_segments):
    for i in range(number_of_segments + 1):
        create_segment(i)


def create_segment(i):
    nodes.append([0, 0, SEGMENT_HEIGHT * i])
    nodes.append([SEGMENT_WIDTH, 0, SEGMENT_HEIGHT * i])
    nodes.append([SEGMENT_WIDTH, SEGMENT_WIDTH, SEGMENT_HEIGHT * i])
    nodes.append([0, SEGMENT_WIDTH, SEGMENT_HEIGHT * i])


create_tower(5, True)

# Override Python arrays with Numpy arrays, nodes are of type float64
nodes = np.array(nodes).astype(float)
bars = np.array(bars)

# Applied forces
P = np.zeros_like(nodes)
P[0, 0] = 1
P[0, 1] = -10
P[0, 2] = -10
P[1, 1] = -10
P[1, 2] = -10
P[2, 0] = 0.5
P[5, 0] = 0.6

# Support Displacement
Ur = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Condition of DOF (1 = free, 0 = fixed)
DOFCON = np.ones_like(nodes).astype(int)
DOFCON[0, :] = 0
DOFCON[1, :] = 0
DOFCON[2, :] = 0
DOFCON[3, :] = 0


# Truss structural analysis
def TrussAnalysis():
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


def Plot(nodes, color, line_style, pen_width, label):
    """
    Plot nodes using matplotlib
    :param nodes: Numpy array containing the coordinates of each node in three-dimensional space
    :param color: Color of the edge
    :param line_style: Style of the edge
    :param pen_width: Width of the edge
    :param label: Name of the edge and what it should represent
    """
    # Create 3d environment
    plt.axes(projection='3d')
    for i in range(len(bars)):
        # Create two variables at the same time.
        xi, xf = nodes[bars[i, 0], 0], nodes[bars[i, 1], 0]
        yi, yf = nodes[bars[i, 0], 1], nodes[bars[i, 1], 1]
        zi, zf = nodes[bars[i, 0], 2], nodes[bars[i, 1], 2]
        # Create a Line3D object in list
        line = plt.plot([xi, xf], [yi, yf], [zi, zf], color=color, linestyle=line_style, linewidth=pen_width)
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
Plot(nodes, 'gray', '--', 1, 'Undeformed')
# scale = 1 #increase to make more evident in plot
# Dnodes = U * scale + nodes
# Plot(Dnodes, 'red', '-', 2, 'Deformed')
plt.show()
