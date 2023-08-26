#include "maincontent.h"
#include "view/settings/cranesettings.h"
#include "src/view/render/renderer.h"

MainContent::MainContent(Crane &crane, QWidget *parent) : QWidget(parent) {
    mainLayout = new QGridLayout(this);
    mainLayout->setContentsMargins(0, 0, 0, 0);
    mainLayout->setSpacing(0);


    auto *settings = new QTabWidget(this);
    settings->setTabPosition(QTabWidget::TabPosition::West);
    settings->setSizePolicy(QSizePolicy::Minimum, QSizePolicy::Expanding);

    auto *craneSettings = new CraneSettings(crane, this);
    this->craneSettings = craneSettings;
    settings->addTab(craneSettings, "Settings");

    mainLayout->addWidget(settings, 0, 0);

    auto locRenderer = new QTabWidget(this);
    locRenderer->setTabsClosable(true);
    //craneTab = new CraneTab(this);
    renderer = new Renderer(this);
    locRenderer->addTab(renderer, "untitled");

    mainLayout->addWidget(locRenderer, 0, 1);
}

void MainContent::createNewCrane(const QString &name) {
    //renderer->addTab(new Renderer(this), name);
    Crane *crane = new Crane();
    auto towerDims = craneSettings->getTowerSettings();
    auto jibDims = craneSettings->getJibSettings();
    auto cjDims = craneSettings->getCounterjibSettings();
    crane->updateDimensions(std::get<0>(towerDims), std::get<1>(towerDims), std::get<2>(towerDims), std::get<3>(towerDims),
                            std::get<0>(jibDims), std::get<1>(jibDims), std::get<2>(jibDims), std::get<3>(jibDims), std::get<4>(jibDims), std::get<5>(jibDims),
                            std::get<0>(cjDims), std::get<1>(cjDims), std::get<2>(cjDims), std::get<3>(cjDims));
    crane->createCrane();

    renderer->setBeamsToRender(crane->getBeams());
    renderer->createBeamPlot();
}

std::tuple<int, int, int, int> MainContent::getTowerSettings() {
    return craneSettings->getTowerSettings();
}

std::tuple<int, int, int, int, bool, bool> MainContent::getJibSettings() {
    return craneSettings->getJibSettings();
}

std::tuple<int, int, int, int> MainContent::getCounterjibSettings() {
    return craneSettings->getCounterjibSettings();
}
