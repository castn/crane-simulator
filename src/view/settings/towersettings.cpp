#include "towersettings.h"
#include "src/util/widget.h"

TowerSettings::TowerSettings(QWidget *parent) : QWidget(parent) {
    towerSettings = new QGroupBox(this);
    towerSettings->setTitle("Tower");

    towerSettings->setLayout(createSettings());
}

QLayout *TowerSettings::createSettings() {
    auto *layout = new QGridLayout(this);

    towerHeight = new QSpinBox(this);
    towerHeight->setMaximum(10000);
    towerHeight->setSuffix(" mm");
    towerHeight->setValue(2000);
    Widget::createGridRow(layout, 0, "Heigt", "This is a tooltip!", towerHeight, this);

    towerWidth = new QSpinBox(this);
    towerWidth->setSuffix(" mm");
    towerWidth->setMaximum(2000);
    towerWidth->setValue(1000);
    Widget::createGridRow(layout, 1, "Width", "This is a tooltip!", towerWidth, this);

    towerSegments = new QSpinBox(this);
    towerSegments->setValue(2);
    Widget::createGridRow(layout, 2, "Segments", "This is a tooltip!", towerSegments, this);

    towerSupportType = new QComboBox(this);
    towerSupportType->addItems({"Cross", "Zigzag", "Diagonal"});
    Widget::createGridRow(layout, 3, "Support Type", "This is a tooltip!", towerSupportType, this);

    return layout;
}

int TowerSettings::getHeight() {
    return towerHeight->value();
}

int TowerSettings::getWidth() {
    return towerWidth->value();
}

int TowerSettings::getSegs() {
    return towerSegments->value();
}

int TowerSettings::getSupType() {
    return towerSupportType->currentIndex() + 1;
}
