//
// Created by carsten on 30.07.23.
//

#include <QLabel>
#include "LeftSide.h"
#include "src/view/settings/towersettings.h"
#include "src/view/settings/counterjibsettings.h"
#include "src/view/settings/jibsettings.h"

LeftSide::LeftSide(QWidget *parent) : QWidget(parent) {
    leftLayout = new QVBoxLayout(this);

    leftLayout->addWidget(new TowerSettings(this));
    leftLayout->addWidget(new JibSettings(this));
    leftLayout->addWidget(new CounterJibSettings(this));


}
