"""
Provides all functions to build a crane plot the crane and deform it
"""

import matplotlib.pyplot as plt
import numpy as np

import tower
import jib
import crane

# Constants
# Youngs Module
E = 210e6  # 210GPa
# Cross section of each beam
A = 0.01  # 0.01m^2

# Create crane
crane.create_crane()
print(f'Total length: {crane.get_length() / 1000} m')
print(f'Total volume: {crane.get_length() / 1000 * A} m^3')
density = 7850
print(f'Total mass: {crane.get_length() / 1000 * A * density} kg with a cost of {crane.get_length() / 1000 * A * density / 1000 * 1000} euros')
# crane.create_counter_jib()

# Override Python arrays with Numpy arrays, nodes are of type float64
nodes, bars = crane.get_counter_jib()


def plot(nodes, color, line_style, pen_width, label):
    """
    Plot nodes using matplotlib
    :param nodes: Numpy array containing the coordinates of each node in three-dimensional space
    :param color: Color of the edge
    :param line_style: Style of the edge
    :param pen_width: Width of the edge
    :param label: Name of the edge and what it should represent
    """

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


# Create 3d environment
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

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
# plot(nodes, 'red', '-', 2, 'Deformed')
plt.axis("equal")
plt.show()
