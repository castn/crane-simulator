# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1022, 1216)
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.options = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.options.setFlat(False)
        self.options.setObjectName("options")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.options)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Settings = QtWidgets.QTabWidget(parent=self.options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Settings.sizePolicy().hasHeightForWidth())
        self.Settings.setSizePolicy(sizePolicy)
        self.Settings.setObjectName("Settings")
        self.crane = QtWidgets.QWidget()
        self.crane.setObjectName("crane")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.crane)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.towerBox = QtWidgets.QGroupBox(parent=self.crane)
        self.towerBox.setCheckable(False)
        self.towerBox.setObjectName("towerBox")
        self.formLayout = QtWidgets.QFormLayout(self.towerBox)
        self.formLayout.setObjectName("formLayout")
        self.towerHeight_label = QtWidgets.QLabel(parent=self.towerBox)
        self.towerHeight_label.setObjectName("towerHeight_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.towerHeight_label)
        self.towerHeight_spinbox = QtWidgets.QSpinBox(parent=self.towerBox)
        self.towerHeight_spinbox.setMinimum(1)
        self.towerHeight_spinbox.setMaximum(1000000)
        self.towerHeight_spinbox.setProperty("value", 2000)
        self.towerHeight_spinbox.setObjectName("towerHeight_spinbox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.towerHeight_spinbox)
        self.towerWidth_label = QtWidgets.QLabel(parent=self.towerBox)
        self.towerWidth_label.setObjectName("towerWidth_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.towerWidth_label)
        self.towerWidth_spinbox = QtWidgets.QSpinBox(parent=self.towerBox)
        self.towerWidth_spinbox.setMinimum(1)
        self.towerWidth_spinbox.setMaximum(1000000)
        self.towerWidth_spinbox.setProperty("value", 1000)
        self.towerWidth_spinbox.setObjectName("towerWidth_spinbox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.towerWidth_spinbox)
        self.towerSegment_label = QtWidgets.QLabel(parent=self.towerBox)
        self.towerSegment_label.setObjectName("towerSegment_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.towerSegment_label)
        self.towerSupportType_label = QtWidgets.QLabel(parent=self.towerBox)
        self.towerSupportType_label.setObjectName("towerSupportType_label")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.ItemRole.LabelRole, self.towerSupportType_label)
        self.towerSupportType_comboBox = QtWidgets.QComboBox(parent=self.towerBox)
        self.towerSupportType_comboBox.setAutoFillBackground(False)
        self.towerSupportType_comboBox.setObjectName("towerSupportType_comboBox")
        self.towerSupportType_comboBox.addItem("")
        self.towerSupportType_comboBox.addItem("")
        self.towerSupportType_comboBox.addItem("")
        self.towerSupportType_comboBox.addItem("")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.ItemRole.FieldRole, self.towerSupportType_comboBox)
        self.towerSegment_spinbox = QtWidgets.QSpinBox(parent=self.towerBox)
        self.towerSegment_spinbox.setMinimum(1)
        self.towerSegment_spinbox.setMaximum(1000000)
        self.towerSegment_spinbox.setProperty("value", 2)
        self.towerSegment_spinbox.setObjectName("towerSegment_spinbox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.towerSegment_spinbox)
        self.verticalLayout_4.addWidget(self.towerBox)
        self.jibBox = QtWidgets.QGroupBox(parent=self.crane)
        self.jibBox.setCheckable(False)
        self.jibBox.setObjectName("jibBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.jibBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.jibLength_label = QtWidgets.QLabel(parent=self.jibBox)
        self.jibLength_label.setObjectName("jibLength_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.jibLength_label)
        self.jibLength_spinBox = QtWidgets.QSpinBox(parent=self.jibBox)
        self.jibLength_spinBox.setMinimum(1)
        self.jibLength_spinBox.setMaximum(1000000)
        self.jibLength_spinBox.setProperty("value", 2000)
        self.jibLength_spinBox.setObjectName("jibLength_spinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.jibLength_spinBox)
        self.jibHeight_label = QtWidgets.QLabel(parent=self.jibBox)
        self.jibHeight_label.setObjectName("jibHeight_label")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.jibHeight_label)
        self.jibHeight_spinBox = QtWidgets.QSpinBox(parent=self.jibBox)
        self.jibHeight_spinBox.setMinimum(1)
        self.jibHeight_spinBox.setMaximum(1000000)
        self.jibHeight_spinBox.setProperty("value", 1000)
        self.jibHeight_spinBox.setObjectName("jibHeight_spinBox")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.jibHeight_spinBox)
        self.jibSegment_label = QtWidgets.QLabel(parent=self.jibBox)
        self.jibSegment_label.setObjectName("jibSegment_label")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.jibSegment_label)
        self.jibSegment_spinBox = QtWidgets.QSpinBox(parent=self.jibBox)
        self.jibSegment_spinBox.setMinimum(1)
        self.jibSegment_spinBox.setMaximum(1000000)
        self.jibSegment_spinBox.setProperty("value", 2)
        self.jibSegment_spinBox.setObjectName("jibSegment_spinBox")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.jibSegment_spinBox)
        self.jibSupportType_label = QtWidgets.QLabel(parent=self.jibBox)
        self.jibSupportType_label.setObjectName("jibSupportType_label")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.ItemRole.LabelRole, self.jibSupportType_label)
        self.jibSupportType_comboBox = QtWidgets.QComboBox(parent=self.jibBox)
        self.jibSupportType_comboBox.setObjectName("jibSupportType_comboBox")
        self.jibSupportType_comboBox.addItem("")
        self.jibSupportType_comboBox.addItem("")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.ItemRole.FieldRole, self.jibSupportType_comboBox)
        self.verticalLayout_4.addWidget(self.jibBox)
        self.counterJibBox = QtWidgets.QGroupBox(parent=self.crane)
        self.counterJibBox.setCheckable(False)
        self.counterJibBox.setObjectName("counterJibBox")
        self.formLayout_3 = QtWidgets.QFormLayout(self.counterJibBox)
        self.formLayout_3.setObjectName("formLayout_3")
        self.counterJibLength_label = QtWidgets.QLabel(parent=self.counterJibBox)
        self.counterJibLength_label.setObjectName("counterJibLength_label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.counterJibLength_label)
        self.counterJibLength_spinBox = QtWidgets.QSpinBox(parent=self.counterJibBox)
        self.counterJibLength_spinBox.setMinimum(1)
        self.counterJibLength_spinBox.setMaximum(1000000)
        self.counterJibLength_spinBox.setProperty("value", 1000)
        self.counterJibLength_spinBox.setObjectName("counterJibLength_spinBox")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.counterJibLength_spinBox)
        self.counterJibHeight_label = QtWidgets.QLabel(parent=self.counterJibBox)
        self.counterJibHeight_label.setObjectName("counterJibHeight_label")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.counterJibHeight_label)
        self.counterJibHeight_spinBox = QtWidgets.QSpinBox(parent=self.counterJibBox)
        self.counterJibHeight_spinBox.setMinimum(1)
        self.counterJibHeight_spinBox.setMaximum(1000000)
        self.counterJibHeight_spinBox.setProperty("value", 800)
        self.counterJibHeight_spinBox.setObjectName("counterJibHeight_spinBox")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.counterJibHeight_spinBox)
        self.counterJibSupportType_label = QtWidgets.QLabel(parent=self.counterJibBox)
        self.counterJibSupportType_label.setObjectName("counterJibSupportType_label")
        self.formLayout_3.setWidget(9, QtWidgets.QFormLayout.ItemRole.LabelRole, self.counterJibSupportType_label)
        self.counterJibSegments_label = QtWidgets.QLabel(parent=self.counterJibBox)
        self.counterJibSegments_label.setObjectName("counterJibSegments_label")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.counterJibSegments_label)
        self.counterJibSegments_spinBox = QtWidgets.QSpinBox(parent=self.counterJibBox)
        self.counterJibSegments_spinBox.setMinimum(1)
        self.counterJibSegments_spinBox.setMaximum(1000000)
        self.counterJibSegments_spinBox.setProperty("value", 2)
        self.counterJibSegments_spinBox.setObjectName("counterJibSegments_spinBox")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.counterJibSegments_spinBox)
        self.counterJibSupportType_comboBox = QtWidgets.QComboBox(parent=self.counterJibBox)
        self.counterJibSupportType_comboBox.setObjectName("counterJibSupportType_comboBox")
        self.counterJibSupportType_comboBox.addItem("")
        self.counterJibSupportType_comboBox.addItem("")
        self.counterJibSupportType_comboBox.addItem("")
        self.counterJibSupportType_comboBox.addItem("")
        self.formLayout_3.setWidget(9, QtWidgets.QFormLayout.ItemRole.FieldRole, self.counterJibSupportType_comboBox)
        self.verticalLayout_4.addWidget(self.counterJibBox)
        self.Settings.addTab(self.crane, "")
        self.settings = QtWidgets.QWidget()
        self.settings.setObjectName("settings")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.settings)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.enable_gravity = QtWidgets.QCheckBox(parent=self.settings)
        self.enable_gravity.setObjectName("enable_gravity")
        self.verticalLayout_6.addWidget(self.enable_gravity)
        self.wind_settings = QtWidgets.QGroupBox(parent=self.settings)
        self.wind_settings.setCheckable(True)
        self.wind_settings.setChecked(False)
        self.wind_settings.setObjectName("wind_settings")
        self.formLayout_7 = QtWidgets.QFormLayout(self.wind_settings)
        self.formLayout_7.setObjectName("formLayout_7")
        self.direction_label = QtWidgets.QLabel(parent=self.wind_settings)
        self.direction_label.setObjectName("direction_label")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.direction_label)
        self.wind_direction = QtWidgets.QComboBox(parent=self.wind_settings)
        self.wind_direction.setObjectName("wind_direction")
        self.wind_direction.addItem("")
        self.wind_direction.addItem("")
        self.wind_direction.addItem("")
        self.wind_direction.addItem("")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.wind_direction)
        self.wind_force_label = QtWidgets.QLabel(parent=self.wind_settings)
        self.wind_force_label.setObjectName("wind_force_label")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.wind_force_label)
        self.wind_force = QtWidgets.QSpinBox(parent=self.wind_settings)
        self.wind_force.setMaximum(500)
        self.wind_force.setProperty("value", 1)
        self.wind_force.setObjectName("wind_force")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.wind_force)
        self.verticalLayout_6.addWidget(self.wind_settings)
        self.fem_settings = QtWidgets.QGroupBox(parent=self.settings)
        self.fem_settings.setEnabled(True)
        self.fem_settings.setCheckable(False)
        self.fem_settings.setObjectName("fem_settings")
        self.formLayout_6 = QtWidgets.QFormLayout(self.fem_settings)
        self.formLayout_6.setObjectName("formLayout_6")
        self.multiplier_label = QtWidgets.QLabel(parent=self.fem_settings)
        self.multiplier_label.setObjectName("multiplier_label")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.multiplier_label)
        self.multiplierSpinBox = QtWidgets.QSpinBox(parent=self.fem_settings)
        self.multiplierSpinBox.setMinimum(1)
        self.multiplierSpinBox.setMaximum(100)
        self.multiplierSpinBox.setProperty("value", 1)
        self.multiplierSpinBox.setObjectName("multiplierSpinBox")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.multiplierSpinBox)
        self.lable_jib_left = QtWidgets.QLabel(parent=self.fem_settings)
        self.lable_jib_left.setObjectName("lable_jib_left")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lable_jib_left)
        self.jib_left_spinBox = QtWidgets.QSpinBox(parent=self.fem_settings)
        self.jib_left_spinBox.setMinimum(-5000)
        self.jib_left_spinBox.setMaximum(5000)
        self.jib_left_spinBox.setProperty("value", -250)
        self.jib_left_spinBox.setObjectName("jib_left_spinBox")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.jib_left_spinBox)
        self.label_jib_right = QtWidgets.QLabel(parent=self.fem_settings)
        self.label_jib_right.setObjectName("label_jib_right")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_jib_right)
        self.jib_right_spinBox = QtWidgets.QSpinBox(parent=self.fem_settings)
        self.jib_right_spinBox.setMinimum(-5000)
        self.jib_right_spinBox.setMaximum(5000)
        self.jib_right_spinBox.setProperty("value", -250)
        self.jib_right_spinBox.setObjectName("jib_right_spinBox")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.jib_right_spinBox)
        self.counterjib_left_spinBox = QtWidgets.QSpinBox(parent=self.fem_settings)
        self.counterjib_left_spinBox.setMinimum(-5000)
        self.counterjib_left_spinBox.setMaximum(5000)
        self.counterjib_left_spinBox.setProperty("value", -100)
        self.counterjib_left_spinBox.setObjectName("counterjib_left_spinBox")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.counterjib_left_spinBox)
        self.label_counter_jib_left = QtWidgets.QLabel(parent=self.fem_settings)
        self.label_counter_jib_left.setObjectName("label_counter_jib_left")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_counter_jib_left)
        self.label_counter_jib_right = QtWidgets.QLabel(parent=self.fem_settings)
        self.label_counter_jib_right.setObjectName("label_counter_jib_right")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_counter_jib_right)
        self.counterjib_right_spinBox = QtWidgets.QSpinBox(parent=self.fem_settings)
        self.counterjib_right_spinBox.setMinimum(-5000)
        self.counterjib_right_spinBox.setMaximum(5000)
        self.counterjib_right_spinBox.setProperty("value", -100)
        self.counterjib_right_spinBox.setObjectName("counterjib_right_spinBox")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.counterjib_right_spinBox)
        self.verticalLayout_6.addWidget(self.fem_settings)
        self.ignore_specification = QtWidgets.QCheckBox(parent=self.settings)
        self.ignore_specification.setObjectName("ignore_specification")
        self.verticalLayout_6.addWidget(self.ignore_specification)
        self.axial_coloring = QtWidgets.QGroupBox(parent=self.settings)
        self.axial_coloring.setCheckable(True)
        self.axial_coloring.setObjectName("axial_coloring")
        self.formLayout_8 = QtWidgets.QFormLayout(self.axial_coloring)
        self.formLayout_8.setObjectName("formLayout_8")
        self.cmap_label = QtWidgets.QLabel(parent=self.axial_coloring)
        self.cmap_label.setObjectName("cmap_label")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cmap_label)
        self.cmap = QtWidgets.QComboBox(parent=self.axial_coloring)
        self.cmap.setObjectName("cmap")
        self.cmap.addItem("")
        self.cmap.addItem("")
        self.cmap.addItem("")
        self.cmap.addItem("")
        self.cmap.addItem("")
        self.cmap.addItem("")
        self.cmap.addItem("")
        self.cmap.addItem("")
        self.cmap.addItem("")
        self.cmap.addItem("")
        self.cmap.addItem("")
        self.cmap.addItem("")
        self.cmap.addItem("")
        self.cmap.addItem("")
        self.cmap.addItem("")
        self.cmap.addItem("")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cmap)
        self.verticalLayout_6.addWidget(self.axial_coloring)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.Settings.addTab(self.settings, "")
        self.verticalLayout_3.addWidget(self.Settings)
        self.gridLayout.addWidget(self.options, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_5 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_5.setObjectName("formLayout_5")
        self.total_length_label = QtWidgets.QLabel(parent=self.groupBox)
        self.total_length_label.setObjectName("total_length_label")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.total_length_label)
        self.total_length = QtWidgets.QLineEdit(parent=self.groupBox)
        self.total_length.setReadOnly(True)
        self.total_length.setObjectName("total_length")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.total_length)
        self.total_volume_label = QtWidgets.QLabel(parent=self.groupBox)
        self.total_volume_label.setObjectName("total_volume_label")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.total_volume_label)
        self.total_volume = QtWidgets.QLineEdit(parent=self.groupBox)
        self.total_volume.setReadOnly(True)
        self.total_volume.setObjectName("total_volume")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.total_volume)
        self.total_mass = QtWidgets.QLineEdit(parent=self.groupBox)
        self.total_mass.setReadOnly(True)
        self.total_mass.setObjectName("total_mass")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.total_mass)
        self.total_mass_volume = QtWidgets.QLabel(parent=self.groupBox)
        self.total_mass_volume.setObjectName("total_mass_volume")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.total_mass_volume)
        self.total_cost_label = QtWidgets.QLabel(parent=self.groupBox)
        self.total_cost_label.setObjectName("total_cost_label")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.total_cost_label)
        self.total_cost = QtWidgets.QLineEdit(parent=self.groupBox)
        self.total_cost.setReadOnly(True)
        self.total_cost.setObjectName("total_cost")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.total_cost)
        self.gridLayout.addWidget(self.groupBox, 3, 0, 1, 1)
        self.runBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.runBox.setObjectName("runBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.runBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.apply_button = QtWidgets.QPushButton(parent=self.runBox)
        self.apply_button.setCheckable(False)
        self.apply_button.setDefault(False)
        self.apply_button.setObjectName("apply_button")
        self.verticalLayout_5.addWidget(self.apply_button)
        self.optimize_button = QtWidgets.QPushButton(parent=self.runBox)
        self.optimize_button.setObjectName("optimize_button")
        self.verticalLayout_5.addWidget(self.optimize_button)
        self.progressBar = QtWidgets.QProgressBar(parent=self.runBox)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_5.addWidget(self.progressBar)
        self.gridLayout.addWidget(self.runBox, 5, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        self.formLayout_4.setLayout(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.gridLayout)
        self.splitter = QtWidgets.QSplitter(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter.setObjectName("splitter")
        self.plotBox = QtWidgets.QTabWidget(parent=self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotBox.sizePolicy().hasHeightForWidth())
        self.plotBox.setSizePolicy(sizePolicy)
        self.plotBox.setObjectName("plotBox")
        self.unoptimizedPlot = QtWidgets.QWidget()
        self.unoptimizedPlot.setObjectName("unoptimizedPlot")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.unoptimizedPlot)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.unoptimized_plot_layout = QtWidgets.QVBoxLayout()
        self.unoptimized_plot_layout.setObjectName("unoptimized_plot_layout")
        self.verticalLayout_10.addLayout(self.unoptimized_plot_layout)
        self.plotBox.addTab(self.unoptimizedPlot, "")
        self.optimizedPlot = QtWidgets.QWidget()
        self.optimizedPlot.setObjectName("optimizedPlot")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.optimizedPlot)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.optimize_plot_layout = QtWidgets.QVBoxLayout()
        self.optimize_plot_layout.setObjectName("optimize_plot_layout")
        self.verticalLayout_7.addLayout(self.optimize_plot_layout)
        self.plotBox.addTab(self.optimizedPlot, "")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.splitter)
        self.tabWidget.setObjectName("tabWidget")
        self.console_output = QtWidgets.QWidget()
        self.console_output.setObjectName("console_output")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.console_output)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.output = QtWidgets.QPlainTextEdit(parent=self.console_output)
        self.output.setReadOnly(True)
        self.output.setObjectName("output")
        self.verticalLayout_9.addWidget(self.output)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.clear_button = QtWidgets.QPushButton(parent=self.console_output)
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout.addWidget(self.clear_button)
        self.verticalLayout_9.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.console_output, "")
        self.fem_output = QtWidgets.QWidget()
        self.fem_output.setObjectName("fem_output")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.fem_output)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.fem_treeWidget = QtWidgets.QTreeWidget(parent=self.fem_output)
        self.fem_treeWidget.setObjectName("fem_treeWidget")
        self.fem_treeWidget.headerItem().setText(0, "1")
        self.verticalLayout_8.addWidget(self.fem_treeWidget)
        self.tabWidget.addTab(self.fem_output, "")
        self.debug_output = QtWidgets.QWidget()
        self.debug_output.setObjectName("debug_output")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.debug_output)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.debug_treeWidget = QtWidgets.QTreeWidget(parent=self.debug_output)
        self.debug_treeWidget.setObjectName("debug_treeWidget")
        self.debug_treeWidget.headerItem().setText(0, "1")
        self.debug_treeWidget.header().setVisible(True)
        self.debug_treeWidget.header().setCascadingSectionResizes(True)
        self.debug_treeWidget.header().setHighlightSections(False)
        self.debug_treeWidget.header().setSortIndicatorShown(False)
        self.debug_treeWidget.header().setStretchLastSection(True)
        self.verticalLayout_11.addWidget(self.debug_treeWidget)
        self.tabWidget.addTab(self.debug_output, "")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.splitter)
        self.verticalLayout_2.addLayout(self.formLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1022, 22))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(parent=self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(parent=MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionAbout = QtGui.QAction(parent=MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionReport_bug = QtGui.QAction(parent=MainWindow)
        self.actionReport_bug.setObjectName("actionReport_bug")
        self.actionRecently_Edited = QtGui.QAction(parent=MainWindow)
        self.actionRecently_Edited.setObjectName("actionRecently_Edited")
        self.actionExit = QtGui.QAction(parent=MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout_Qt = QtGui.QAction(parent=MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.menu_File.addAction(self.actionOpen)
        self.menu_File.addAction(self.actionRecently_Edited)
        self.menu_File.addAction(self.actionSave)
        self.menu_File.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionReport_bug)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.Settings.setCurrentIndex(0)
        self.plotBox.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.clear_button.clicked.connect(self.output.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.jibLength_spinBox, self.jibHeight_spinBox)
        MainWindow.setTabOrder(self.jibHeight_spinBox, self.counterJibLength_spinBox)
        MainWindow.setTabOrder(self.counterJibLength_spinBox, self.counterJibHeight_spinBox)
        MainWindow.setTabOrder(self.counterJibHeight_spinBox, self.clear_button)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.options.setTitle(_translate("MainWindow", "Options"))
        self.towerBox.setTitle(_translate("MainWindow", "Tower"))
        self.towerHeight_label.setText(_translate("MainWindow", "Height"))
        self.towerHeight_spinbox.setSuffix(_translate("MainWindow", " mm"))
        self.towerWidth_label.setText(_translate("MainWindow", "Width"))
        self.towerWidth_spinbox.setSuffix(_translate("MainWindow", " mm"))
        self.towerSegment_label.setText(_translate("MainWindow", "Segments"))
        self.towerSupportType_label.setText(_translate("MainWindow", "Support Type"))
        self.towerSupportType_comboBox.setCurrentText(_translate("MainWindow", "Zigzag"))
        self.towerSupportType_comboBox.setItemText(0, _translate("MainWindow", "Zigzag"))
        self.towerSupportType_comboBox.setItemText(1, _translate("MainWindow", "None"))
        self.towerSupportType_comboBox.setItemText(2, _translate("MainWindow", "Cross"))
        self.towerSupportType_comboBox.setItemText(3, _translate("MainWindow", "Diagonal"))
        self.jibBox.setTitle(_translate("MainWindow", "Jib"))
        self.jibLength_label.setText(_translate("MainWindow", "Length"))
        self.jibLength_spinBox.setSuffix(_translate("MainWindow", " mm"))
        self.jibHeight_label.setText(_translate("MainWindow", "Height"))
        self.jibHeight_spinBox.setSuffix(_translate("MainWindow", " mm"))
        self.jibSegment_label.setText(_translate("MainWindow", "Segments"))
        self.jibSupportType_label.setText(_translate("MainWindow", "Support Type"))
        self.jibSupportType_comboBox.setCurrentText(_translate("MainWindow", "Truss"))
        self.jibSupportType_comboBox.setItemText(0, _translate("MainWindow", "Truss"))
        self.jibSupportType_comboBox.setItemText(1, _translate("MainWindow", "Set-back truss"))
        self.counterJibBox.setTitle(_translate("MainWindow", "Counter Jib"))
        self.counterJibLength_label.setText(_translate("MainWindow", "Length"))
        self.counterJibLength_spinBox.setSuffix(_translate("MainWindow", " mm"))
        self.counterJibHeight_label.setText(_translate("MainWindow", "Height"))
        self.counterJibHeight_spinBox.setSuffix(_translate("MainWindow", " mm"))
        self.counterJibSupportType_label.setText(_translate("MainWindow", "Support Type"))
        self.counterJibSegments_label.setText(_translate("MainWindow", "Segments"))
        self.counterJibSupportType_comboBox.setCurrentText(_translate("MainWindow", "Truss"))
        self.counterJibSupportType_comboBox.setItemText(0, _translate("MainWindow", "Truss"))
        self.counterJibSupportType_comboBox.setItemText(1, _translate("MainWindow", "None"))
        self.counterJibSupportType_comboBox.setItemText(2, _translate("MainWindow", "Single tower"))
        self.counterJibSupportType_comboBox.setItemText(3, _translate("MainWindow", "Twin towers"))
        self.Settings.setTabText(self.Settings.indexOf(self.crane), _translate("MainWindow", "Crane"))
        self.enable_gravity.setText(_translate("MainWindow", "Gravity"))
        self.wind_settings.setTitle(_translate("MainWindow", "Wind"))
        self.direction_label.setText(_translate("MainWindow", "Direction"))
        self.wind_direction.setItemText(0, _translate("MainWindow", "Front"))
        self.wind_direction.setItemText(1, _translate("MainWindow", "Left"))
        self.wind_direction.setItemText(2, _translate("MainWindow", "Right"))
        self.wind_direction.setItemText(3, _translate("MainWindow", "Back"))
        self.wind_force_label.setText(_translate("MainWindow", "Force"))
        self.wind_force.setSuffix(_translate("MainWindow", " kN"))
        self.fem_settings.setTitle(_translate("MainWindow", "FEM"))
        self.multiplier_label.setText(_translate("MainWindow", "Multiplier"))
        self.lable_jib_left.setText(_translate("MainWindow", "Jib Left"))
        self.jib_left_spinBox.setSuffix(_translate("MainWindow", " kN"))
        self.label_jib_right.setText(_translate("MainWindow", "Jib Right"))
        self.jib_right_spinBox.setSuffix(_translate("MainWindow", " kN"))
        self.counterjib_left_spinBox.setSuffix(_translate("MainWindow", " kN"))
        self.label_counter_jib_left.setText(_translate("MainWindow", "Counter Jib Left"))
        self.label_counter_jib_right.setText(_translate("MainWindow", "Counter Jib Right"))
        self.counterjib_right_spinBox.setSuffix(_translate("MainWindow", " kN"))
        self.ignore_specification.setText(_translate("MainWindow", "Ignore specifications of the project task"))
        self.axial_coloring.setTitle(_translate("MainWindow", "Axial forces visibility"))
        self.cmap_label.setText(_translate("MainWindow", "Color Map"))
        self.cmap.setItemText(0, _translate("MainWindow", "jet"))
        self.cmap.setItemText(1, _translate("MainWindow", "copper"))
        self.cmap.setItemText(2, _translate("MainWindow", "hot"))
        self.cmap.setItemText(3, _translate("MainWindow", "viridis"))
        self.cmap.setItemText(4, _translate("MainWindow", "plasma"))
        self.cmap.setItemText(5, _translate("MainWindow", "inferno"))
        self.cmap.setItemText(6, _translate("MainWindow", "magma"))
        self.cmap.setItemText(7, _translate("MainWindow", "cividis"))
        self.cmap.setItemText(8, _translate("MainWindow", "spring"))
        self.cmap.setItemText(9, _translate("MainWindow", "summer"))
        self.cmap.setItemText(10, _translate("MainWindow", "autumn"))
        self.cmap.setItemText(11, _translate("MainWindow", "winter"))
        self.cmap.setItemText(12, _translate("MainWindow", "cool"))
        self.cmap.setItemText(13, _translate("MainWindow", "Wistia"))
        self.cmap.setItemText(14, _translate("MainWindow", "afmhot"))
        self.cmap.setItemText(15, _translate("MainWindow", "gist_heat"))
        self.Settings.setTabText(self.Settings.indexOf(self.settings), _translate("MainWindow", "Settings"))
        self.groupBox.setTitle(_translate("MainWindow", "Total"))
        self.total_length_label.setText(_translate("MainWindow", "Length"))
        self.total_length.setPlaceholderText(_translate("MainWindow", "no current data"))
        self.total_volume_label.setText(_translate("MainWindow", "Volume"))
        self.total_volume.setPlaceholderText(_translate("MainWindow", "no current data"))
        self.total_mass.setPlaceholderText(_translate("MainWindow", "no current data"))
        self.total_mass_volume.setText(_translate("MainWindow", "Mass"))
        self.total_cost_label.setText(_translate("MainWindow", "Cost"))
        self.total_cost.setPlaceholderText(_translate("MainWindow", "no current data"))
        self.runBox.setTitle(_translate("MainWindow", "Run"))
        self.apply_button.setText(_translate("MainWindow", "Apply"))
        self.optimize_button.setText(_translate("MainWindow", "Optimize"))
        self.plotBox.setTabText(self.plotBox.indexOf(self.unoptimizedPlot), _translate("MainWindow", "Unoptimized"))
        self.plotBox.setTabText(self.plotBox.indexOf(self.optimizedPlot), _translate("MainWindow", "Optimized"))
        self.clear_button.setText(_translate("MainWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.console_output), _translate("MainWindow", "Console"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fem_output), _translate("MainWindow", "FEM"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.debug_output), _translate("MainWindow", "Debug"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionReport_bug.setText(_translate("MainWindow", "Report Bug"))
        self.actionRecently_Edited.setText(_translate("MainWindow", "Open Recent"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout_Qt.setText(_translate("MainWindow", "About Qt"))
