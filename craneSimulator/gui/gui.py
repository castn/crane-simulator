import sys

import PySide6.QtWidgets

from craneSimulator.truss.crane import Crane
from craneSimulator.util import file_handler
from craneSimulator.util.file_handler import FileHandler
from craneSimulator.util.string_handler import string_to_boolean

sys.path.append('./')

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMessageBox, QTreeWidgetItem, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from craneSimulator.gui.plotting import plotter
from craneSimulator.gui.windows.MainWindow import Ui_MainWindow
from craneSimulator.truss import crane
from craneSimulator.truss.dimensions import Dims


class matplotlib_canvas(FigureCanvasQTAgg):
    """Creates plot"""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111, projection='3d')
        super(matplotlib_canvas, self).__init__(self.fig)


def create_tree_item(arr, name):
    """Creates tree for 'Debug' tab"""
    tree_item = QTreeWidgetItem([name])
    for ind, comp in enumerate(arr):
        child = QTreeWidgetItem([f"{ind}. {comp}"])
        tree_item.addChild(child)
    return tree_item


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """Main UI window"""

    def __init__(self):
        """Initializes main window"""
        super(MainWindow, self).__init__()
        # Call the autogenerated Ui_MainWindow.py, generated from the .ui file using the command "pyuic6 mainwindow.ui -o MainWindow.py"

        # Perform initial setups of window
        self.setupUi(self)
        self.setWindowTitle("Crane Simulator 2024")
        # Set menu bar actions
        self.create_actions()
        # Set tree widgets
        self.debug_treeWidget.setColumnCount(1)
        self.debug_treeWidget.setHeaderLabel("View Points of Nodes/Beams")
        self.fem_treeWidget.setColumnCount(1)
        self.fem_treeWidget.setHeaderLabel("FEM stuff")
        # Set default size of plotBox, otherwise will shrink to minimal and needs manual adjustment
        self.plotBox.setGeometry(0, 0, 716, 544)
        # Create matplot canvas and associated toolbar
        self.canvas = None #matplotlib_canvas(self, width=5, height=4, dpi=100)
        self.toolbar = None
        # Add canvas and toolbar to dedicated widget in this window

        self.fileHandler = FileHandler()
        self.is_saved = False
        self.crane = Crane()
        self.dims = Dims()
        self.set_dims()
        self.apply_configuration()

        # Perform action on press of apply button
        self.apply_button.clicked.connect(self.apply_configuration)

    def create_actions(self):
        self.actionOpen.triggered.connect(self.open)
        self.actionSave.triggered.connect(self.save)
        self.actionExit.triggered.connect(self.on_exit)
        self.actionReport_bug.triggered.connect(self.report_bug)
        self.actionAbout.triggered.connect(self.about)
        self.actionAbout_Qt.triggered.connect(PySide6.QtWidgets.QApplication.aboutQt)

    def open(self):
        file_name, types_of_files = QFileDialog.getOpenFileName(self)
        if file_name != "":
            self.fileHandler.load_file(file_name)
            if self.fileHandler.config == type(None):
                QMessageBox.critical(self, "Error", "Could not load config. Possible error while reading the file")
            else:
                self.dictionary_to_config(self.fileHandler.config)

    def dictionary_to_config(self, config):
        tower = config.get("tower")
        self.towerHeight_spinbox.setValue(int(tower.get("height")))
        self.towerWidth_spinbox.setValue(int(tower.get("width")))
        self.towerSegment_spinbox.setValue(int(tower.get("segments")))
        self.towerSupportType_comboBox.setCurrentText(tower.get("type"))
        jib = config.get("jib")
        self.jibLength_spinBox.setValue(int(jib.get("length")))
        self.jibHeight_spinBox.setValue(int(jib.get("height")))
        self.jibSegment_spinBox.setValue(int(jib.get("segments")))
        self.jibSupportType_comboBox.setCurrentText(jib.get("type"))
        counterjib = config.get("counterjib")
        self.counterJibLength_spinBox.setValue(int(counterjib.get("length")))
        self.counterJibHeight_spinBox.setValue(int(counterjib.get("height")))
        self.counterJibSegments_spinBox.setValue(int(counterjib.get("segments")))
        self.counterJibSupportType_comboBox.setCurrentText(counterjib.get("type"))
        fem = config.get("fem")
        self.jib_left_spinBox.setValue(int(fem.get("jibLeft")))
        self.jib_right_spinBox.setValue(int(fem.get("jibRight")))
        self.counterjib_left_spinBox.setValue(int(fem.get("counterJibLeft")))
        self.counterjib_right_spinBox.setValue(int(fem.get("counterJibRight")))
        self.multiplierSpinBox.setValue(int(fem.get("scale")))
        wind = config.get("wind")
        self.wind_settings.setChecked(string_to_boolean(wind.get("enabled")))
        self.wind_direction.setCurrentText(wind.get("direction"))
        self.wind_force.setValue(int(wind.get("force")))
        gravity = config.get("gravity")
        self.enable_gravity.setChecked(string_to_boolean(gravity.get("enabled")))
        ignorespec = config.get("ignorespec")
        self.ignore_specification.setChecked(string_to_boolean(ignorespec.get("enabled")))

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
        tower["height"] = self.towerHeight_spinbox.value()
        tower["width"] = self.towerWidth_spinbox.value()
        tower["segments"] = self.towerSegment_spinbox.value()
        tower["type"] = self.towerSupportType_comboBox.currentText()
        dictionary["tower"] = tower
        jib = dict()
        jib["length"] = self.jibLength_spinBox.value()
        jib["height"] = self.jibHeight_spinBox.value()
        jib["segments"] = self.jibSegment_spinBox.value()
        jib["type"] = self.jibSupportType_comboBox.currentText()
        dictionary["jib"] = jib
        counterjib = dict()
        counterjib["length"] = self.counterJibLength_spinBox.value()
        counterjib["height"] = self.counterJibHeight_spinBox.value()
        counterjib["segments"] = self.counterJibSegments_spinBox.value()
        counterjib["type"] = self.counterJibSupportType_comboBox.currentText()
        dictionary["counterjib"] = counterjib
        fem = dict()
        fem["jibLeft"] = self.jib_left_spinBox.value()
        fem["jibRight"] = self.jib_right_spinBox.value()
        fem["counterJibLeft"] = self.counterjib_left_spinBox.value()
        fem["counterJibRight"] = self.counterjib_right_spinBox.value()
        fem["scale"] = self.multiplierSpinBox.value()
        dictionary["fem"] = fem
        wind = dict()
        wind["enabled"] = self.wind_settings.isChecked()
        wind["direction"] = self.wind_direction.currentText()
        wind["force"] = self.wind_force.value()
        dictionary["wind"] = wind
        gravity = dict()
        gravity["enabled"] = self.enable_gravity.isChecked()
        dictionary["gravity"] = gravity
        ignorespec = dict()
        ignorespec["enabled"] = self.ignore_specification.isChecked()
        dictionary["ignorespec"] = ignorespec
        self.is_saved = True
        return dictionary

    def report_bug(self):
        QMessageBox.about(self, "Bug Report",
                          "You found a bug and want to report it? Great, please open an issue on "
                          "<a href='https://github.com/'>Github</a> where you decribe the bug in as much details as possible. "
                          "If you can please add screenshots or anything else. That can help us to fix it as soon as possible")

    def about(self):
        QMessageBox.about(self, "About Crane Simulator 2024",
                          "<b>Crane Simulator 2024</b> is a software written in Python which was developed in the "
                          "context of a project course at the TU Darmstadt. The source code is available on Github.")

    def update_debug_tree_widget(self, nodes, beams, def_nodes):
        """Updates node and beam tree in 'Debug' tab"""
        self.debug_treeWidget.clear()
        tree_items = [create_tree_item(nodes, "Nodes"), create_tree_item(beams, "Beams"), create_tree_item(def_nodes, "Deformed nodes")]
        self.debug_treeWidget.insertTopLevelItems(0, tree_items)

    def update_fem_tree_widget(self, N, R, U):
        """Updates node and beam tree in 'Debug' tab"""
        self.fem_treeWidget.clear()
        tree_items = [
            create_tree_item(N.round(decimals=4), "Axial Forces (positive = tension, negative = compression)"),
            create_tree_item(R.round(decimals=2), "Reaction Forces (positive = upward, negative = downward)"),
            create_tree_item(U.round(decimals=4), "Deformation at nodes")]
        self.fem_treeWidget.insertTopLevelItems(0, tree_items)

    def set_dims(self):
        """Sets dimensions from what is currently in the input fields"""
        # Reset all old dimensions
        self.dims.clear_all()
        # Set all tower dimensions
        self.dims.set_tower_height(self.towerHeight_spinbox.value())
        self.dims.set_tower_width(self.towerWidth_spinbox.value())
        self.dims.set_tower_segments(self.towerSegment_spinbox.value())
        self.dims.set_tower_support_type(self.towerSupportType_comboBox.currentText())
        # Set all jib dimensions
        self.dims.set_jib_height(self.jibHeight_spinBox.value())
        self.dims.set_jib_length(self.jibLength_spinBox.value())
        self.dims.set_jib_segments(self.jibSegment_spinBox.value())
        self.dims.set_jib_support_type(self.jibSupportType_comboBox.currentText())
        # Set all counter jib dimensions
        self.dims.set_counter_jib_height(self.counterJibHeight_spinBox.value())
        self.dims.set_counter_jib_length(self.counterJibLength_spinBox.value())
        self.dims.set_counter_jib_segments(self.counterJibSegments_spinBox.value())
        self.dims.set_counter_jib_support_type(self.counterJibSupportType_comboBox.currentText())

    def update_plot(self):
        """Updates 3D plot"""
        # Remove existing toolbar and canvas otherwise only the old one will be displayed instead of the new one
        # Maybe there is another way to do this
        self.plot_layout.removeWidget(self.toolbar)
        self.plot_layout.removeWidget(self.canvas)

        # Create new canvas and toolbar we will use for plotting
        updated_canvas = matplotlib_canvas(self, width=5, height=4, dpi=100)
        self.toolbar = NavigationToolbar(updated_canvas, self)
        self.canvas = updated_canvas
        self.plot_layout.addWidget(self.toolbar)
        self.plot_layout.addWidget(self.canvas)

        # Build undeformed crane with updated values
        nodes, beams = crane.get_crane()
        plotter.plot(nodes, beams, 'gray', '--', 'Undeformed', self.canvas.axes, self.canvas.fig)

        if self.fem_settings.isChecked():
            # Build deformed crane with updated values
            multiplier = self.multiplierSpinBox.value()
            self.N, self.R, self.U = self.crane.analyze()
            deformed_nodes = self.U * multiplier + nodes
            if self.axial_coloring.isChecked():
                plotter.plot_deformation_with_grad(nodes, deformed_nodes, beams, '-', self.canvas.axes, self.canvas.fig, self.N, self.cmap.currentText())
            else:
                plotter.plot(deformed_nodes, beams, 'red', '-', 'Deformed', self.canvas.axes, self.canvas.fig)
            # plotter.plot_deformation(nodes, deformed_nodes, beams, '-', self.canvas.axes, self.canvas.fig)
            
            self.output.appendPlainText("Jib displacement at front where forces are applied")
            self.output.appendPlainText(
                str(deformed_nodes[crane.Dims.JIB_NUM_NODES - 2] - nodes[crane.Dims.JIB_NUM_NODES - 2]))
            self.output.appendPlainText(
                str(deformed_nodes[crane.Dims.JIB_NUM_NODES - 1] - nodes[crane.Dims.JIB_NUM_NODES - 1]))
            self.output.appendPlainText("\nCounter Jib displacement at back where forces are applied")
            self.output.appendPlainText(str(deformed_nodes[len(deformed_nodes) - 2] - nodes[len(nodes) - 2]))
            self.output.appendPlainText(str(deformed_nodes[len(deformed_nodes) - 1] - nodes[len(nodes) - 1]))
            self.output.appendPlainText('\n')

    def apply_configuration(self):
        """Updates crane configuration"""
        self.is_saved = False
        self.progressBar.reset()
        self.progressBar.setValue(0)

        self.set_dims()
        # Will always generate a tower
        crane.should_have_tower(True)
        crane.set_tower_dims(self.dims.get_tower_height(),
                             self.dims.get_tower_width(),
                             self.dims.get_tower_segments(),
                             self.dims.get_tower_support_type())
        # Will always generate a jib
        crane.should_have_jib(True)
        crane.set_jib_dims(self.dims.get_jib_length(),
                           self.dims.get_jib_height(),
                           self.dims.get_jib_segments())
        # Will always generate a counter jib
        crane.should_have_counter_jib(True)
        crane.set_counterjib_dims(self.dims.get_counter_jib_length(),
                                  self.dims.get_counter_jib_height(),
                                  self.dims.get_counter_jib_segments(),
                                  self.dims.get_counter_jib_support_type())

        self.crane.build_crane()

        if self.check_config():
            if not self.enable_gravity.isChecked() or not self.wind_settings.isChecked():
                self.crane.reset_forces(self)

            if self.enable_gravity.isChecked():
                self.crane.enable_gravity(self)

            if self.wind_settings.isChecked():
                self.crane.enable_wind(self.wind_direction.currentText(), self.wind_force.value())

            self.update_plot()
            nodes, beams = crane.get_crane()
            self.update_debug_tree_widget(nodes, beams, nodes + self.U)
            self.update_info()

            if self.fem_settings.isChecked():
                self.update_fem_tree_widget(self.N, self.R, self.U)

        self.progressBar.setValue(100)

    def update_info(self):
        """Updates infobox in the bottom left"""
        total_length = crane.get_length()
        total_length = total_length / 1000
        total_volumn = total_length * self.crane.A
        total_mass = total_volumn * self.crane.DENSITY
        total_cost = total_mass / 1000 * 1000
        self.total_length.setText(f'{(total_length):.3f} m')
        self.total_volumn.setText(f'{(total_volumn):.3f} m\u00B3')
        self.total_mass.setText(f'{(total_mass):.3f} kg')
        self.total_cost.setText(f'{(total_cost):.2f} \u20AC')

    def check_config(self):
        """Checks if all beams are within the required range"""
        if not self.ignore_specification.isChecked():
            tower_longest = crane.tower.get_longest_beam()
            if tower_longest < 500 or tower_longest > 2000:
                QMessageBox.critical(self, 'Specification Violation',
                                     f'Your inputted tower parameters violate the length requirements for a beam with a length of {tower_longest:.4f}mm which falls outside the allowed range of 500-2000mm')
                return False
            jib_longest = crane.jib.get_longest_beam()
            if jib_longest < 500 or jib_longest > 2000:
                QMessageBox.critical(self, 'Specification Violation',
                                     f'Your inputted jib parameters violate the length requirements for a beam with a length of {jib_longest:.4f}mm which falls outside the allowed range of 500-2000mm')
                return False
            counterjib_longest = crane.counterjib.get_longest_beam()
            if counterjib_longest < 500 or counterjib_longest > 2000:
                QMessageBox.critical(self, 'Specification Violation',
                                     f'Your inputted counterjib parameters violate the length requirements for a beam with a length of {counterjib_longest:.4f}mm which falls outside the allows range of 500-2000mm')
                return False
        return True


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()

# Will not be reached until application is closed
