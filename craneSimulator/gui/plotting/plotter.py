"""
Provides all functions to plot the crane and to display the plot
"""
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
import matplotlib.cm as cm

LINE_WIDTH = 1


# Create 3d environment


def plot(nodes, beams, color, line_style, label, ax, fig):
    """
    Plot nodes using matplotlib
    :param nodes: Numpy array containing the coordinates of each node in three-dimensional space
    :param beams: Array containing the nodes each beam is connected to
    :param color: Color of the edge
    :param line_style: Style of the edge
    :param pen_width: Width of the edge
    :param label: Name of the edge and what it should represent
    """

    for i in range(len(beams)):
        # Create initial and final coordinates
        xi, xf = nodes[beams[i, 0], 0], nodes[beams[i, 1], 0]
        yi, yf = nodes[beams[i, 0], 1], nodes[beams[i, 1], 1]
        zi, zf = nodes[beams[i, 0], 2], nodes[beams[i, 1], 2]
        # Create a Line3D object in list
        line = ax.plot([xi, xf], [yi, yf], [zi, zf], color=color, linestyle=line_style, linewidth=LINE_WIDTH)
        # Override list with first element in list, always the Line3D object.
        line = line[0]
        
        # ax.plot(xi, yi, zi, label=i) # Labels points on graph (I think)
    line.set_label(label)
    fig.legend(prop={'size': 10})
    fig.gca().set_aspect('equal')


def plot_deformation(nodes, deformed_nodes, beams, line_style, ax, fig):
    for i in range(len(beams)):
        # Undeformed nodes
        xi, xf = nodes[beams[i, 0], 0], nodes[beams[i, 1], 0]
        yi, yf = nodes[beams[i, 0], 1], nodes[beams[i, 1], 1]
        zi, zf = nodes[beams[i, 0], 2], nodes[beams[i, 1], 2]

        # Deformed nodes
        dxi, dxf = deformed_nodes[beams[i, 0], 0], deformed_nodes[beams[i, 1], 0]
        dyi, dyf = deformed_nodes[beams[i, 0], 1], deformed_nodes[beams[i, 1], 1]
        dzi, dzf = deformed_nodes[beams[i, 0], 2], deformed_nodes[beams[i, 1], 2]
        difference = np.array([[xi, xf], [yi, yf], [zi, zf]]) - np.array([[dxi, dxf], [dyi, dyf], [dzi, dzf]])

        if np.all(difference == np.array([[0,0],[0, 0],[0, 0]])):
            line = ax.plot([dxi, dxf], [dyi, dyf], [dzi, dzf], color="g", linestyle=line_style, linewidth=LINE_WIDTH)
        else:
            line = ax.plot([dxi, dxf], [dyi, dyf], [dzi, dzf], color="r", linestyle=line_style, linewidth=LINE_WIDTH)
        line = line[0]
    line.set_label("Deformed")
    fig.legend(prop={'size': 10})
    fig.gca().set_aspect('equal')
    

def plot_deformation_with_grad(nodes, deformed_nodes, beams, line_style, ax, fig, axial_forces):
    axial_forces = np.absolute(axial_forces)
    norm = mpl.colors.Normalize(min(axial_forces), max(axial_forces))
    cmap = cm.get_cmap('gist_heat')
    for i in range(len(beams)):
        # Deformed nodes
        dxi, dxf = deformed_nodes[beams[i, 0], 0], deformed_nodes[beams[i, 1], 0]
        dyi, dyf = deformed_nodes[beams[i, 0], 1], deformed_nodes[beams[i, 1], 1]
        dzi, dzf = deformed_nodes[beams[i, 0], 2], deformed_nodes[beams[i, 1], 2]

        line = ax.plot([dxi, dxf], [dyi, dyf], [dzi, dzf], color=cmap(norm(axial_forces[i])), linestyle=line_style, linewidth=LINE_WIDTH)
        line = line[0]
    line.set_label("Deformed")
    fig.legend(prop={'size': 10})
    fig.gca().set_aspect('equal')

def display():
    """Displays generated plot"""
    plt.axis("equal")
    plt.show()
