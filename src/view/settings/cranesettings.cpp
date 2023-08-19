#include <QLabel>
#include <tuple>
#include "cranesettings.h"
#include "mainwindow.h"
#include "util/widget.h"


CraneSettings::CraneSettings(Crane &crane, QWidget *parent) : QWidget(parent) {
    settingsLayout = new QVBoxLayout(this);

    // Tower
    auto *towerGroup = new QGroupBox(this);
    towerGroup->setTitle("Tower");

    auto *towerLayout = new QGridLayout(this);
    towerHeight = new QSpinBox(this);
    towerHeight->setMaximum(10000);
    towerHeight->setSuffix(" mm");
    towerHeight->setValue(2000);
    Widget::createGridRow(towerLayout, 0, "Height", "This is a tooltip!", towerHeight, this);
    towerWidth = new QSpinBox(this);
    towerWidth->setSuffix(" mm");
    towerWidth->setMaximum(2000);
    towerWidth->setValue(1000);
    Widget::createGridRow(towerLayout, 1, "Width", "This is a tooltip!", towerWidth, this);
    towerSegments = new QSpinBox(this);
    towerSegments->setValue(2);
    Widget::createGridRow(towerLayout, 2, "Segments", "This is a tooltip!", towerSegments, this);
    towerSupportType = new QComboBox(this);
    towerSupportType->addItems({"Cross", "Zigzag", "Diagonal"});
    Widget::createGridRow(towerLayout, 3, "Support Type", "This is a tooltip!", towerSupportType, this);

    // We need to call QOverload due to Qt5 overloading valueChanged(), this deprecated and is fixed in Qt6
    connect(towerHeight, QOverload<int>::of(&QSpinBox::valueChanged), &crane, &Crane::updateTowerHeight);
    connect(towerWidth, QOverload<int>::of(&QSpinBox::valueChanged), &crane, &Crane::updateTowerWidth);
    connect(towerSegments, QOverload<int>::of(&QSpinBox::valueChanged), &crane, &Crane::updateTowerSegments);
    connect(towerSupportType, QOverload<int>::of(&QComboBox::currentIndexChanged), &crane, &Crane::updateTowerSupportType);

    towerGroup->setLayout(towerLayout);
    settingsLayout->addWidget(towerGroup);

    // Jib
    auto *jibGroup = new QGroupBox(this);
    jibGroup->setTitle("Jib");

    auto *jibLayout = new QGridLayout(this);
    jibLength = new QSpinBox(this);
    jibLength->setMaximum(10000);
    jibLength->setSuffix(" mm");
    jibLength->setValue(2000);
    Widget::createGridRow(jibLayout, 0, "Length", "This is a tooltip!", jibLength, this);
    jibHeight = new QSpinBox(this);
    jibHeight->setMaximum(2000);
    jibHeight->setSuffix(" mm");
    jibHeight->setValue(1000);
    Widget::createGridRow(jibLayout, 1, "Height", "This is a tooltip!", jibHeight, this);
    jibSegments = new QSpinBox(this);
    jibSegments->setValue(2);
    Widget::createGridRow(jibLayout, 2, "Segments", "This is a tooltip!", jibSegments, this);
    jibSupportType = new QComboBox(this);
    jibSupportType->addItems({"Truss", "Set-back Truss"});
    Widget::createGridRow(jibLayout, 3, "Support Type", "This is a tooltip!", jibSupportType, this);
    heightDropdown = new QCheckBox(this);
    heightDropdown->setText("Realistic decrease in height of support");
    jibLayout->addWidget(heightDropdown, 4, 0);
    upwardBend = new QCheckBox(this);
    upwardBend->setText("Realistic upward bend");
    jibLayout->addWidget(upwardBend, 5, 0);

    jibGroup->setLayout(jibLayout);
    settingsLayout->addWidget(jibGroup);

    // Counterjib
    auto *counterjibGroup = new QGroupBox(this);
    counterjibGroup->setTitle("Counter Jib");

    auto *counterJibLayout = new QGridLayout(this);
    counterjibLength = new QSpinBox(this);
    counterjibLength->setMaximum(10000);
    counterjibLength->setSuffix(" mm");
    counterjibLength->setValue(1000);
    Widget::createGridRow(counterJibLayout, 0, "Length", "This is a tooltip!", counterjibLength, this);
    counterjibHeight = new QSpinBox(this);
    counterjibHeight->setMaximum(2000);
    counterjibHeight->setSuffix(" mm");
    counterjibHeight->setValue(800);
    Widget::createGridRow(counterJibLayout, 1, "Width", "This is a tooltip!", counterjibHeight, this);
    counterjibSegments = new QSpinBox(this);
    counterjibSegments->setValue(1);
    Widget::createGridRow(counterJibLayout, 2, "Segments", "This is a tooltip!", counterjibSegments, this);
    counterjibSupportType = new QComboBox(this);
    counterjibSupportType->addItems({"Truss", "Tower"});
    Widget::createGridRow(counterJibLayout, 3, "Support Type", "This is a tooltip!", counterjibSupportType, this);

    counterjibGroup->setLayout(counterJibLayout);
    settingsLayout->addWidget(counterjibGroup);

    // Add stretch between groups and button
    settingsLayout->addStretch(3);

    // Apply button
    applyButton = new QPushButton("Apply", this);
    applyButton->resize(200, 50);

    settingsLayout->addWidget(applyButton);
}

std::tuple<int, int, int, int> CraneSettings::getTowerSettings() {
    return std::make_tuple(0, 0, 0, 0);
}

std::tuple<int, int, int, int, bool, bool> CraneSettings::getJibSettings() {
    return std::make_tuple(0, 0, 0, 0, false, false);
}

std::tuple<int, int, int, int> CraneSettings::getCounterjibSettings() {
    return std::make_tuple(0, 0, 0, 0);
}

void CraneSettings::connectApply() {
    //connect(applyButton, &QPushButton::released, this, SLOT(&MainWindow::handleApply));
}
