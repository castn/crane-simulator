import sys

import numpy as np
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox, QTreeWidgetItem, QFileDialog

from craneSimulator.gui.plotting.plotter import PlotterManager
from craneSimulator.gui.windows.Ui_MainWindow import Ui_MainWindow
from craneSimulator.simulation import analysis
from craneSimulator.truss.crane import Crane
from craneSimulator.util import file_handler
from craneSimulator.util.file_handler import FileHandler
from craneSimulator.util.string_handler import string_to_boolean

sys.path.append('./')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from craneSimulator.truss import crane
from craneSimulator.truss.dimensions import Dims


class matplotlib_canvas(FigureCanvasQTAgg):
    """Creates plot"""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(matplotlib_canvas, self).__init__(self.fig)


def create_tree_item(arr, name, unit):
    """Creates tree for 'Debug' tab"""
    tree_item = QTreeWidgetItem([name])
    for ind, comp in enumerate(arr):
        child = QTreeWidgetItem([f"{ind}. {comp} {unit}"])
        tree_item.addChild(child)
    return tree_item


def update_debug_treeWidget(widget, nodes, deformed_nodes, beams, area_per_rod):
    widget.clear()
    optim_tree_items = [create_tree_item(nodes, "XYZ-Coordinates of undeformed Nodes", ""),
                        create_tree_item(deformed_nodes, "XYZ-Coordinates of deformed Nodes", ""),
                        create_tree_item(beams, "Beams (start and end nodes)", ""),
                        create_tree_item(area_per_rod, "Cross sectional area per Rod", "m\u00B2")]
    widget.insertTopLevelItems(0, optim_tree_items)
    return widget


