"""
Provides all functions to plot the crane and to display the plot
"""
import matplotlib as mpl
import matplotlib.cm as cm
import numpy as np
from matplotlib import pyplot as plt
from numpy.linalg import norm

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
    def __init__(self, has_gradient, cmap_deformation, cmap_area, u_fig, opt_fig, diff_fig):
        self.has_gradient = has_gradient
        self.cmap_deformation = cmap_deformation
        self.cmap_area = cmap_area
        self.unoptim_fig = u_fig
        self.optim_fig = opt_fig
        self.diff_fig = diff_fig
        self.unoptim_ax_l = self.unoptim_fig.add_subplot(1, 2, 1, projection='3d')
        self.unoptim_ax_r = self.unoptim_fig.add_subplot(1, 2, 2, projection='3d')
        self.optim_ax_l = self.optim_fig.add_subplot(1, 2, 1, projection='3d')
        self.optim_ax_r = self.optim_fig.add_subplot(1, 2, 2, projection='3d')
        self.diff_ax_l = self.diff_fig.add_subplot(1, 2, 1, projection='3d')
        self.diff_ax_r = self.diff_fig.add_subplot(1, 2, 2, projection='3d')
        set_default_settings(self.unoptim_ax_l, "Deformation")
        set_default_settings(self.unoptim_ax_r, "Cross section area")
        set_default_settings(self.optim_ax_l, "Deformation")
        set_default_settings(self.optim_ax_r, "Cross section area")
        set_default_settings(self.diff_ax_l, "Comparison base (old)")
        set_default_settings(self.diff_ax_r, "Current (new)")

    def update_unoptimized_plots(self, nodes, deformed_nodes, beams, area_per_rod, axial_forces, end_crane_parts, loads):
        """Plots unoptimized crane"""
        simple_plot(nodes, beams, "grey", "--", "Undeformed", self.unoptim_ax_l,
                    end_crane_parts[1], end_crane_parts[2], loads[0], loads[1])
        plot_deformation_with_grad(deformed_nodes, beams, '-', self.unoptim_ax_l,
                                   axial_forces, self.cmap_deformation)
        plot_area_with_grad(nodes, beams, '-', self.unoptim_ax_r, self.unoptim_fig, area_per_rod)
        # print(u_ax_l.get_xticklabels())
        # u_ax_l.set_xticklabels(u_ax_l.get_xticklabels(), rotation=45)
        # u_ax_l.set_zticklabels(u_ax_l.get_zticklabels(), rotation=45)

    def update_optimized_plots(self, nodes, opt_deformed_nodes, beams, opt_area_per_rod,
                               optm_axial_forces, end_crane_parts, loads):
        """Plot optimized crane"""
        simple_plot(nodes, beams, "grey", "--", "Undeformed", self.optim_ax_l,
                    end_crane_parts[1], end_crane_parts[2], loads[0], loads[1])
        plot_deformation_with_grad(opt_deformed_nodes, beams, '-', self.optim_ax_l,
                                   optm_axial_forces, self.cmap_deformation)
        plot_area_with_grad(nodes, beams, '-', self.optim_ax_r, self.optim_fig, opt_area_per_rod)
        # print(u_ax_l.get_xticklabels())
        # u_ax_l.set_xticklabels(u_ax_l.get_xticklabels(), rotation=45)
        # u_ax_l.set_zticklabels(u_ax_l.get_zticklabels(), rotation=45)

    def update_diff_plot(self, base_nodes, base_opt_deformed_nodes, base_beams,
                         base_optm_axial_forces, current_nodes, current_opt_deformed_nodes,
                         current_beams, current_optm_axial_forces, base_end_crane_parts,
                         current_end_crane_parts, loads):
        # Comparison base
        if type(base_nodes) != type(None) or type(base_opt_deformed_nodes) != type(None) or type(base_beams) != type(None) or type(base_optm_axial_forces) != type(None): 
            #not isinstance(base_nodes, None) or not isinstance(base_opt_deformed_nodes, None) or not isinstance(base_beams, None) or not isinstance(base_optm_axial_forces, None)
            simple_plot(base_nodes, base_beams, "grey", "--", "Undeformed", self.diff_ax_l,
                        base_end_crane_parts[1], base_end_crane_parts[2], loads[0], loads[1])
            plot_deformation_with_grad(base_opt_deformed_nodes, base_beams, '-', self.diff_ax_l,
                                       base_optm_axial_forces, self.cmap_deformation)
        # Current
        # TODO here we could use reuse the current instead of plotting it again saves time
        simple_plot(current_nodes, current_beams, "grey", "--", "Undeformed", self.diff_ax_r,
                    current_end_crane_parts[1], current_end_crane_parts[2], loads[0], loads[1])
        plot_deformation_with_grad(current_opt_deformed_nodes, current_beams, '-', self.diff_ax_r,
                                   current_optm_axial_forces, self.cmap_deformation)


