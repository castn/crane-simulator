import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from MainWindow import Ui_MainWindow
import crane


class matplotlib_canvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(matplotlib_canvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # Call the autogenerated Ui_MainWindow.py, generated from the .ui file using the command "pyuic6 mainwindow.ui -o MainWindow.py"
        self.setupUi(self)

        sc = matplotlib_canvas(self, width=5, height=4, dpi=100)
        sc.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        plot_toolbar = NavigationToolbar(sc, self)
        # Add toolbar and canvas to window
        self.plot_layout.addWidget(plot_toolbar)
        self.plot_layout.addWidget(sc)

        self.apply_button.clicked.connect(self.apply_configuration)


    def apply_configuration(self):
        self.output.appendPlainText(f"Tower values: [{self.towerHeight_spinbox.value()},{self.towerWidth_spinbox.value()},{self.towerSegment_spinbox.value()},{self.towerSupportType_comboBox.currentText()}]")
        self.output.appendPlainText(f"Jib values: [{self.jibLength_spinBox.value()},{self.jibLength_spinBox.value()},{self.jibLength_spinBox.value()},{self.jibSupportType_comboBox.currentText()}]")
        self.output.appendPlainText(f"CounterJib values: [{self.counterJibLength_spinBox.value()},{self.counterJibHeight_spinBox.value()},{self.counterJibSegments_spinBox.value()},{self.counterJibSupportType_comboBox.currentText()}]")
        self.output.appendPlainText(f"Enable FEM: [{self.enableFEM_checkbox.isChecked()}]")
        self.output.appendPlainText("------")
        self.progressBar.setValue(100)
        
        if self.towerBox.isChecked():
            crane.set_tower_dims(self.towerHeight_spinbox.value(), self.towerWidth_spinbox.value(),
                             self.towerSegment_spinbox.value(), self.towerSupportType_comboBox.currentText())
        if self.jibBox.isChecked():
            crane.set_jib_dims(self.jibLength_spinBox.value(), self.jibLength_spinBox.value(), self.jibLength_spinBox.value())
        if self.counterJibBox.isChecked():
            crane.set_counterjib_dims(self.counterJibLength_spinBox.value(), self.counterJibHeight_spinBox.value(),
                                  self.counterJibSegments_spinBox.value(), self.counterJibSupportType_comboBox.currentText())




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
