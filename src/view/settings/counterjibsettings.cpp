//
// Created by carsten on 30.07.23.
//

#include <QGridLayout>
#include "counterjibsettings.h"
#include "src/util/widget.h"

CounterjibSettings::CounterjibSettings(QWidget *parent) : QWidget(parent) {
    counterjibSettings = new QGroupBox(this);
    counterjibSettings->setTitle("Counter Jib");

    counterjibSettings->setLayout(createSettings());
}

QLayout *CounterjibSettings::createSettings() {
    auto *layout = new QGridLayout(this);

    counterjibLength = new QDoubleSpinBox(this);
    counterjibLength->setSuffix(" mm");
    Widget::createGridRow(layout, 0, "Length", "This is a tooltip!", counterjibLength, this);

    counterjibWidth = new QDoubleSpinBox(this);
    counterjibWidth->setSuffix(" mm");
    Widget::createGridRow(layout, 1, "Width", "This is a tooltip!", counterjibWidth, this);

    counterjibSegments = new QSpinBox(this);
//    counterjibSegments->setSuffix(" mm");
    Widget::createGridRow(layout, 2, "Segments", "This is a tooltip!", counterjibSegments, this);

    counterjibSupportType = new QComboBox(this);
    counterjibSupportType->addItems({"Truss", "Tower"});
    Widget::createGridRow(layout, 3, "Support Type", "This is a tooltip!", counterjibSupportType, this);

    return layout;
}

double CounterjibSettings::getLength() {
    return counterjibLength->value();
}

double CounterjibSettings::getWidth() {
    return counterjibWidth->value();
}

int CounterjibSettings::getSegs() {
    return counterjibSegments->value();
}

int CounterjibSettings::getSupType() {
    return counterjibSupportType->currentIndex();
}
