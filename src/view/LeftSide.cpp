#include <QLabel>
#include <tuple>
#include "LeftSide.h"
#include "src/view/settings/towersettings.h"
#include "src/view/settings/counterjibsettings.h"
#include "src/view/settings/jibsettings.h"
#include "mainwindow.h"


LeftSide::LeftSide(QWidget *parent) : QWidget(parent) {
    leftLayout = new QVBoxLayout(this);

    towerSettings = new TowerSettings(this);
    jibSettings = new JibSettings(this);
    counterjibSettings = new CounterjibSettings(this);

    applyButton = new QPushButton("Apply", this);
    applyButton->resize(200, 50);

    leftLayout->addWidget(towerSettings);
    leftLayout->addWidget(jibSettings);
    leftLayout->addWidget(counterjibSettings);
    leftLayout->addWidget(applyButton);
}

std::tuple<int, int, int, int> LeftSide::getTowerSettings() {
    return std::make_tuple(towerSettings->getHeight(), towerSettings->getWidth(), towerSettings->getSegs(),
                           towerSettings->getSupType());
}

std::tuple<int, int, int, int, bool, bool> LeftSide::getJibSettings() {
    return std::make_tuple(jibSettings->getLength(), jibSettings->getHeight(), jibSettings->getSegs(),
                           jibSettings->getSupType(), jibSettings->getDropdown(), jibSettings->getBend());
}

std::tuple<int, int, int, int> LeftSide::getCounterjibSettings() {
    return std::make_tuple(counterjibSettings->getLength(), counterjibSettings->getHeight(),
                           counterjibSettings->getSegs(), counterjibSettings->getSupType());
}

void LeftSide::connectApply() {
    //connect(applyButton, &QPushButton::released, this, SLOT(&MainWindow::handleApply));
}
