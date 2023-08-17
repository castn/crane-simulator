#include "maincontent.h"
#include "view/settings/cranesettings.h"
#include "src/view/render/renderer.h"

MainContent::MainContent(QWidget *parent) : QWidget(parent) {
    mainLayout = new QGridLayout(this);
    mainLayout->setContentsMargins(0, 0, 0, 0);
    mainLayout->setSpacing(0);


    auto *settings = new QTabWidget(this);
    settings->setTabPosition(QTabWidget::TabPosition::West);
    settings->setSizePolicy(QSizePolicy::Minimum, QSizePolicy::Expanding);
    settings->addTab(new CraneSettings(this), "Settings");

    mainLayout->addWidget(settings, 0,0);

    renderer = new QTabWidget(this);
    renderer->setTabsClosable(true);
    //craneTab = new CraneTab(this);
    renderer->addTab(new Renderer(this), "test");

    mainLayout->addWidget(renderer, 0,1);
}

void MainContent::createNewCrane(const QString &name) {
    renderer->addTab(new Renderer(this), name);

}

std::tuple<double, double, int, int> MainContent::getTowerSettings() {
    return std::make_tuple(0, 0, 0, 0);
}

std::tuple<double, double, int, int, bool, bool> MainContent::getJibSettings() {
    return std::make_tuple(0, 0, 0, 0, false, false);
}

std::tuple<double, double, int, int> MainContent::getCounterjibSettings() {
    return std::make_tuple(0, 0, 0, 0);
}
