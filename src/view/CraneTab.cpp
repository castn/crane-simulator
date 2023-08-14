#include <QLabel>
#include <QSplitter>

#include "CraneTab.h"
#include "src/util/widget.h"
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

std::tuple<int, int, int, int> CraneTab::getTowerSettings() {
    return leftSide->getTowerSettings();
}

std::tuple<int, int, int, int, bool, bool> CraneTab::getJibSettings() {
    return leftSide->getJibSettings();
}

std::tuple<int, int, int, int> CraneTab::getCounterjibSettings() {
    return leftSide->getCounterjibSettings();
}
