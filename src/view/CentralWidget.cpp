//
// Created by carsten on 28.07.23.
//

#include "CentralWidget.h"
#include "CraneTab.h"

CentralWidget::CentralWidget(QWidget *parent) : QWidget(parent){
    centralLayout = new QVBoxLayout(this);
    centralLayout->setContentsMargins(0, 0, 0, 0);
    centralLayout->setSpacing(0);

    tabs = new QTabWidget(this);
    tabs->setTabsClosable(true);
    tabs->addTab(new CraneTab(this), "test");

    centralLayout->addWidget(tabs);
}

void CentralWidget::createNewCrane(const QString& name) {
    tabs->addTab(new CraneTab(this), name);

}
