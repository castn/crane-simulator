//
// Created by carsten on 28.07.23.
//

#include <QLabel>

#include "CraneTab.h"
#include "src/widget.h"
#include "LeftSide.h"
#include "RightSide.h"

CraneTab::CraneTab(QWidget *parent) : QWidget(parent) {
    tabLayout = new QGridLayout(this);

    auto *leftSide = new LeftSide(this);
    tabLayout->addWidget(leftSide, 0, 0);

    auto *rightSide = new RightSide(this);
    tabLayout->addWidget(rightSide, 0, 1);

}
