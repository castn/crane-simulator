import logging
import sys

sys.path.append('./')

import numpy as np
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMessageBox, QTreeWidgetItem
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


def create_tree_item(beams, name):
    """Creates tree for 'Debug' tab"""
    tree_item = QTreeWidgetItem([name])
    i = 0
    for beam in beams:
        child = QTreeWidgetItem([f"{i}. {beam}"])
        tree_item.addChild(child)
        i = i + 1
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
        self.treeWidget.setColumnCount(1)
        self.treeWidget.setHeaderLabel("View Points of Nodes/Beams")
        # Set default size of plotBox, otherwise will shrink to minimal and needs manual adjustment
        self.plotBox.setGeometry(0, 0, 716, 544)
        # Create matplot canvas and associated toolbar
        self.canvas = matplotlib_canvas(self, width=5, height=4, dpi=100)
        self.toolbar = NavigationToolbar(self.canvas, self)
        # Add canvas and toolbar to dedicated widget in this window
        self.plot_layout.addWidget(self.toolbar)
        self.plot_layout.addWidget(self.canvas)

        self.dims = Dims()
        self.set_dims()
        self.apply_configuration()
        self.update_plot()

        # Perform action on press of apply button
        self.apply_button.clicked.connect(self.apply_configuration)

    def update_tree_widget(self, beams, nodes):
        """Updates node and beam tree in 'Debug' tab"""
        self.treeWidget.clear()
        tree_items = [create_tree_item(nodes, "Nodes"), create_tree_item(beams, "Beams")]
        self.treeWidget.insertTopLevelItems(0, tree_items)

    def set_dims(self):
        """Sets dimensions from what is currently in the input fields"""
        self.dims.clear_all()

        if self.towerBox.isChecked():
            self.dims.set_tower_height(self.towerHeight_spinbox.value())
            self.dims.set_tower_width(self.towerWidth_spinbox.value())
            self.dims.set_tower_segments(self.towerSegment_spinbox.value())
            self.dims.set_tower_support_type(self.towerSupportType_comboBox.currentText())
        if self.jibBox.isChecked():
            self.dims.set_jib_height(self.jibHeight_spinBox.value())
            self.dims.set_jib_length(self.jibLength_spinBox.value())
            self.dims.set_jib_segments(self.jibSegment_spinBox.value())
            self.dims.set_jib_support_type(self.jibSupportType_comboBox.currentText())
        if self.counterJibBox.isChecked():
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
        plotter.plot(nodes, beams, 'gray', '--', 'Undeformed', updated_canvas.axes, updated_canvas.fig)

        if self.enableFEM_checkbox.isChecked():
            # Build deformed crane with updated values
            scale = 10
            self.N, self.R, self.U = crane.analyze()
            deformed_nodes = self.U * scale + nodes
            plotter.plot(deformed_nodes, beams, 'red', '-', 'Deformed', updated_canvas.axes, updated_canvas.fig)

    def apply_configuration(self):
        """Updates crane configuration"""
        self.progressBar.reset()
        self.progressBar.setValue(0)

        self.set_dims()

        if self.towerBox.isChecked():
            crane.should_have_tower(True)
            crane.set_tower_dims(self.dims.get_tower_height(), self.dims.get_tower_width(),
                                 self.dims.get_tower_segments(), self.dims.get_tower_support_type())
        else:
            crane.should_have_tower(False)
        if self.jibBox.isChecked():
            crane.should_have_jib(True)
            crane.set_jib_dims(self.dims.get_jib_length(), self.dims.get_jib_height(), self.dims.get_jib_segments())
        else:
            crane.should_have_jib(False)
        if self.counterJibBox.isChecked():
            crane.should_have_counter_jib(True)
            crane.set_counterjib_dims(self.dims.get_counter_jib_length(), self.dims.get_counter_jib_height(),
                                      self.dims.get_counter_jib_segments(),
                                      self.dims.get_counter_jib_support_type())
        else:
            crane.should_have_counter_jib(False)

        crane.build_crane()

        if self.check_config():
            self.update_plot()
            nodes, beams = crane.get_crane()
            self.update_tree_widget(beams, nodes)

            if self.enableFEM_checkbox.isChecked():
                self.analysis.appendPlainText('Axial Forces (positive = tension, negative = compression)')
                self.analysis.appendPlainText(str(self.N[np.newaxis].T))
                self.analysis.appendPlainText('Reaction Forces (positive = upward, negative = downward)')
                self.analysis.appendPlainText(str(self.R))
                self.analysis.appendPlainText('Deformation at nodes')
                self.analysis.appendPlainText(str(self.U))

        self.progressBar.setValue(100)

    def check_config(self):
        """Checks if all beams are within the required range"""
        if not self.ignore_specification.isChecked():
            tower_longest = crane.tower.get_longest_beam()
            if tower_longest < 500 or tower_longest > 2000:
                QMessageBox.about(self, 'Error',
                                  f'Your inputted tower parameters violate the length requirements for a beam with a length of {tower_longest:.4f}mm which falls outside the allows range of 500-2000mm')
                return False
            jib_longest = crane.jib.get_longest_beam()
            if jib_longest < 500 or jib_longest > 2000:
                QMessageBox.about(self, 'Error',
                                  f'Your inputted jib parameters violate the length requirements for a beam with a length of {jib_longest:.4f}mm which falls outside the allows range of 500-2000mm')
                return False
            counterjib_longest = crane.counterjib.get_longest_beam()
            if counterjib_longest < 500 or counterjib_longest > 2000:
                QMessageBox.about(self, 'Error',
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
