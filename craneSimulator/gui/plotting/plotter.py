"""
Provides all functions to plot the crane and to display the plot
"""
import matplotlib as mpl
import matplotlib.cm as cm
import numpy as np
from matplotlib import pyplot as plt

LINE_WIDTH = 1


class PlotterManager:
    def __init__(self, has_gradient, cmap_deformation, cmap_area):
        self.has_gradient = has_gradient
        self.cmap_deformation = cmap_deformation
        self.cmap_area = cmap_area

    def create_plots(self, nodes, deformed_nodes, o_deformed_nodes, beams, area_per_rod, o_area_per_rod, fig, N, o_N):
        ax_tl = fig.add_subplot(2, 2, 1, projection='3d')
        ax_tr = fig.add_subplot(2, 2, 2, projection='3d')
        ax_bl = fig.add_subplot(2, 2, 3, projection='3d')
        ax_br = fig.add_subplot(2, 2, 4, projection='3d')
        ax_tl.set_title("Deformation (Unoptimized)")
        ax_tr.set_title("Cross section area (Unoptimized)")
        ax_bl.set_title("Deformation (Optimized)")
        ax_br.set_title("Cross section area (Optimized)")
        # Set view point (camera angle)
        # Here set to display z,x plane
        ax_tl.view_init(0, -90, 0)
        ax_tr.view_init(0, -90, 0)
        ax_bl.view_init(0, -90, 0)
        ax_br.view_init(0, -90, 0)

        # Plot unoptimized crane
        plot(nodes, beams, "grey", "--", "Undeformed", ax_tl, fig)
        plot_deformation_with_grad(deformed_nodes, beams, '-', ax_tl, fig, N, self.cmap_deformation)
        plot_area_with_grad(nodes, beams, '-', ax_tr, fig, area_per_rod, self.cmap_area)
        # Plot optimized crane
        plot(nodes, beams, "grey", "--", "Undeformed", ax_bl, fig)
        plot_deformation_with_grad(o_deformed_nodes, beams, '-', ax_bl, fig, o_N, self.cmap_deformation)
        plot_area_with_grad(nodes, beams, '-', ax_br, fig, o_area_per_rod, self.cmap_area)


def plot(nodes, beams, color, line_style, label, axes, fig):
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
        line = axes.plot([xi, xf], [yi, yf], [zi, zf], color=color, linestyle=line_style, linewidth=LINE_WIDTH)
        # Override list with first element in list, always the Line3D object.
        line = line[0]

        # ax.plot(xi, yi, zi, label=i) # Labels points on graph (I think)
    line.set_label(label)
    axes.legend(prop={'size': 10})


def plot_deformation_with_grad(deformed_nodes, beams, line_style, ax, fig, axial_forces, cmap_type):
    axial_forces = np.absolute(axial_forces)
    norm = mpl.colors.Normalize(min(axial_forces), max(axial_forces))
    cmap = cm.get_cmap(cmap_type.currentText())
    for i in range(len(beams)):
        # Deformed nodes
        dxi, dxf = deformed_nodes[beams[i, 0], 0], deformed_nodes[beams[i, 1], 0]
        dyi, dyf = deformed_nodes[beams[i, 0], 1], deformed_nodes[beams[i, 1], 1]
        dzi, dzf = deformed_nodes[beams[i, 0], 2], deformed_nodes[beams[i, 1], 2]

        line = ax.plot([dxi, dxf], [dyi, dyf], [dzi, dzf], color=cmap(norm(axial_forces[i])), linestyle=line_style,
                       linewidth=LINE_WIDTH)
        line = line[0]
    line.set_label("Deformed")
    # ax.legend(handles=create_colormap_gradient(axial_forces, cmap), prop={'size': 0}, loc='upper left',
    #            title='Absolute axial forces')


def plot_area_with_grad(nodes, beams, line_style, ax, fig, area_per_rod, cmap_type):
    norm = mpl.colors.Normalize(min(area_per_rod), max(area_per_rod))
    cmap = cm.get_cmap("rainbow")
    for i in range(len(beams)):
        # Undeformed nodes
        xi, xf = nodes[beams[i, 0], 0], nodes[beams[i, 1], 0]
        yi, yf = nodes[beams[i, 0], 1], nodes[beams[i, 1], 1]
        zi, zf = nodes[beams[i, 0], 2], nodes[beams[i, 1], 2]

        line = ax.plot([xi, xf], [yi, yf], [zi, zf], color=cmap(norm(area_per_rod[i])), linestyle=line_style,
                       linewidth=LINE_WIDTH)
        line = line[0]
    # ax.legend(handles=create_colormap_gradient(area_per_rod, cmap), prop={'size': 0}, loc='upper left',
    #            title='Absolute area')
    fig.gca().set_aspect('equal')


def create_colormap_gradient(value, cmap):
    gradient = np.linspace(0, 1, 256)
    cmap_legend = []
    for i in range(len(gradient)):
        if i == 0:
            cmap_legend.append(mpl.lines.Line2D([0], [0], color=cmap(i), label=f'Low ({min(value):.0f})'))
        elif i == 255:
            cmap_legend.append(mpl.lines.Line2D([0], [0], color=cmap(i), label=f'High ({max(value):.0f})'))
        else:
            cmap_legend.append(mpl.lines.Line2D([0], [0], color=cmap(i)))
    # cmap_legend = [mpl.lines.Line2D([0], [0], color=cmap(0.), lw=4, label=f'Low ({min(axial_forces):.0f})'),
    #                mpl.lines.Line2D([0], [0], color=cmap(.5), lw=4, label='Medium'),
    #                mpl.lines.Line2D([0], [0], color=cmap(1.), lw=4, label=f'High ({max(axial_forces):.0f})')]
    return cmap_legend


def display():
    """Displays generated plot"""
    plt.axis("equal")
    plt.show()
