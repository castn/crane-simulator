//
// Created by carsten on 28.07.23.
//

#include <QLabel>
#include <QSplitter>

#include "CraneTab.h"
#include "src/widget.h"
#include "LeftSide.h"
#include "RightSide.h"

CraneTab::CraneTab(QWidget *parent) : QWidget(parent) {
    tabLayout = new QVBoxLayout(this);
    auto *splitter = new QSplitter(this);

    leftSide = new LeftSide(this);
    splitter->addWidget(leftSide);

    rightSide = new RightSide(this);
    splitter->addWidget(rightSide);

    tabLayout->addWidget(splitter);
}

std::tuple<double, double, int, int> CraneTab::getTowerSettings() {
    return leftSide->getTowerSettings();
}

std::tuple<double, double, int, int, bool, bool> CraneTab::getJibSettings() {
    return leftSide->getJibSettings();
}

std::tuple<double, double, int, int> CraneTab::getCounterjibSettings() {
    return leftSide->getCounterjibSettings();
}
