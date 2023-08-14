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

    counterjibLength = new QSpinBox(this);
    counterjibLength->setMaximum(10000);
    counterjibLength->setSuffix(" mm");
    counterjibLength->setValue(1000);
    Widget::createGridRow(layout, 0, "Length", "This is a tooltip!", counterjibLength, this);

    counterjibHeight = new QSpinBox(this);
    counterjibHeight->setMaximum(2000);
    counterjibHeight->setSuffix(" mm");
    counterjibHeight->setValue(800);
    Widget::createGridRow(layout, 1, "Width", "This is a tooltip!", counterjibHeight, this);

    counterjibSegments = new QSpinBox(this);
    counterjibSegments->setValue(1);
    Widget::createGridRow(layout, 2, "Segments", "This is a tooltip!", counterjibSegments, this);

    counterjibSupportType = new QComboBox(this);
    counterjibSupportType->addItems({"Truss", "Tower"});
    Widget::createGridRow(layout, 3, "Support Type", "This is a tooltip!", counterjibSupportType, this);

    return layout;
}

int CounterjibSettings::getLength() {
    return counterjibLength->value();
}

int CounterjibSettings::getHeight() {
    return counterjibHeight->value();
}

int CounterjibSettings::getSegs() {
    return counterjibSegments->value();
}

int CounterjibSettings::getSupType() {
    return counterjibSupportType->currentIndex();
}