class MainWindow(QtWidgets.QMainWindow):
    """Main UI window"""

    def __init__(self):
        """Initializes main window"""
        super(MainWindow, self).__init__()
        self.base_end_crane_parts = None
        self.end_crane_parts = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Call the autogenerated Ui_MainWindow.py, generated from the .ui file using the command "pyuic6 mainwindow.ui -o MainWindow.py"

        # Perform initial setups of window
        self.base_optim_axial_forces = None
        self.base_optim_area_per_rod = None
        self.base_beams = None
        self.base_optim_deformed_nodes = None
        self.base_nodes = None
        self.nodes = None
        self.beams = None
        self.optim_deformed_nodes = None
        self.deformed_nodes = None
        self.area_per_rod = None
        self.deformation = None
        self.reaction_forces = None
        self.axial_forces = None
        self.optim_area_per_rod = None
        self.optim_deformations = None
        self.optim_reaction_forces = None
        self.optim_axial_forces = None
        self.unoptim_canvas = None  # matplotlib_canvas(self, width=5, height=4, dpi=100)
        self.unoptim_toolbar = None
        self.optim_canvas = None  # matplotlib_canvas(self, width=5, height=4, dpi=100)
        self.optim_toolbar = None
        self.diff_canvas = None  # matplotlib_canvas(self, width=5, height=4, dpi=100)
        self.diff_toolbar = None
        self.setWindowTitle("Crane Simulator 2024")
        # Set menu bar actions
        self.create_actions()
        # Set tree widgets
        self.ui.fem_unoptimized_treeWidget.setColumnCount(1)
        self.ui.fem_unoptimized_treeWidget.setHeaderLabel("FEM values for unoptimized crane")
        self.ui.fem_optimized_treeWidget.setColumnCount(1)
        self.ui.fem_optimized_treeWidget.setHeaderLabel("FEM values for optimized crane")
        self.ui.debug_unoptimized_treeWidget.setColumnCount(1)
        self.ui.debug_unoptimized_treeWidget.setHeaderLabel("Debug values for unoptimized crane")
        self.ui.debug_optimized_treeWidget.setColumnCount(1)
        self.ui.debug_optimized_treeWidget.setHeaderLabel("Debug values for optimized crane")
        self.ui.comparison_base_treeWidget.setColumnCount(1)
        self.ui.comparison_base_treeWidget.setHeaderLabel("Comparison base (old)")
        self.ui.current_treeWidget.setColumnCount(1)
        self.ui.current_treeWidget.setHeaderLabel("Current crane (new)")

        # Set default size of plotBox, otherwise will shrink to minimal and needs manual adjustment
        self.ui.plotBox.setGeometry(0, 0, 716, 544)
        # Create matplot canvas and associated toolbar
        # Add canvas and toolbar to dedicated widget in this window

        self.fileHandler = FileHandler()
        self.is_saved = False
        self.is_analysed = False
        self.is_optimized = False
        self.crane = Crane()
        self.comparison_base = None
        self.dims = Dims()
        self.set_crane_dimensions()

        # Perform action on press of apply button
        self.ui.apply_button.clicked.connect(self.apply_configuration)
        self.ui.current_as_comparison_base.clicked.connect(self.create_comparison)

    def create_actions(self):
        self.ui.actionOpen.triggered.connect(self.open)
        self.ui.actionSave.triggered.connect(self.save)
        self.ui.actionExit.triggered.connect(self.on_exit)
        self.ui.actionReport_bug.triggered.connect(self.report_bug)
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionAbout_Qt.triggered.connect(QtWidgets.QApplication.aboutQt)

    def open(self):
        file_name, types_of_files = QFileDialog.getOpenFileName(self)
        if file_name != "":
            self.fileHandler.load_file(file_name)
            if self.fileHandler.config == type(None):
                QMessageBox.critical(self, "Error", "Could not load config. Possible error while reading the file")
            else:
                self.dictionary_to_config(self.fileHandler.config)
                QMessageBox.information(self, "Import successful", f"Successfully imported {file_name}.\n\nClick the "
                                                                   f"Apply button to render the changes!")

    def dictionary_to_config(self, config):
        tower = config.get("tower")
        self.ui.towerHeight_spinbox.setValue(int(tower.get("height")))
        self.ui.towerWidth_spinbox.setValue(int(tower.get("width")))
        self.ui.towerSegment_spinbox.setValue(int(tower.get("segments")))
        self.ui.towerSupportType_comboBox.setCurrentText(tower.get("type"))
        jib = config.get("jib")
        self.ui.jibLength_spinBox.setValue(int(jib.get("length")))
        self.ui.jibHeight_spinBox.setValue(int(jib.get("height")))
        self.ui.jibSegment_spinBox.setValue(int(jib.get("segments")))
        self.ui.jibSupportType_comboBox.setCurrentText(jib.get("type"))
        counterjib = config.get("counterjib")
        self.ui.counterJibLength_spinBox.setValue(int(counterjib.get("length")))
        self.ui.counterJibHeight_spinBox.setValue(int(counterjib.get("height")))
        self.ui.counterJibSegments_spinBox.setValue(int(counterjib.get("segments")))
        self.ui.counterJibSupportType_comboBox.setCurrentText(counterjib.get("type"))
        fem = config.get("fem")
        self.ui.jib_left_spinBox.setValue(int(fem.get("jibLeft")))
        self.ui.jib_right_spinBox.setValue(int(fem.get("jibRight")))
        self.ui.counterjib_left_spinBox.setValue(int(fem.get("counterJibLeft")))
        self.ui.counterjib_right_spinBox.setValue(int(fem.get("counterJibRight")))
        self.ui.multiplierSpinBox.setValue(int(fem.get("scale")))
        wind = config.get("wind")
        self.ui.wind_settings.setChecked(string_to_boolean(wind.get("enabled")))
        self.ui.wind_direction.setCurrentText(wind.get("direction"))
        self.ui.wind_force.setValue(int(wind.get("force")))
        gravity = config.get("gravity")
        self.ui.enable_gravity.setChecked(string_to_boolean(gravity.get("enabled")))
        ignorespec = config.get("ignorespec")
        self.ui.ignore_specification.setChecked(string_to_boolean(ignorespec.get("enabled")))

    def on_exit(self):
        if self.is_saved:
            sys.exit()
        if self.save():
            sys.exit()

    def save(self):
        file_name, types_of_files = QFileDialog.getSaveFileName(self)
        if file_name == "":
            return False
        else:
            return file_handler.save_file(file_name, self.config_to_dictionary())

    def config_to_dictionary(self):
        dictionary = dict()
        tower = dict()
        tower["height"] = self.ui.towerHeight_spinbox.value()
        tower["width"] = self.ui.towerWidth_spinbox.value()
        tower["segments"] = self.ui.towerSegment_spinbox.value()
        tower["type"] = self.ui.towerSupportType_comboBox.currentText()
        dictionary["tower"] = tower
        jib = dict()
        jib["length"] = self.ui.jibLength_spinBox.value()
        jib["height"] = self.ui.jibHeight_spinBox.value()
        jib["segments"] = self.ui.jibSegment_spinBox.value()
        jib["type"] = self.ui.jibSupportType_comboBox.currentText()
        dictionary["jib"] = jib
        counterjib = dict()
        counterjib["length"] = self.ui.counterJibLength_spinBox.value()
        counterjib["height"] = self.ui.counterJibHeight_spinBox.value()
        counterjib["segments"] = self.ui.counterJibSegments_spinBox.value()
        counterjib["type"] = self.ui.counterJibSupportType_comboBox.currentText()
        dictionary["counterjib"] = counterjib
        fem = dict()
        fem["jibLeft"] = self.ui.jib_left_spinBox.value()
        fem["jibRight"] = self.ui.jib_right_spinBox.value()
        fem["counterJibLeft"] = self.ui.counterjib_left_spinBox.value()
        fem["counterJibRight"] = self.ui.counterjib_right_spinBox.value()
        fem["scale"] = self.ui.multiplierSpinBox.value()
        dictionary["fem"] = fem
        wind = dict()
        wind["enabled"] = self.ui.wind_settings.isChecked()
        wind["direction"] = self.ui.wind_direction.currentText()
        wind["force"] = self.ui.wind_force.value()
        dictionary["wind"] = wind
        gravity = dict()
        gravity["enabled"] = self.ui.enable_gravity.isChecked()
        dictionary["gravity"] = gravity
        ignorespec = dict()
        ignorespec["enabled"] = self.ui.ignore_specification.isChecked()
        dictionary["ignorespec"] = ignorespec
        self.is_saved = True
        return dictionary

    def report_bug(self):
        # aboutBox = QMessageBox(self)
        # aboutBox.setText("The document has been modified.")
        # aboutBox.icon("../../resources/debug.svg")
        # aboutBox.exec()
        QMessageBox.about(self, "Bug Report",
                          "You found a bug and want to report it? Great, please open an issue on "
                          "<a href='https://github.com/'>Github</a> where you decribe the bug in as much details as possible. "
                          "If you can please add screenshots or anything else. That can help us to fix it as soon as possible")

    def about(self):
        QMessageBox.about(self, "About Crane Simulator 2024",
                          "<b>Crane Simulator 2024</b><br> is a software written in Python which was developed in the "
                          "context of a project course at the TU Darmstadt. The source code is available on Github.")

    def set_values_debug_treeWidgets(self):
        """Updates node and beam tree in 'Debug' tab"""
        self.ui.debug_unoptimized_treeWidget.clear()
        optim_tree_items = [create_tree_item(self.nodes, "XYZ-Coordinates of undeformed Nodes", ""),
                            create_tree_item(self.deformed_nodes, "XYZ-Coordinates of deformed Nodes", ""),
                            create_tree_item(self.beams, "Beams (start and end nodes)", ""),
                            create_tree_item(self.area_per_rod, "Cross sectional area per Rod", "m\u00B2")]
        self.ui.debug_unoptimized_treeWidget.insertTopLevelItems(0, optim_tree_items)

        self.ui.debug_optimized_treeWidget.clear()
        optim_tree_items = [create_tree_item(self.nodes, "XYZ-Coordinates of undeformed Nodes", ""),
                            create_tree_item(self.optim_deformed_nodes, "XYZ-Coordinates of deformed Nodes", ""),
                            create_tree_item(self.beams, "Beams (start and end nodes)", ""),
                            create_tree_item(self.optim_area_per_rod, "Cross sectional area per Rod", "m\u00B2")]
        self.ui.debug_optimized_treeWidget.insertTopLevelItems(0, optim_tree_items)

    def update_fem_treeWidget(self):
        """Updates node and beam tree in 'Debug' tab"""
        self.ui.fem_unoptimized_treeWidget.clear()
        self.ui.fem_optimized_treeWidget.clear()
        unoptim_tree_items = [
            create_tree_item(self.axial_forces.round(decimals=2),
                             "Axial Forces (positive = tension, negative = compression)", "N"),
            create_tree_item(self.reaction_forces.round(decimals=2),
                             "Reaction Forces (positive = upward, negative = downward)", "N"),
            create_tree_item(self.deformation.round(decimals=2), "Deformation at nodes", "mm")]
        optim_tree_items = [
            create_tree_item(self.optim_axial_forces.round(decimals=2),
                             "Axial Forces (positive = tension, negative = compression)", "N"),
            create_tree_item(self.optim_reaction_forces.round(decimals=2),
                             "Reaction Forces (positive = upward, negative = downward)", "N"),
            create_tree_item(self.optim_deformations.round(decimals=2), "Deformation at nodes", "mm")]
        self.ui.fem_unoptimized_treeWidget.insertTopLevelItems(0, unoptim_tree_items)
        self.ui.fem_optimized_treeWidget.insertTopLevelItems(0, optim_tree_items)

    def update_diff_treeWidget(self):
        self.ui.comparison_base_treeWidget.clear()
        self.ui.current_treeWidget.clear()

        current_tree_items = [create_tree_item(self.nodes, "XYZ-Coordinates of undeformed Nodes", ""),
                              create_tree_item(self.optim_deformed_nodes, "XYZ-Coordinates of deformed Nodes", ""),
                              create_tree_item(self.beams, "Beams (start and end nodes)", ""),
                              create_tree_item(self.optim_area_per_rod, "Cross sectional area per Rod", "m\u00B2")]
        self.ui.current_treeWidget.insertTopLevelItems(0, current_tree_items)

        # Check if comparison base exists
        if type(self.comparison_base) != type(None):  # Might need to check all types in list below
            comparison_base_tree_items = [create_tree_item(self.base_nodes, "XYZ-Coordinates of undeformed Nodes", ""),
                                          create_tree_item(self.base_optim_deformed_nodes,
                                                           "XYZ-Coordinates of deformed Nodes",
                                                           ""),
                                          create_tree_item(self.base_beams, "Beams (start and end nodes)", ""),
                                          create_tree_item(self.base_optim_area_per_rod, "Cross sectional area per Rod",
                                                           "m\u00B2")]
            self.ui.comparison_base_treeWidget.insertTopLevelItems(0, comparison_base_tree_items)

    def set_crane_dimensions(self):
        """Sets dimensions from what is currently in the input fields"""
        # Reset all old dimensions
        self.dims.clear_all()
        # Set all tower dimensions
        self.dims.set_tower_height(self.ui.towerHeight_spinbox.value())
        self.dims.set_tower_width(self.ui.towerWidth_spinbox.value())
        self.dims.set_tower_segments(self.ui.towerSegment_spinbox.value())
        self.dims.set_tower_support_type(self.ui.towerSupportType_comboBox.currentText())
        # Set all jib dimensions
        self.dims.set_jib_height(self.ui.jibHeight_spinBox.value())
        self.dims.set_jib_length(self.ui.jibLength_spinBox.value())
        self.dims.set_jib_segments(self.ui.jibSegment_spinBox.value())
        self.dims.set_jib_support_type(self.ui.jibSupportType_comboBox.currentText())
        # Set all counter jib dimensions
        self.dims.set_counter_jib_height(self.ui.counterJibHeight_spinBox.value())
        self.dims.set_counter_jib_length(self.ui.counterJibLength_spinBox.value())
        self.dims.set_counter_jib_segments(self.ui.counterJibSegments_spinBox.value())
        self.dims.set_counter_jib_support_type(self.ui.counterJibSupportType_comboBox.currentText())

    def update_plot(self):
        """Updates 3D plot"""
        # Reset plots by removing and readding them again to the gui
        self.reset_plots()

        # Create new plot manager to manage the different plots
        plotter_manager = PlotterManager(self.ui.axial_coloring.isChecked(), self.ui.cmap, self.ui.cmap,
                                         self.unoptim_canvas.fig, self.optim_canvas.fig, self.diff_canvas.fig)

        # Update plots for unoptimized tab
        plotter_manager.update_unoptimized_plots(self.nodes, self.deformed_nodes, self.beams, self.area_per_rod,
                                                 self.axial_forces, self.end_crane_parts,
                                                 [self.ui.jib_left_spinBox.value(), self.ui.counterjib_left_spinBox.value()])
        # Update plots for optimized tab
        plotter_manager.update_optimized_plots(self.nodes, self.optim_deformed_nodes, self.beams, self.optim_area_per_rod,
                                               self.optim_axial_forces, self.end_crane_parts,
                                               [self.ui.jib_left_spinBox.value(), self.ui.counterjib_left_spinBox.value()])

        plotter_manager.update_diff_plot(self.base_nodes, self.base_optim_deformed_nodes, self.base_beams,
                                         self.base_optim_axial_forces, self.nodes, self.optim_deformed_nodes,
                                         self.beams, self.optim_axial_forces, self.base_end_crane_parts,
                                         self.end_crane_parts, [self.ui.jib_left_spinBox.value(), self.ui.counterjib_left_spinBox.value()])

    def display_in_console(self):
        """Display displacement of crane at points where forces are applied"""
        self.ui.output.appendPlainText("[Unoptimized] Jib displacement")
        self.ui.output.appendPlainText(
            str(self.deformed_nodes[crane.Dims.JIB_NUM_NODES - 2].round(decimals=3) - self.nodes[crane.Dims.JIB_NUM_NODES - 2].round(decimals=3)) + ' mm')
        self.ui.output.appendPlainText(
            str(self.deformed_nodes[crane.Dims.JIB_NUM_NODES - 1].round(decimals=3) - self.nodes[crane.Dims.JIB_NUM_NODES - 1].round(decimals=3)) + ' mm')
        self.ui.output.appendPlainText("[Optimized] Jib displacement")
        self.ui.output.appendPlainText(
            str(self.optim_deformed_nodes[crane.Dims.JIB_NUM_NODES - 2].round(decimals=3) - self.nodes[crane.Dims.JIB_NUM_NODES - 2].round(decimals=3)) + ' mm')
        self.ui.output.appendPlainText(
            str(self.optim_deformed_nodes[crane.Dims.JIB_NUM_NODES - 1].round(decimals=3) - self.nodes[crane.Dims.JIB_NUM_NODES - 1].round(decimals=3)) + ' mm')
        self.ui.output.appendPlainText("[Unoptimized] Counter Jib displacement")
        self.ui.output.appendPlainText(
            str(self.deformed_nodes[len(self.deformed_nodes) - 2].round(decimals=3) - self.nodes[len(self.nodes) - 2].round(decimals=3)) + ' mm')
        self.ui.output.appendPlainText(
            str(self.deformed_nodes[len(self.deformed_nodes) - 1].round(decimals=3) - self.nodes[len(self.nodes) - 1].round(decimals=3)) + ' mm')
        self.ui.output.appendPlainText("[Optimized] Counter Jib displacement")
        self.ui.output.appendPlainText(
            str(self.optim_deformed_nodes[len(self.deformed_nodes) - 2].round(decimals=3) - self.nodes[len(self.nodes) - 2].round(decimals=3)) + ' mm')
        self.ui.output.appendPlainText(
            str(self.optim_deformed_nodes[len(self.deformed_nodes) - 1].round(decimals=3) - self.nodes[len(self.nodes) - 1].round(decimals=3)) + ' mm')
        self.ui.output.appendPlainText('\n')

    def reset_plots(self):
        self.remove_current_plots()
        self.add_new_plots()

    def add_new_plots(self):
        # Create new canvas and toolbar we will use for plotting
        new_unoptim_canvas = matplotlib_canvas(self, width=5, height=4, dpi=100)
        # Toolbar and canvas for unoptimized view
        self.unoptim_toolbar = NavigationToolbar(new_unoptim_canvas, self)
        self.unoptim_canvas = new_unoptim_canvas
        # Toolbar and canvas for optimized view
        new_optim_canvas = matplotlib_canvas(self, width=5, height=4, dpi=100)
        self.optim_toolbar = NavigationToolbar(new_optim_canvas, self)
        self.optim_canvas = new_optim_canvas
        # Toolbar and canvas for diff view
        new_diff_canvas = matplotlib_canvas(self, width=5, height=4, dpi=100)
        self.diff_toolbar = NavigationToolbar(new_diff_canvas, self)
        self.diff_canvas = new_diff_canvas

        # Make toolbars and canvases visible in gui by adding them as a widget
        self.ui.unoptimized_plot_layout.addWidget(self.unoptim_toolbar)
        self.ui.unoptimized_plot_layout.addWidget(self.unoptim_canvas)
        self.ui.optimize_plot_layout.addWidget(self.optim_toolbar)
        self.ui.optimize_plot_layout.addWidget(self.optim_canvas)
        self.ui.diff_plot_layout.addWidget(self.diff_toolbar)
        self.ui.diff_plot_layout.addWidget(self.diff_canvas)

    def remove_current_plots(self):
        # Hide NO DATA label because we will now display a plot
        if not self.ui.unoptimized_no_data_label.isHidden():
            self.ui.unoptimized_no_data_label.hide()
        if not self.ui.optimized_no_data_label.isHidden():
            self.ui.optimized_no_data_label.hide()
        if not self.ui.diff_no_data_label.isHidden():
            self.ui.diff_no_data_label.hide()

        # TODO here are some code duplications guess this can be done more elegant, but currently most trivial fix
        # Remove toolbars and canvas of matplotlib view
        # Unoptimized tab
        self.remove_plot_from_unoptimized(self.unoptim_toolbar)
        self.remove_plot_from_unoptimized(self.unoptim_canvas)
        # Optimized tab
        self.remove_plot_from_optimized(self.optim_toolbar)
        self.remove_plot_from_optimized(self.optim_canvas)
        # Diff tab
        self.remove_plot_from_diff(self.diff_toolbar)
        self.remove_plot_from_diff(self.diff_canvas)

    def remove_plot_from_unoptimized(self, widget):
        if not type(widget) == type(None):
            self.ui.unoptimized_plot_layout.removeWidget(widget)

    def remove_plot_from_optimized(self, widget):
        if not type(widget) == type(None):
            self.ui.optimize_plot_layout.removeWidget(widget)

    def remove_plot_from_diff(self, widget):
        if not type(widget) == type(None):
            self.ui.diff_plot_layout.removeWidget(widget)

    def apply_configuration(self):
        """Updates crane configuration"""
        self.is_saved = False
        self.ui.progressBar.reset()
        self.ui.progressBar.setValue(0)

        self.set_crane_dimensions()
        # Will always generate a tower
        crane.set_tower_dims(self.dims.get_tower_height(),
                             self.dims.get_tower_width(),
                             self.dims.get_tower_segments(),
                             self.dims.get_tower_support_type())
        # Will always generate a jib
        crane.set_jib_dims(self.dims.get_jib_length(),
                           self.dims.get_jib_height(),
                           self.dims.get_jib_segments(),
                           self.dims.get_jib_support_type())
        # Will always generate a counter jib
        crane.set_counterjib_dims(self.dims.get_counter_jib_length(),
                                  self.dims.get_counter_jib_height(),
                                  self.dims.get_counter_jib_segments(),
                                  self.dims.get_counter_jib_support_type())

        self.crane.build_crane()

        if self.check_config():
            if not self.ui.enable_gravity.isChecked() or not self.ui.wind_settings.isChecked():
                self.crane.reset_forces(self.ui)

            if self.ui.enable_gravity.isChecked():
                self.crane.enable_gravity(self.ui)

            if self.ui.wind_settings.isChecked():
                self.crane.enable_wind(self.ui.wind_direction.currentText(), self.ui.wind_force.value())

            # Get undeformed crane with updated values
            self.nodes, self.beams = crane.get_crane()
            self.do_simulation()
            self.update_info()
            self.set_values_debug_treeWidgets()
            self.update_fem_treeWidget()
            self.update_diff_treeWidget()
            self.display_in_console()
            self.end_crane_parts = crane.get_end_parts()
            
            # plot as last so all values are set before plots so user only can see delay in plot update
            self.update_plot()

        self.is_analysed = True
        self.ui.progressBar.setValue(100)

    def do_simulation(self):
        # Get value set in multiplier
        multiplier = self.ui.multiplierSpinBox.value()
        # Do the analysis for unoptimized crane
        self.axial_forces, self.reaction_forces, self.deformation, self.area_per_rod = self.crane.analyze()
        self.deformed_nodes = self.deformation * multiplier + self.nodes
        # Now do the optimisation
        self.optim_axial_forces, self.optim_reaction_forces, self.optim_deformations, self.optim_area_per_rod = self.crane.optimize()
        self.optim_deformed_nodes = self.optim_deformations * multiplier + self.nodes

    def update_info(self):
        """Updates infobox in the bottom left"""
        total_length = crane.get_length()
        total_length = total_length / 1000
        total_volume = np.sum(self.optim_area_per_rod * (analysis.get_length_of_each_beam() / 1000))
        total_mass = total_volume * self.crane.DENSITY
        total_cost = total_mass / 1000 * 1000
        self.ui.total_length.setText(f'{(total_length):.3f} m')
        self.ui.total_volume.setText(f'{(total_volume):.3f} m\u00B3')
        self.ui.total_mass.setText(f'{(total_mass):.3f} kg')
        self.ui.total_cost.setText(f'{(total_cost):.2f} \u20AC')

    def check_config(self):
        """Checks if all beams are within the required range"""
        if not self.ui.ignore_specification.isChecked():
            tower_longest = crane.tower.get_longest_beam()
            if tower_longest < 500 or tower_longest > 2000:
                self.display_waring("Tower", tower_longest)
                return False
            jib_longest = crane.jib.get_longest_beam()
            if jib_longest < 500 or jib_longest > 2000:
                self.display_waring("Jib", jib_longest)
                return False
            counterjib_longest = crane.counterjib.get_longest_beam()
            if counterjib_longest < 500 or counterjib_longest > 2000:
                self.display_waring("Counter Jib", counterjib_longest)
                return False
        return True

    def create_comparison(self):
        if not self.crane.is_build:
            QMessageBox.critical(self, "No available data",
                                 "No data is available to create a comparison base from the current crane. "
                                 "You need to first apply all the settings to perform this action!")
        else:
            self.comparison_base = self.crane
            self.base_nodes = self.nodes
            self.base_optim_deformed_nodes = self.optim_deformed_nodes
            self.base_beams = self.beams
            self.base_optim_area_per_rod = self.optim_area_per_rod
            self.base_optim_axial_forces = self.optim_axial_forces
            self.base_end_crane_parts = self.end_crane_parts
            QMessageBox.information(self, "Success",
                                    "Successfully created a base version of your current crane. Click apply again to display them")

    def display_waring(self, type, longest_beam):
        QMessageBox.critical(self, 'Specification Violation',
                             f'Input parameters of <b>{type}</b> produce a value that violates the requirements.<br>'
                             f'Longest beam in your {type} has a length of {longest_beam:.4f}mm, but it must be in '
                             f'range of 500-2000mm. Change your parameters to fix this issue.<br><br>'
                             f'Allow specification violations? Check box "<i>Ignore specifications of project task</i>" in settings section')


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QtWidgets.QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()

# Will not be reached until application is closed
