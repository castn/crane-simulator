"""
Provides all functions to plot the crane and to display the plot
"""
import matplotlib as mpl
import matplotlib.cm as cm
import numpy as np
from matplotlib import pyplot as plt

LINE_WIDTH = 1


def set_default_settings(ax, title):
    # Set view point (camera angle)
    # Here set to display z,x plane
    ax.view_init(0, -90, 0)
    # Set labels for axis
    ax.set_xlabel("X - Achse")
    # ax.set_ylabel("Y - Achse")
    ax.set_zlabel("Z - Achse")
    # Set title of subplot
    ax.set_title(title)
    ax.set_yticks([])


class PlotterManager:
    def __init__(self, has_gradient, cmap_deformation, cmap_area, u_fig, opt_fig):
        self.has_gradient = has_gradient
        self.cmap_deformation = cmap_deformation
        self.cmap_area = cmap_area
        self.unoptim_fig = u_fig
        self.optim_fig = opt_fig
        self.unoptim_ax_l = u_fig.add_subplot(1, 2, 1, projection='3d')
        self.unoptim_ax_r = u_fig.add_subplot(1, 2, 2, projection='3d')
        self.optim_ax_l = opt_fig.add_subplot(1, 2, 1, projection='3d')
        self.optim_ax_r = opt_fig.add_subplot(1, 2, 2, projection='3d')
        set_default_settings(self.unoptim_ax_l, "Deformation")
        set_default_settings(self.unoptim_ax_r, "Cross section area")
        set_default_settings(self.optim_ax_l, "Deformation")
        set_default_settings(self.optim_ax_r, "Cross section area")

    def update_unoptimized_plots(self, nodes, deformed_nodes, beams, area_per_rod, N, end_crane_parts):
        # Plot unoptimized crane
        simple_plot(nodes, beams, "grey", "--", "Undeformed", self.unoptim_ax_l, end_crane_parts[1], end_crane_parts[2])
        plot_deformation_with_grad(deformed_nodes, beams, '-', self.unoptim_ax_l, N, self.cmap_deformation)
        plot_area_with_grad(nodes, beams, '-', self.unoptim_ax_r, self.unoptim_fig, area_per_rod)
        # print(u_ax_l.get_xticklabels())
        # u_ax_l.set_xticklabels(u_ax_l.get_xticklabels(), rotation=45)
        # u_ax_l.set_zticklabels(u_ax_l.get_zticklabels(), rotation=45)

    def update_optimized_plots(self, nodes, opt_deformed_nodes, beams, opt_area_per_rod, opt_N):
        # Plot optimized crane
        simple_plot(nodes, beams, "grey", "--", "Undeformed", self.optim_ax_l, 5, 5)
        plot_deformation_with_grad(opt_deformed_nodes, beams, '-', self.optim_ax_l, opt_N, self.cmap_deformation)
        plot_area_with_grad(nodes, beams, '-', self.optim_ax_r, self.optim_fig, opt_area_per_rod)
        # print(u_ax_l.get_xticklabels())
        # u_ax_l.set_xticklabels(u_ax_l.get_xticklabels(), rotation=45)
        # u_ax_l.set_zticklabels(u_ax_l.get_zticklabels(), rotation=45)


def simple_plot(nodes, beams, color, line_style, label, axes, end_jib, end_cj):
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

    for i in range(len(nodes)):
        x = nodes[i, 0]
        y = nodes[i, 1]
        z = nodes[i, 2]
        if i == end_jib - 1 or i == end_jib - 2:
            axes.quiver(x, y, z, 0, 0, -180, color='r', length=5)
        if i == end_cj - 1 or i == end_cj - 2:
            axes.quiver(x, y, z, 0, 0, -180, color='g', length=5)

    line.set_label(label)
    axes.legend(prop={'size': 10})


def plot_deformation_with_grad(deformed_nodes, beams, line_style, ax, axial_forces, cmap_type):
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
    ax.set_aspect("equal")
    # ax.legend(handles=create_colormap_gradient(axial_forces, cmap), prop={'size': 0}, loc='upper left',
    #            title='Absolute axial forces')


def plot_area_with_grad(nodes, beams, line_style, ax, fig, area_per_rod):
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
