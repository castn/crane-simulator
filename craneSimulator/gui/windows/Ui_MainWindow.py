# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QSplitter, QStatusBar, QTabWidget, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1022, 1325)
        icon = QIcon()
        icon.addFile(u"../../../resources/images/crane.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionReport_bug = QAction(MainWindow)
        self.actionReport_bug.setObjectName(u"actionReport_bug")
        self.actionRecently_Edited = QAction(MainWindow)
        self.actionRecently_Edited.setObjectName(u"actionRecently_Edited")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout_Qt = QAction(MainWindow)
        self.actionAbout_Qt.setObjectName(u"actionAbout_Qt")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.options = QGroupBox(self.centralwidget)
        self.options.setObjectName(u"options")
        self.options.setFlat(False)
        self.verticalLayout_3 = QVBoxLayout(self.options)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Settings = QTabWidget(self.options)
        self.Settings.setObjectName(u"Settings")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Settings.sizePolicy().hasHeightForWidth())
        self.Settings.setSizePolicy(sizePolicy)
        self.crane = QWidget()
        self.crane.setObjectName(u"crane")
        self.verticalLayout_4 = QVBoxLayout(self.crane)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.towerBox = QGroupBox(self.crane)
        self.towerBox.setObjectName(u"towerBox")
        self.towerBox.setCheckable(False)
        self.formLayout = QFormLayout(self.towerBox)
        self.formLayout.setObjectName(u"formLayout")
        self.towerHeight_label = QLabel(self.towerBox)
        self.towerHeight_label.setObjectName(u"towerHeight_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.towerHeight_label)

        self.towerHeight_spinbox = QSpinBox(self.towerBox)
        self.towerHeight_spinbox.setObjectName(u"towerHeight_spinbox")
        self.towerHeight_spinbox.setMinimum(1)
        self.towerHeight_spinbox.setMaximum(1000000)
        self.towerHeight_spinbox.setValue(10000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.towerHeight_spinbox)

        self.towerWidth_label = QLabel(self.towerBox)
        self.towerWidth_label.setObjectName(u"towerWidth_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.towerWidth_label)

        self.towerWidth_spinbox = QSpinBox(self.towerBox)
        self.towerWidth_spinbox.setObjectName(u"towerWidth_spinbox")
        self.towerWidth_spinbox.setMinimum(1)
        self.towerWidth_spinbox.setMaximum(1000000)
        self.towerWidth_spinbox.setValue(1200)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.towerWidth_spinbox)

        self.towerSegment_label = QLabel(self.towerBox)
        self.towerSegment_label.setObjectName(u"towerSegment_label")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.towerSegment_label)

        self.towerSupportType_label = QLabel(self.towerBox)
        self.towerSupportType_label.setObjectName(u"towerSupportType_label")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.towerSupportType_label)

        self.towerSupportType_comboBox = QComboBox(self.towerBox)
        self.towerSupportType_comboBox.addItem("")
        self.towerSupportType_comboBox.addItem("")
        self.towerSupportType_comboBox.addItem("")
        self.towerSupportType_comboBox.setObjectName(u"towerSupportType_comboBox")
        self.towerSupportType_comboBox.setAutoFillBackground(False)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.towerSupportType_comboBox)

        self.towerSegment_spinbox = QSpinBox(self.towerBox)
        self.towerSegment_spinbox.setObjectName(u"towerSegment_spinbox")
        self.towerSegment_spinbox.setMinimum(1)
        self.towerSegment_spinbox.setMaximum(1000000)
        self.towerSegment_spinbox.setValue(7)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.towerSegment_spinbox)


        self.verticalLayout_4.addWidget(self.towerBox)

        self.jibBox = QGroupBox(self.crane)
        self.jibBox.setObjectName(u"jibBox")
        self.jibBox.setCheckable(False)
        self.formLayout_2 = QFormLayout(self.jibBox)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.jibLength_label = QLabel(self.jibBox)
        self.jibLength_label.setObjectName(u"jibLength_label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.jibLength_label)

        self.jibLength_spinBox = QSpinBox(self.jibBox)
        self.jibLength_spinBox.setObjectName(u"jibLength_spinBox")
        self.jibLength_spinBox.setMinimum(1)
        self.jibLength_spinBox.setMaximum(1000000)
        self.jibLength_spinBox.setValue(10000)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.jibLength_spinBox)

        self.jibHeight_label = QLabel(self.jibBox)
        self.jibHeight_label.setObjectName(u"jibHeight_label")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.jibHeight_label)

        self.jibHeight_spinBox = QSpinBox(self.jibBox)
        self.jibHeight_spinBox.setObjectName(u"jibHeight_spinBox")
        self.jibHeight_spinBox.setMinimum(1)
        self.jibHeight_spinBox.setMaximum(1000000)
        self.jibHeight_spinBox.setValue(1000)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.jibHeight_spinBox)

        self.jibSegment_label = QLabel(self.jibBox)
        self.jibSegment_label.setObjectName(u"jibSegment_label")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.jibSegment_label)

        self.jibSegment_spinBox = QSpinBox(self.jibBox)
        self.jibSegment_spinBox.setObjectName(u"jibSegment_spinBox")
        self.jibSegment_spinBox.setMinimum(1)
        self.jibSegment_spinBox.setMaximum(1000000)
        self.jibSegment_spinBox.setValue(7)

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.jibSegment_spinBox)

        self.jibSupportType_label = QLabel(self.jibBox)
        self.jibSupportType_label.setObjectName(u"jibSupportType_label")

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.jibSupportType_label)

        self.jibSupportType_comboBox = QComboBox(self.jibBox)
        self.jibSupportType_comboBox.addItem("")
        self.jibSupportType_comboBox.addItem("")
        self.jibSupportType_comboBox.setObjectName(u"jibSupportType_comboBox")

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.jibSupportType_comboBox)

        self.jibBend = QCheckBox(self.jibBox)
        self.jibBend.setObjectName(u"jibBend")
        self.jibBend.setChecked(True)

        self.formLayout_2.setWidget(11, QFormLayout.SpanningRole, self.jibBend)

        self.jibSupportHalfDrop = QCheckBox(self.jibBox)
        self.jibSupportHalfDrop.setObjectName(u"jibSupportHalfDrop")
        self.jibSupportHalfDrop.setChecked(True)

        self.formLayout_2.setWidget(10, QFormLayout.SpanningRole, self.jibSupportHalfDrop)


        self.verticalLayout_4.addWidget(self.jibBox)

        self.counterJibBox = QGroupBox(self.crane)
        self.counterJibBox.setObjectName(u"counterJibBox")
        self.counterJibBox.setCheckable(False)
        self.formLayout_3 = QFormLayout(self.counterJibBox)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.counterJibLength_label = QLabel(self.counterJibBox)
        self.counterJibLength_label.setObjectName(u"counterJibLength_label")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.counterJibLength_label)

        self.counterJibLength_spinBox = QSpinBox(self.counterJibBox)
        self.counterJibLength_spinBox.setObjectName(u"counterJibLength_spinBox")
        self.counterJibLength_spinBox.setMinimum(1)
        self.counterJibLength_spinBox.setMaximum(1000000)
        self.counterJibLength_spinBox.setValue(4000)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.counterJibLength_spinBox)

        self.counterJibHeight_label = QLabel(self.counterJibBox)
        self.counterJibHeight_label.setObjectName(u"counterJibHeight_label")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.counterJibHeight_label)

        self.counterJibHeight_spinBox = QSpinBox(self.counterJibBox)
        self.counterJibHeight_spinBox.setObjectName(u"counterJibHeight_spinBox")
        self.counterJibHeight_spinBox.setMinimum(1)
        self.counterJibHeight_spinBox.setMaximum(1000000)
        self.counterJibHeight_spinBox.setValue(600)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.counterJibHeight_spinBox)

        self.counterJibSupportType_label = QLabel(self.counterJibBox)
        self.counterJibSupportType_label.setObjectName(u"counterJibSupportType_label")

        self.formLayout_3.setWidget(9, QFormLayout.LabelRole, self.counterJibSupportType_label)

        self.counterJibSegments_label = QLabel(self.counterJibBox)
        self.counterJibSegments_label.setObjectName(u"counterJibSegments_label")

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.counterJibSegments_label)

        self.counterJibSegments_spinBox = QSpinBox(self.counterJibBox)
        self.counterJibSegments_spinBox.setObjectName(u"counterJibSegments_spinBox")
        self.counterJibSegments_spinBox.setMinimum(1)
        self.counterJibSegments_spinBox.setMaximum(1000000)
        self.counterJibSegments_spinBox.setValue(3)

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.counterJibSegments_spinBox)

        self.counterJibSupportType_comboBox = QComboBox(self.counterJibBox)
        self.counterJibSupportType_comboBox.addItem("")
        self.counterJibSupportType_comboBox.addItem("")
        self.counterJibSupportType_comboBox.setObjectName(u"counterJibSupportType_comboBox")

        self.formLayout_3.setWidget(9, QFormLayout.FieldRole, self.counterJibSupportType_comboBox)


        self.verticalLayout_4.addWidget(self.counterJibBox)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.current_as_comparison_base = QPushButton(self.crane)
        self.current_as_comparison_base.setObjectName(u"current_as_comparison_base")

        self.verticalLayout_4.addWidget(self.current_as_comparison_base)

        self.Settings.addTab(self.crane, "")
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.verticalLayout_6 = QVBoxLayout(self.settings)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.enable_gravity = QCheckBox(self.settings)
        self.enable_gravity.setObjectName(u"enable_gravity")
        self.enable_gravity.setChecked(True)

        self.verticalLayout_6.addWidget(self.enable_gravity)

        self.wind_settings = QGroupBox(self.settings)
        self.wind_settings.setObjectName(u"wind_settings")
        self.wind_settings.setCheckable(True)
        self.wind_settings.setChecked(True)
        self.formLayout_7 = QFormLayout(self.wind_settings)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.direction_label = QLabel(self.wind_settings)
        self.direction_label.setObjectName(u"direction_label")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.direction_label)

        self.wind_direction = QComboBox(self.wind_settings)
        self.wind_direction.addItem("")
        self.wind_direction.addItem("")
        self.wind_direction.addItem("")
        self.wind_direction.addItem("")
        self.wind_direction.setObjectName(u"wind_direction")

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.wind_direction)

        self.wind_force_label = QLabel(self.wind_settings)
        self.wind_force_label.setObjectName(u"wind_force_label")

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.wind_force_label)

        self.wind_force = QDoubleSpinBox(self.wind_settings)
        self.wind_force.setObjectName(u"wind_force")
        self.wind_force.setMaximum(50.000000000000000)
        self.wind_force.setValue(50.000000000000000)

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.wind_force)


        self.verticalLayout_6.addWidget(self.wind_settings)

        self.fem_settings = QGroupBox(self.settings)
        self.fem_settings.setObjectName(u"fem_settings")
        self.fem_settings.setEnabled(True)
        self.fem_settings.setCheckable(False)
        self.formLayout_6 = QFormLayout(self.fem_settings)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.multiplier_label = QLabel(self.fem_settings)
        self.multiplier_label.setObjectName(u"multiplier_label")

        self.formLayout_6.setWidget(4, QFormLayout.LabelRole, self.multiplier_label)

        self.multiplierSpinBox = QSpinBox(self.fem_settings)
        self.multiplierSpinBox.setObjectName(u"multiplierSpinBox")
        self.multiplierSpinBox.setMinimum(1)
        self.multiplierSpinBox.setMaximum(100)
        self.multiplierSpinBox.setValue(1)

        self.formLayout_6.setWidget(4, QFormLayout.FieldRole, self.multiplierSpinBox)

        self.lable_jib_left = QLabel(self.fem_settings)
        self.lable_jib_left.setObjectName(u"lable_jib_left")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.lable_jib_left)

        self.label_jib_right = QLabel(self.fem_settings)
        self.label_jib_right.setObjectName(u"label_jib_right")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_jib_right)

        self.label_counter_jib_left = QLabel(self.fem_settings)
        self.label_counter_jib_left.setObjectName(u"label_counter_jib_left")

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.label_counter_jib_left)

        self.label_counter_jib_right = QLabel(self.fem_settings)
        self.label_counter_jib_right.setObjectName(u"label_counter_jib_right")

        self.formLayout_6.setWidget(3, QFormLayout.LabelRole, self.label_counter_jib_right)

        self.jib_left_spinBox = QDoubleSpinBox(self.fem_settings)
        self.jib_left_spinBox.setObjectName(u"jib_left_spinBox")
        self.jib_left_spinBox.setMinimum(-250.000000000000000)
        self.jib_left_spinBox.setMaximum(0.000000000000000)
        self.jib_left_spinBox.setValue(-250.000000000000000)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.jib_left_spinBox)

        self.jib_right_spinBox = QDoubleSpinBox(self.fem_settings)
        self.jib_right_spinBox.setObjectName(u"jib_right_spinBox")
        self.jib_right_spinBox.setMinimum(-250.000000000000000)
        self.jib_right_spinBox.setMaximum(0.000000000000000)
        self.jib_right_spinBox.setValue(-250.000000000000000)

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.jib_right_spinBox)

        self.counterjib_left_spinBox = QDoubleSpinBox(self.fem_settings)
        self.counterjib_left_spinBox.setObjectName(u"counterjib_left_spinBox")
        self.counterjib_left_spinBox.setMinimum(-250.000000000000000)
        self.counterjib_left_spinBox.setMaximum(0.000000000000000)
        self.counterjib_left_spinBox.setValue(-250.000000000000000)

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.counterjib_left_spinBox)

        self.counterjib_right_spinBox = QDoubleSpinBox(self.fem_settings)
        self.counterjib_right_spinBox.setObjectName(u"counterjib_right_spinBox")
        self.counterjib_right_spinBox.setMinimum(-250.000000000000000)
        self.counterjib_right_spinBox.setMaximum(0.000000000000000)
        self.counterjib_right_spinBox.setValue(-250.000000000000000)

        self.formLayout_6.setWidget(3, QFormLayout.FieldRole, self.counterjib_right_spinBox)


        self.verticalLayout_6.addWidget(self.fem_settings)

        self.ignore_specification = QCheckBox(self.settings)
        self.ignore_specification.setObjectName(u"ignore_specification")

        self.verticalLayout_6.addWidget(self.ignore_specification)

        self.axial_coloring = QGroupBox(self.settings)
        self.axial_coloring.setObjectName(u"axial_coloring")
        self.axial_coloring.setCheckable(True)
        self.formLayout_8 = QFormLayout(self.axial_coloring)
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.cmap_label = QLabel(self.axial_coloring)
        self.cmap_label.setObjectName(u"cmap_label")

        self.formLayout_8.setWidget(1, QFormLayout.LabelRole, self.cmap_label)

        self.cmap = QComboBox(self.axial_coloring)
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
        self.cmap.setObjectName(u"cmap")

        self.formLayout_8.setWidget(1, QFormLayout.FieldRole, self.cmap)


        self.verticalLayout_6.addWidget(self.axial_coloring)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.Settings.addTab(self.settings, "")

        self.verticalLayout_3.addWidget(self.Settings)


        self.gridLayout.addWidget(self.options, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout_5 = QFormLayout(self.groupBox)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.total_length_label = QLabel(self.groupBox)
        self.total_length_label.setObjectName(u"total_length_label")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.total_length_label)

        self.total_length = QLineEdit(self.groupBox)
        self.total_length.setObjectName(u"total_length")
        self.total_length.setReadOnly(True)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.total_length)

        self.total_volume_label = QLabel(self.groupBox)
        self.total_volume_label.setObjectName(u"total_volume_label")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.total_volume_label)

        self.total_volume = QLineEdit(self.groupBox)
        self.total_volume.setObjectName(u"total_volume")
        self.total_volume.setReadOnly(True)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.total_volume)

        self.total_mass = QLineEdit(self.groupBox)
        self.total_mass.setObjectName(u"total_mass")
        self.total_mass.setReadOnly(True)

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.total_mass)

        self.total_mass_volume = QLabel(self.groupBox)
        self.total_mass_volume.setObjectName(u"total_mass_volume")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.total_mass_volume)

        self.total_cost_label = QLabel(self.groupBox)
        self.total_cost_label.setObjectName(u"total_cost_label")

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.total_cost_label)

        self.total_cost = QLineEdit(self.groupBox)
        self.total_cost.setObjectName(u"total_cost")
        self.total_cost.setReadOnly(True)

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.total_cost)


        self.gridLayout.addWidget(self.groupBox, 3, 0, 1, 1)

        self.runBox = QGroupBox(self.centralwidget)
        self.runBox.setObjectName(u"runBox")
        self.verticalLayout_5 = QVBoxLayout(self.runBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.apply_button = QPushButton(self.runBox)
        self.apply_button.setObjectName(u"apply_button")
        self.apply_button.setCheckable(False)

        self.verticalLayout_5.addWidget(self.apply_button)

        self.progressBar = QProgressBar(self.runBox)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)

        self.verticalLayout_5.addWidget(self.progressBar)


        self.gridLayout.addWidget(self.runBox, 5, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 0, 1, 1)


        self.formLayout_4.setLayout(0, QFormLayout.LabelRole, self.gridLayout)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy1)
        self.splitter.setOrientation(Qt.Vertical)
        self.plotBox = QTabWidget(self.splitter)
        self.plotBox.setObjectName(u"plotBox")
        sizePolicy1.setHeightForWidth(self.plotBox.sizePolicy().hasHeightForWidth())
        self.plotBox.setSizePolicy(sizePolicy1)
        self.unoptimizedPlot = QWidget()
        self.unoptimizedPlot.setObjectName(u"unoptimizedPlot")
        self.verticalLayout_10 = QVBoxLayout(self.unoptimizedPlot)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.unoptimized_plot_layout = QVBoxLayout()
        self.unoptimized_plot_layout.setObjectName(u"unoptimized_plot_layout")
        self.unoptimized_no_data_label = QLabel(self.unoptimizedPlot)
        self.unoptimized_no_data_label.setObjectName(u"unoptimized_no_data_label")

        self.unoptimized_plot_layout.addWidget(self.unoptimized_no_data_label, 0, Qt.AlignHCenter)


        self.verticalLayout_10.addLayout(self.unoptimized_plot_layout)

        self.plotBox.addTab(self.unoptimizedPlot, "")
        self.optimizedPlot = QWidget()
        self.optimizedPlot.setObjectName(u"optimizedPlot")
        self.verticalLayout_7 = QVBoxLayout(self.optimizedPlot)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.optimize_plot_layout = QVBoxLayout()
        self.optimize_plot_layout.setObjectName(u"optimize_plot_layout")
        self.optimized_no_data_label = QLabel(self.optimizedPlot)
        self.optimized_no_data_label.setObjectName(u"optimized_no_data_label")

        self.optimize_plot_layout.addWidget(self.optimized_no_data_label, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addLayout(self.optimize_plot_layout)

        self.plotBox.addTab(self.optimizedPlot, "")
        self.diff_plot = QWidget()
        self.diff_plot.setObjectName(u"diff_plot")
        self.verticalLayout = QVBoxLayout(self.diff_plot)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.diff_plot_layout = QVBoxLayout()
        self.diff_plot_layout.setObjectName(u"diff_plot_layout")
        self.diff_no_data_label = QLabel(self.diff_plot)
        self.diff_no_data_label.setObjectName(u"diff_no_data_label")

        self.diff_plot_layout.addWidget(self.diff_no_data_label, 0, Qt.AlignHCenter)


        self.verticalLayout.addLayout(self.diff_plot_layout)

        self.plotBox.addTab(self.diff_plot, "")
        self.splitter.addWidget(self.plotBox)
        self.tabWidget = QTabWidget(self.splitter)
        self.tabWidget.setObjectName(u"tabWidget")
        self.console_output = QWidget()
        self.console_output.setObjectName(u"console_output")
        self.verticalLayout_9 = QVBoxLayout(self.console_output)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.output = QPlainTextEdit(self.console_output)
        self.output.setObjectName(u"output")
        self.output.setReadOnly(True)

        self.verticalLayout_9.addWidget(self.output)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.clear_button = QPushButton(self.console_output)
        self.clear_button.setObjectName(u"clear_button")

        self.horizontalLayout.addWidget(self.clear_button)


        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.console_output, "")
        self.fem_output = QWidget()
        self.fem_output.setObjectName(u"fem_output")
        self.horizontalLayout_3 = QHBoxLayout(self.fem_output)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.fem_unoptimized_treeWidget = QTreeWidget(self.fem_output)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.fem_unoptimized_treeWidget.setHeaderItem(__qtreewidgetitem)
        self.fem_unoptimized_treeWidget.setObjectName(u"fem_unoptimized_treeWidget")

        self.horizontalLayout_3.addWidget(self.fem_unoptimized_treeWidget)

        self.fem_optimized_treeWidget = QTreeWidget(self.fem_output)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"1");
        self.fem_optimized_treeWidget.setHeaderItem(__qtreewidgetitem1)
        self.fem_optimized_treeWidget.setObjectName(u"fem_optimized_treeWidget")

        self.horizontalLayout_3.addWidget(self.fem_optimized_treeWidget)

        self.tabWidget.addTab(self.fem_output, "")
        self.debug_output = QWidget()
        self.debug_output.setObjectName(u"debug_output")
        self.horizontalLayout_2 = QHBoxLayout(self.debug_output)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.debug_unoptimized_treeWidget = QTreeWidget(self.debug_output)
        __qtreewidgetitem2 = QTreeWidgetItem()
        __qtreewidgetitem2.setText(0, u"1");
        self.debug_unoptimized_treeWidget.setHeaderItem(__qtreewidgetitem2)
        self.debug_unoptimized_treeWidget.setObjectName(u"debug_unoptimized_treeWidget")
        self.debug_unoptimized_treeWidget.header().setVisible(True)
        self.debug_unoptimized_treeWidget.header().setCascadingSectionResizes(True)
        self.debug_unoptimized_treeWidget.header().setHighlightSections(False)
        self.debug_unoptimized_treeWidget.header().setProperty("showSortIndicator", False)
        self.debug_unoptimized_treeWidget.header().setStretchLastSection(True)

        self.horizontalLayout_2.addWidget(self.debug_unoptimized_treeWidget)

        self.debug_optimized_treeWidget = QTreeWidget(self.debug_output)
        __qtreewidgetitem3 = QTreeWidgetItem()
        __qtreewidgetitem3.setText(0, u"1");
        self.debug_optimized_treeWidget.setHeaderItem(__qtreewidgetitem3)
        self.debug_optimized_treeWidget.setObjectName(u"debug_optimized_treeWidget")

        self.horizontalLayout_2.addWidget(self.debug_optimized_treeWidget)

        self.tabWidget.addTab(self.debug_output, "")
        self.diff_output = QWidget()
        self.diff_output.setObjectName(u"diff_output")
        self.horizontalLayout_4 = QHBoxLayout(self.diff_output)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.comparison_base_treeWidget = QTreeWidget(self.diff_output)
        __qtreewidgetitem4 = QTreeWidgetItem()
        __qtreewidgetitem4.setText(0, u"1");
        self.comparison_base_treeWidget.setHeaderItem(__qtreewidgetitem4)
        self.comparison_base_treeWidget.setObjectName(u"comparison_base_treeWidget")

        self.horizontalLayout_4.addWidget(self.comparison_base_treeWidget)

        self.current_treeWidget = QTreeWidget(self.diff_output)
        __qtreewidgetitem5 = QTreeWidgetItem()
        __qtreewidgetitem5.setText(0, u"1");
        self.current_treeWidget.setHeaderItem(__qtreewidgetitem5)
        self.current_treeWidget.setObjectName(u"current_treeWidget")

        self.horizontalLayout_4.addWidget(self.current_treeWidget)

        self.tabWidget.addTab(self.diff_output, "")
        self.splitter.addWidget(self.tabWidget)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.splitter)


        self.verticalLayout_2.addLayout(self.formLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1022, 19))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.jibLength_spinBox, self.jibHeight_spinBox)
        QWidget.setTabOrder(self.jibHeight_spinBox, self.counterJibLength_spinBox)
        QWidget.setTabOrder(self.counterJibLength_spinBox, self.counterJibHeight_spinBox)
        QWidget.setTabOrder(self.counterJibHeight_spinBox, self.clear_button)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menu_File.addAction(self.actionOpen)
        self.menu_File.addAction(self.actionRecently_Edited)
        self.menu_File.addAction(self.actionSave)
        self.menu_File.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionReport_bug)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAbout_Qt)

        self.retranslateUi(MainWindow)
        self.clear_button.clicked.connect(self.output.clear)

        self.Settings.setCurrentIndex(0)
        self.apply_button.setDefault(False)
        self.plotBox.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionReport_bug.setText(QCoreApplication.translate("MainWindow", u"Report Bug", None))
        self.actionRecently_Edited.setText(QCoreApplication.translate("MainWindow", u"Open Recent", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionAbout_Qt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
        self.options.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.towerBox.setTitle(QCoreApplication.translate("MainWindow", u"Tower", None))
        self.towerHeight_label.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.towerHeight_spinbox.setSuffix(QCoreApplication.translate("MainWindow", u" mm", None))
        self.towerWidth_label.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.towerWidth_spinbox.setSuffix(QCoreApplication.translate("MainWindow", u" mm", None))
        self.towerSegment_label.setText(QCoreApplication.translate("MainWindow", u"Segments", None))
        self.towerSupportType_label.setText(QCoreApplication.translate("MainWindow", u"Support Type", None))
        self.towerSupportType_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Zigzag", None))
        self.towerSupportType_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Cross", None))
        self.towerSupportType_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Diagonal", None))

        self.towerSupportType_comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"Zigzag", None))
        self.jibBox.setTitle(QCoreApplication.translate("MainWindow", u"Jib", None))
        self.jibLength_label.setText(QCoreApplication.translate("MainWindow", u"Length", None))
        self.jibLength_spinBox.setSuffix(QCoreApplication.translate("MainWindow", u" mm", None))
        self.jibHeight_label.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.jibHeight_spinBox.setSuffix(QCoreApplication.translate("MainWindow", u" mm", None))
        self.jibSegment_label.setText(QCoreApplication.translate("MainWindow", u"Segments", None))
        self.jibSupportType_label.setText(QCoreApplication.translate("MainWindow", u"Support Type", None))
        self.jibSupportType_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Set-back truss", None))
        self.jibSupportType_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Truss", None))

        self.jibSupportType_comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"Set-back truss", None))
        self.jibBend.setText(QCoreApplication.translate("MainWindow", u"Realistic upward bend", None))
        self.jibSupportHalfDrop.setText(QCoreApplication.translate("MainWindow", u"Realistic decrease in height of support", None))
        self.counterJibBox.setTitle(QCoreApplication.translate("MainWindow", u"Counter Jib", None))
        self.counterJibLength_label.setText(QCoreApplication.translate("MainWindow", u"Length", None))
        self.counterJibLength_spinBox.setSuffix(QCoreApplication.translate("MainWindow", u" mm", None))
        self.counterJibHeight_label.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.counterJibHeight_spinBox.setSuffix(QCoreApplication.translate("MainWindow", u" mm", None))
        self.counterJibSupportType_label.setText(QCoreApplication.translate("MainWindow", u"Support Type", None))
        self.counterJibSegments_label.setText(QCoreApplication.translate("MainWindow", u"Segments", None))
        self.counterJibSupportType_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Truss", None))
        self.counterJibSupportType_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Tower", None))

        self.counterJibSupportType_comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"Truss", None))
        self.current_as_comparison_base.setText(QCoreApplication.translate("MainWindow", u"Make current as comparison base", None))
        self.Settings.setTabText(self.Settings.indexOf(self.crane), QCoreApplication.translate("MainWindow", u"Crane", None))
        self.enable_gravity.setText(QCoreApplication.translate("MainWindow", u"Gravity", None))
        self.wind_settings.setTitle(QCoreApplication.translate("MainWindow", u"Horizontal Force", None))
        self.direction_label.setText(QCoreApplication.translate("MainWindow", u"Direction", None))
        self.wind_direction.setItemText(0, QCoreApplication.translate("MainWindow", u"Front", None))
        self.wind_direction.setItemText(1, QCoreApplication.translate("MainWindow", u"Left", None))
        self.wind_direction.setItemText(2, QCoreApplication.translate("MainWindow", u"Right", None))
        self.wind_direction.setItemText(3, QCoreApplication.translate("MainWindow", u"Back", None))

        self.wind_force_label.setText(QCoreApplication.translate("MainWindow", u"Force", None))
        self.wind_force.setSuffix(QCoreApplication.translate("MainWindow", u" kN", None))
        self.fem_settings.setTitle(QCoreApplication.translate("MainWindow", u"FEM", None))
        self.multiplier_label.setText(QCoreApplication.translate("MainWindow", u"Multiplier", None))
        self.lable_jib_left.setText(QCoreApplication.translate("MainWindow", u"Jib Left", None))
        self.label_jib_right.setText(QCoreApplication.translate("MainWindow", u"Jib Right", None))
        self.label_counter_jib_left.setText(QCoreApplication.translate("MainWindow", u"Counter Jib Left", None))
        self.label_counter_jib_right.setText(QCoreApplication.translate("MainWindow", u"Counter Jib Right", None))
        self.jib_left_spinBox.setPrefix("")
        self.jib_left_spinBox.setSuffix(QCoreApplication.translate("MainWindow", u" kN", None))
        self.jib_right_spinBox.setSuffix(QCoreApplication.translate("MainWindow", u" kN", None))
        self.counterjib_left_spinBox.setSuffix(QCoreApplication.translate("MainWindow", u" kN", None))
        self.counterjib_right_spinBox.setSuffix(QCoreApplication.translate("MainWindow", u" kN", None))
        self.ignore_specification.setText(QCoreApplication.translate("MainWindow", u"Ignore specifications of the project task", None))
        self.axial_coloring.setTitle(QCoreApplication.translate("MainWindow", u"Axial forces visibility", None))
        self.cmap_label.setText(QCoreApplication.translate("MainWindow", u"Color Map", None))
        self.cmap.setItemText(0, QCoreApplication.translate("MainWindow", u"jet", None))
        self.cmap.setItemText(1, QCoreApplication.translate("MainWindow", u"copper", None))
        self.cmap.setItemText(2, QCoreApplication.translate("MainWindow", u"hot", None))
        self.cmap.setItemText(3, QCoreApplication.translate("MainWindow", u"viridis", None))
        self.cmap.setItemText(4, QCoreApplication.translate("MainWindow", u"plasma", None))
        self.cmap.setItemText(5, QCoreApplication.translate("MainWindow", u"inferno", None))
        self.cmap.setItemText(6, QCoreApplication.translate("MainWindow", u"magma", None))
        self.cmap.setItemText(7, QCoreApplication.translate("MainWindow", u"cividis", None))
        self.cmap.setItemText(8, QCoreApplication.translate("MainWindow", u"spring", None))
        self.cmap.setItemText(9, QCoreApplication.translate("MainWindow", u"summer", None))
        self.cmap.setItemText(10, QCoreApplication.translate("MainWindow", u"autumn", None))
        self.cmap.setItemText(11, QCoreApplication.translate("MainWindow", u"winter", None))
        self.cmap.setItemText(12, QCoreApplication.translate("MainWindow", u"cool", None))
        self.cmap.setItemText(13, QCoreApplication.translate("MainWindow", u"Wistia", None))
        self.cmap.setItemText(14, QCoreApplication.translate("MainWindow", u"afmhot", None))
        self.cmap.setItemText(15, QCoreApplication.translate("MainWindow", u"gist_heat", None))

        self.Settings.setTabText(self.Settings.indexOf(self.settings), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Total", None))
        self.total_length_label.setText(QCoreApplication.translate("MainWindow", u"Length", None))
        self.total_length.setPlaceholderText(QCoreApplication.translate("MainWindow", u"no current data", None))
        self.total_volume_label.setText(QCoreApplication.translate("MainWindow", u"Volume", None))
        self.total_volume.setPlaceholderText(QCoreApplication.translate("MainWindow", u"no current data", None))
        self.total_mass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"no current data", None))
        self.total_mass_volume.setText(QCoreApplication.translate("MainWindow", u"Mass", None))
        self.total_cost_label.setText(QCoreApplication.translate("MainWindow", u"Cost", None))
        self.total_cost.setPlaceholderText(QCoreApplication.translate("MainWindow", u"no current data", None))
        self.runBox.setTitle(QCoreApplication.translate("MainWindow", u"Run", None))
        self.apply_button.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.unoptimized_no_data_label.setText(QCoreApplication.translate("MainWindow", u"No available data. Click Apply to plot the crane defined via the Options", None))
        self.plotBox.setTabText(self.plotBox.indexOf(self.unoptimizedPlot), QCoreApplication.translate("MainWindow", u"Unoptimized", None))
        self.optimized_no_data_label.setText(QCoreApplication.translate("MainWindow", u"No available data. Click Apply to plot the crane defined via the Options", None))
        self.plotBox.setTabText(self.plotBox.indexOf(self.optimizedPlot), QCoreApplication.translate("MainWindow", u"Optimized", None))
        self.diff_no_data_label.setText(QCoreApplication.translate("MainWindow", u"No available data. Click Apply to plot the crane defined via the Options", None))
        self.plotBox.setTabText(self.plotBox.indexOf(self.diff_plot), QCoreApplication.translate("MainWindow", u"Diff", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.console_output), QCoreApplication.translate("MainWindow", u"Console", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fem_output), QCoreApplication.translate("MainWindow", u"FEM", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.debug_output), QCoreApplication.translate("MainWindow", u"Debug", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.diff_output), QCoreApplication.translate("MainWindow", u"Diff", None))
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"&Help", None))
    # retranslateUi

