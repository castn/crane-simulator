#include "CentralWidget.h"
#include "CraneTab.h"

CentralWidget::CentralWidget(QWidget *parent) : QWidget(parent){
    centralLayout = new QVBoxLayout(this);
    centralLayout->setContentsMargins(0, 0, 0, 0);
    centralLayout->setSpacing(0);

    tabs = new QTabWidget(this);
    tabs->setTabsClosable(true);
    craneTab = new CraneTab(this);
    tabs->addTab(craneTab, "test");

    centralLayout->addWidget(tabs);
}

void CentralWidget::createNewCrane(const QString& name) {
    tabs->addTab(new CraneTab(this), name);

}

std::tuple<double, double, int, int> CentralWidget::getTowerSettings() {
    return craneTab->getTowerSettings();
}

std::tuple<double, double, int, int, bool, bool> CentralWidget::getJibSettings() {
    return craneTab->getJibSettings();
}

std::tuple<double, double, int, int> CentralWidget::getCounterjibSettings() {
    return craneTab->getCounterjibSettings();
}
