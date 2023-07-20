"""
Provides all functions to plot the crane and to display the plot
"""
import matplotlib as mpl
import matplotlib.cm as cm
import numpy as np
from matplotlib import pyplot as plt

LINE_WIDTH = 1


def set_default_settings(ax, title):
    """Sets default values for plots"""
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
    """Handles all plotting in the GUI"""
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

    def update_unoptimized_plots(self, nodes, deformed_nodes, beams,
                                 area_per_beam, axial_forces, end_crane_parts, loads):
        """Plots unoptimized crane"""
        simple_plot(nodes, beams, "grey", "--", "Undeformed", self.unoptim_ax_l,
                    end_crane_parts[1], end_crane_parts[2], loads[0], loads[1])
        plot_deformation_with_grad(deformed_nodes, beams, '-', self.unoptim_ax_l,
                                   axial_forces, self.cmap_deformation)
        plot_area_with_grad(nodes, beams, '-', self.unoptim_ax_r,
                            self.unoptim_fig, area_per_beam, 1)

    def update_optimized_plots(self, nodes, opt_deformed_nodes, beams, opt_area_per_beam,
                               optm_axial_forces, end_crane_parts, loads):
        """Plot optimized crane"""
        simple_plot(nodes, beams, "grey", "--", "Undeformed", self.optim_ax_l,
                    end_crane_parts[1], end_crane_parts[2], loads[0], loads[1])
        plot_deformation_with_grad(opt_deformed_nodes, beams, '-', self.optim_ax_l,
                                   optm_axial_forces, self.cmap_deformation)
        plot_area_with_grad(nodes, beams, '-', self.optim_ax_r,
                            self.optim_fig, opt_area_per_beam, 6)

    def update_diff_plot(self, base_nodes, base_opt_deformed_nodes, base_beams,
                         base_optm_axial_forces, current_nodes, current_opt_deformed_nodes,
                         current_beams, current_optm_axial_forces, base_end_crane_parts,
                         current_end_crane_parts, loads):
        """Updates the plots showing the base version and the new version to enable comparison"""
        # Comparison base
        if type(base_nodes) != type(None) or type(base_opt_deformed_nodes) != type(None) or type(base_beams) != type(None) or type(base_optm_axial_forces) != type(None): 
            simple_plot(base_nodes, base_beams, "grey", "--", "Undeformed", self.diff_ax_l,
                        base_end_crane_parts[1], base_end_crane_parts[2], loads[0], loads[1])
            plot_deformation_with_grad(base_opt_deformed_nodes, base_beams, '-', self.diff_ax_l,
                                       base_optm_axial_forces, self.cmap_deformation)
        # Current
        # TODO here we could reuse the current instead of plotting it again saves time
        simple_plot(current_nodes, current_beams, "grey", "--", "Undeformed", self.diff_ax_r,
                    current_end_crane_parts[1], current_end_crane_parts[2], loads[0], loads[1])
        plot_deformation_with_grad(current_opt_deformed_nodes, current_beams, '-', self.diff_ax_r,
                                   current_optm_axial_forces, self.cmap_deformation)


def simple_plot(nodes, beams, color, line_style, label,
                axes, end_jib, end_cj, front_load, back_load):
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
        line = axes.plot([xi, xf], [yi, yf], [zi, zf], color=color,
                         linestyle=line_style, linewidth=LINE_WIDTH)
        # Override list with first element in list, always the Line3D object.
        line = line[0]

    for i in range(len(nodes)):
        x = nodes[i, 0]
        y = nodes[i, 1]
        z = nodes[i, 2]
        if i == end_jib - 1 or i == end_jib - 2:
            axes.quiver(x, y, z, 0, 0, -180, color='r',
                        length=max(1, min(12.5, abs(front_load) / 20)))
        if i == end_cj - 1 or i == end_cj - 2:
            axes.quiver(x, y, z, 0, 0, -180, color='g',
                        length=max(1, min(12.5, abs(back_load) / 20)))

    line.set_label(label)
    axes.legend(prop={'size': 10})


