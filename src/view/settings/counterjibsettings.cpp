//
// Created by carsten on 30.07.23.
//

#include <QGridLayout>
#include "counterjibsettings.h"
#include "src/widget.h"

CounterJibSettings::CounterJibSettings(QWidget *parent) : QWidget(parent) {
    counterjibSettings = new QGroupBox(this);
    counterjibSettings->setTitle("Tower");

    counterjibSettings->setLayout(createSettings());
}

QLayout *CounterJibSettings::createSettings() {
    auto *layout = new QGridLayout(this);

    counterjibLength = new QSpinBox(this);
    counterjibLength->setSuffix(" mm");
    Widget::createGridRow(layout, 0, "Length", "This is a tooltip!", counterjibLength, this);

    counterjibWidth = new QSpinBox(this);
    counterjibWidth->setSuffix(" mm");
    Widget::createGridRow(layout, 1, "Width", "This is a tooltip!", counterjibWidth, this);

    counterjibSegments = new QSpinBox(this);
    counterjibSegments->setSuffix(" mm");
    Widget::createGridRow(layout, 2, "Segments", "This is a tooltip!", counterjibSegments, this);

    counterjibSupportType = new QComboBox(this);
    counterjibSupportType->addItems({"Truss", "Tower"});
    Widget::createGridRow(layout, 3, "Support Type", "This is a tooltip!", counterjibSupportType, this);

    return layout;
}
