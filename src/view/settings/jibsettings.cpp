#include <QGridLayout>
#include "jibsettings.h"
#include "src/util/widget.h"

JibSettings::JibSettings(QWidget *parent) : QWidget(parent) {
    jibSettings = new QGroupBox(this);
    jibSettings->setTitle("Jib");

    jibSettings->setLayout(createSettings());
}

QLayout *JibSettings::createSettings() {
    auto *layout = new QGridLayout(this);

    jibLength = new QSpinBox(this);
    jibLength->setMaximum(10000);
    jibLength->setSuffix(" mm");
    jibLength->setValue(2000);
    Widget::createGridRow(layout, 0, "Length", "This is a tooltip!", jibLength, this);

    jibHeight = new QSpinBox(this);
    jibHeight->setMaximum(2000);
    jibHeight->setSuffix(" mm");
    jibHeight->setValue(1000);
    Widget::createGridRow(layout, 1, "Height", "This is a tooltip!", jibHeight, this);

    jibSegments = new QSpinBox(this);
    jibSegments->setValue(2);
    Widget::createGridRow(layout, 2, "Segments", "This is a tooltip!", jibSegments, this);

    jibSupportType = new QComboBox(this);
    jibSupportType->addItems({"Truss", "Set-back Truss"});
    Widget::createGridRow(layout, 3, "Support Type", "This is a tooltip!", jibSupportType, this);

    heightDropdown = new QCheckBox(this);
    heightDropdown->setText("Realistic decrease in height of support");
    layout->addWidget(heightDropdown, 4, 0);

    upwardBend = new QCheckBox(this);
    upwardBend->setText("Realistic upward bend");
    layout->addWidget(upwardBend, 5, 0);


    return layout;
}

int JibSettings::getLength() {
    return jibLength->value();
}

int JibSettings::getHeight() {
    return jibHeight->value();
}

int JibSettings::getSegs() {
    return jibSegments->value();
}

int JibSettings::getSupType() {
    return jibSupportType->currentIndex() + 1;
}

bool JibSettings::getDropdown() {
    return heightDropdown->isChecked();
}

bool JibSettings::getBend() {
    return upwardBend->isChecked();
}
