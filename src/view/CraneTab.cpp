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

    auto *leftSide = new LeftSide(this);
    splitter->addWidget(leftSide);

    auto *rightSide = new RightSide(this);
    splitter->addWidget(rightSide);

    tabLayout->addWidget(splitter);

}