def plot_deformation_with_grad(deformed_nodes, beams, line_style, ax, axial_forces, cmap_type):
    """Plots crane with deformation of it and colors
    representing the axial forces of individual beams"""
    axial_forces = np.absolute(axial_forces)
    norm_vals = mpl.colors.Normalize(min(axial_forces), max(axial_forces))
    cmap = cm.get_cmap(cmap_type.currentText())
    values_listed_in_legend = {}
    for i in range(len(beams)):
        # Get deformed node coords
        dxi, dxf = deformed_nodes[beams[i, 0], 0], deformed_nodes[beams[i, 1], 0]
        dyi, dyf = deformed_nodes[beams[i, 0], 1], deformed_nodes[beams[i, 1], 1]
        dzi, dzf = deformed_nodes[beams[i, 0], 2], deformed_nodes[beams[i, 1], 2]
        # Plot beams
        line = ax.plot([dxi, dxf], [dyi, dyf], [dzi, dzf], color=cmap(norm_vals(axial_forces[i])),
                       linestyle=line_style, linewidth=LINE_WIDTH)
        value = axial_forces[i].round(decimals=0)
        value_as_norm = norm_vals(value)
        if value_as_norm not in values_listed_in_legend:
            values_listed_in_legend[value] = value_as_norm
        line = line[0]
    axial_forces_list = axial_forces
    axial_forces_list.sort()
    ax.legend(handles=create_colormap_gradient(axial_forces_list, cmap), prop={'size': 10},
              loc='lower right', draggable=True, title='Axial forces per beam')

    line.set_label("Deformed")
    ax.set_aspect("equal")


def plot_area_with_grad(nodes, beams, line_style, ax, fig, area_per_beam, vals_to_disp):
    """Plots crane with colors representing the cross section area of individual beams"""
    norm_vals = mpl.colors.Normalize(min(area_per_beam), max(area_per_beam))
    cmap = cm.get_cmap("rainbow")
    values_listed_in_legend = {}
    for i in range(len(beams)):
        # Get undeformed node coords
        xi, xf = nodes[beams[i, 0], 0], nodes[beams[i, 1], 0]
        yi, yf = nodes[beams[i, 0], 1], nodes[beams[i, 1], 1]
        zi, zf = nodes[beams[i, 0], 2], nodes[beams[i, 1], 2]
        # Plot beams
        line = ax.plot([xi, xf], [yi, yf], [zi, zf], color=cmap(norm_vals(area_per_beam[i])),
                       linestyle=line_style, linewidth=LINE_WIDTH)
        value_as_norm = norm_vals(area_per_beam[i])
        if value_as_norm not in values_listed_in_legend.values():
            values_listed_in_legend[area_per_beam[i]] = value_as_norm
        line = line[0]
    values_listed_in_legend_list = list(values_listed_in_legend.keys())
    values_listed_in_legend_list.sort()
    vals_to_disp = min(vals_to_disp, len(values_listed_in_legend_list))
    cmap_grad = create_colormap_gradient_area_per_beam(values_listed_in_legend_list,
                                                       cmap, "m\u00B2", vals_to_disp)
    ax.legend(handles=cmap_grad, prop={'size': 10}, loc='lower right',
              draggable=True, title='Cross sectional area per beam')
    fig.gca().set_aspect('equal')


def create_colormap_gradient(sorted_axial_forces, cmap):
    """Generates a gradient of a colormap"""
    cmap_legend = []
    select_axial_forces = np.round(np.linspace(0, len(sorted_axial_forces) - 1, 6)).astype(int)
    for i, axial_force in enumerate(select_axial_forces):
        label_txt = num_with_units(sorted_axial_forces[axial_force].round(decimals=1))
        cmap_legend.append(mpl.lines.Line2D([0], [0], color=cmap(0.2 * i),
                                            lw=4, label=label_txt))
    return cmap_legend


def num_with_units(num, suffix="Pa"):
    """
    Adjusts axial force and applies correct prefix to unit\n
    https://stackoverflow.com/questions/1094841/get-human-readable-version-of-file-size
    """
    for unit in ("", "k", "M", "G"):
        if abs(num) < 1000.0:
            return f"{num:3.1f} {unit}{suffix}"
        num /= 1000.0
    return f"{num:.1f}Y{suffix}"


def create_colormap_gradient_area_per_beam(areas_per_beam, cmap, suffix, vals_to_disp):
    """Generates a gradient of a colormap specifically for the cross section area"""
    cmap_legend = []
    select_areas = np.round(np.linspace(0, len(areas_per_beam) - 1, 6)).astype(int)
    for i in range(vals_to_disp):
        label_txt = f'{areas_per_beam[select_areas[i]].round(decimals=4)} {suffix}'
        cmap_legend.append(mpl.lines.Line2D([0], [0], color=cmap(0.2 * i), lw=4, label=label_txt))
    return cmap_legend


def display():
    """Displays generated plot"""
    plt.axis("equal")
    plt.show()
