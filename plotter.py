"""
Provides all functions to plot the crane and to display the plot
"""
from matplotlib import pyplot as plt

LINE_WIDTH = 1

# Create 3d environment
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


def plot(nodes, bars, color, line_style, label):
    """
    Plot nodes using matplotlib
    :param nodes: Numpy array containing the coordinates of each node in three-dimensional space
    :param bars: Array containing the nodes each bar is connected to
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
        line = ax.plot([xi, xf], [yi, yf], [zi, zf], color=color, linestyle=line_style, linewidth=LINE_WIDTH)
        # Override list with first element in list, always the Line3D object.
        line = line[0]
    line.set_label(label)
    plt.legend(prop={'size': 10})


def display():
    plt.axis("equal")
    plt.show()
