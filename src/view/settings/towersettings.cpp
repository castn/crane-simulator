//
// Created by carsten on 30.07.23.
//

#include "towersettings.h"
#include "src/widget.h"

TowerSettings::TowerSettings(QWidget *parent) : QWidget(parent) {
    towerSettings = new QGroupBox(this);
    towerSettings->setTitle("Tower");

    towerSettings->setLayout(createSettings());
}

QLayout *TowerSettings::createSettings() {
    auto *layout = new QGridLayout(this);

    towerHeight = new QSpinBox(this);
    towerHeight->setSuffix(" mm");
    Widget::createGridRow(layout, 0, "Heigt", "This is a tooltip!", towerHeight, this);

    towerWidth = new QSpinBox(this);
    towerWidth->setSuffix(" mm");
    Widget::createGridRow(layout, 1, "Width", "This is a tooltip!", towerWidth, this);

    towerSegments = new QSpinBox(this);
    towerSegments->setSuffix(" mm");
    Widget::createGridRow(layout, 2, "Segments", "This is a tooltip!", towerSegments, this);

    towerSupportType = new QComboBox(this);
    towerSupportType->addItems({"Zigzag", "Cross", "Diagonal"});
    Widget::createGridRow(layout, 3, "Support Type", "This is a tooltip!", towerSupportType, this);

    return layout;
}
