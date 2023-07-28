//
// Created by carsten on 28.07.23.
//

#include <QLabel>
#include <QVBoxLayout>
#include "CraneTab.h"

CraneTab::CraneTab(QWidget *parent) : QWidget(parent) {
    tabLayout = new QVBoxLayout(this);
    tabLayout->setContentsMargins(0, 0, 0, 0);
    tabLayout->setSpacing(0);

    auto *test = new QLabel("A");
    tabLayout->addWidget(test);
}
