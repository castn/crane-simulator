//
// Created by castn on 01.08.23.
//

#include <QGridLayout>
#include "jibsettings.h"
#include "src/widget.h"

JibSettings::JibSettings(QWidget *parent) : QWidget(parent) {
    jibSettings = new QGroupBox(this);
    jibSettings->setTitle("Jib");

    jibSettings->setLayout(createSettings());
}

QLayout *JibSettings::createSettings() {
    auto *layout = new QGridLayout(this);

    jibLength = new QSpinBox(this);
    jibLength->setSuffix(" mm");
    Widget::createGridRow(layout, 0, "Length", "This is a tooltip!", jibLength, this);

    jibHeight = new QSpinBox(this);
    jibHeight->setSuffix(" mm");
    Widget::createGridRow(layout, 1, "Height", "This is a tooltip!", jibHeight, this);

    jibSegments = new QSpinBox(this);
    jibSegments->setSuffix(" mm");
    Widget::createGridRow(layout, 2, "Segments", "This is a tooltip!", jibSegments, this);

    jibSupportType = new QComboBox(this);
    jibSupportType->addItems({"Set-back Truss", "Truss"});
    Widget::createGridRow(layout, 3, "Support Type", "This is a tooltip!", jibSupportType, this);

    heightDegrease = new QCheckBox(this);
    heightDegrease->setText("Realistic decrease in height of support");
    layout->addWidget(heightDegrease, 4, 0);

    upwardBend = new QCheckBox(this);
    upwardBend->setText("Realistic upward bend");
    layout->addWidget(upwardBend, 5, 0);


    return layout;
}