def simple_plot(nodes, beams, color, line_style, label, axes, end_jib, end_cj, front_load, back_load):
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
            axes.quiver(x, y, z, 0, 0, -180, color='r', length=max(1, min(12.5, abs(front_load) / 20)))
        if i == end_cj - 1 or i == end_cj - 2:
            axes.quiver(x, y, z, 0, 0, -180, color='g', length=max(1, min(12.5, abs(back_load) / 20)))

    line.set_label(label)
    axes.legend(prop={'size': 10})


def plot_deformation_with_grad(deformed_nodes, beams, line_style, ax, axial_forces, cmap_type):
    """Plots crane with deformation of it and colors representing the axial forces of individual beams"""
    axial_forces = np.absolute(axial_forces)
    norm = mpl.colors.Normalize(min(axial_forces), max(axial_forces))
    cmap = cm.get_cmap(cmap_type.currentText())
    values_listed_in_legend = {}
    for i in range(len(beams)):
        # Deformed nodes
        dxi, dxf = deformed_nodes[beams[i, 0], 0], deformed_nodes[beams[i, 1], 0]
        dyi, dyf = deformed_nodes[beams[i, 0], 1], deformed_nodes[beams[i, 1], 1]
        dzi, dzf = deformed_nodes[beams[i, 0], 2], deformed_nodes[beams[i, 1], 2]

        line = ax.plot([dxi, dxf], [dyi, dyf], [dzi, dzf], color=cmap(norm(axial_forces[i])),
                       linestyle=line_style, linewidth=LINE_WIDTH)
        value = axial_forces[i].round(decimals=0)
        value_as_norm = norm(value)
        if not value_as_norm in values_listed_in_legend:
            values_listed_in_legend[value] = value_as_norm
        line = line[0]
    axial_forces_list = axial_forces
    axial_forces_list.sort()
    # ax.legend(handles=create_colormap_gradient(axial_forces_list, cmap, "Pa"), prop={'size': 10},
            #   loc='upper right', draggable=True, title='Axial forces per rod')

    line.set_label("Deformed")
    ax.set_aspect("equal")
    # ax.legend(handles=create_colormap_gradient(axial_forces, cmap), prop={'size': 0}, loc='upper left',
    #            title='Absolute axial forces')


def plot_area_with_grad(nodes, beams, line_style, ax, fig, area_per_rod):
    """Plots crane with colors representing the cross section area of individual beams"""
    norm = mpl.colors.Normalize(min(area_per_rod), max(area_per_rod))
    cmap = cm.get_cmap("rainbow")
    values_listed_in_legend = {}
    for i in range(len(beams)):
        # Undeformed nodes
        xi, xf = nodes[beams[i, 0], 0], nodes[beams[i, 1], 0]
        yi, yf = nodes[beams[i, 0], 1], nodes[beams[i, 1], 1]
        zi, zf = nodes[beams[i, 0], 2], nodes[beams[i, 1], 2]

        line = ax.plot([xi, xf], [yi, yf], [zi, zf], color=cmap(norm(area_per_rod[i])), linestyle=line_style,
                       linewidth=LINE_WIDTH)
        value_as_norm = norm(area_per_rod[i])
        if not value_as_norm in values_listed_in_legend.values():
            values_listed_in_legend[area_per_rod[i]] = value_as_norm
        line = line[0]
    ax.legend(handles=create_colormap_gradient_area_per_rod(values_listed_in_legend, cmap, "m\u00B2"),
              prop={'size': 10},
              loc='upper right', draggable=True, title='Cross sectional area per rod')
    fig.gca().set_aspect('equal')


def create_colormap_gradient(list, cmap, suffix):
    """Generates a gradient of a colormap"""
    cmap_legend = []
    idx = np.round(np.linspace(0, len(list) - 1, 6)).astype(int)
    for i in idx:
        value = list[i]
        a = norm(value)
        cmap_legend.append(mpl.lines.Line2D([0], [0], color=cmap(norm(value)), label=f'{value.round(decimals=1)} {suffix}'))
    return cmap_legend


def create_colormap_gradient_area_per_rod(dictionary, cmap, suffix):
    """Generates a gradient of a colormap specifically for the cross section area"""
    cmap_legend = []
    for value in dictionary:
        value_as_norm = dictionary[value]
        cmap_legend.append(mpl.lines.Line2D([0], [0], color=cmap(value_as_norm), label=f'{value} {suffix}'))
    return cmap_legend


def display():
    """Displays generated plot"""
    plt.axis("equal")
    plt.show()
