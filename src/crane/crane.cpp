#include <iostream>
#include "crane.h"


Crane::Crane() {
    // Crane(0, 0, 0, 0, 0, 0, 0, 0, false, false, 0, 0, 0, 0);
    tower = new Tower(0, 0, 0, 0);
    jib = new Jib(0, 0, 0, 0, false, false);
    counterjib = new Counterjib(0, 0, 0, 0);
}

void Crane::updateDimensions(int towerHeight, int towerWidth, int towerNumSegs, int towerSupStyle,
                             int jibLength, int jibHeight, int jibNumSegs, int jibSupStyle, bool jibDrop, bool jibBend,
                             int cjLength, int cjHeight, int cjNumSegs, int cjSupStyle) {
    // tower = new Tower(towerHeight, towerWidth, towerNumSegs, towerSupStyle);
    // jib = new Jib(jibLength, jibHeight, jibNumSegs, jibSupStyle, jibDrop, jibBend);
    // counterjib = new Counterjib(cjLength, cjHeight, cjNumSegs, cjSupStyle);
    updateTowerDimensions(towerHeight, towerWidth, towerNumSegs, towerSupStyle);
    updateJibDimensions(jibLength, jibHeight, jibNumSegs, jibSupStyle, jibDrop, jibBend);
    updateCounterjibDimensions(cjLength, cjHeight, cjNumSegs, cjSupStyle);
}

void Crane::createCrane() {
    createTower();
    createJib();
    createCounterjib();
}

// Methods relating to the tower
void Crane::createTower() {
    tower->create(true, true);
}
std::vector<Node> Crane::getTowerNodes() {
    return tower->getNodes();
}
std::vector<Beam> Crane::getTowerBeams() {
    return tower->getBeams();
}
double Crane::getTowerLength() {
    return tower->getTotalBeamLength();
}
void Crane::updateTowerDimensions(int towerHeight, int towerWidth, int towerSegs,
                                  int towerSupStyle) {
    tower->updateDimensions(towerHeight, towerWidth, towerSegs, towerSupStyle);
}

void Crane::updateTowerHeight(int height) {
    tower->setHeight(height);
    std::cout << "new height to 9";
}

// Methods relating to the jib
void Crane::createJib() {
    jib->create(getTowerNodes(), getTowerBeams(), tower->getHeight(), tower->getWidth());
}
std::vector<Node> Crane::getJibNodes() {
    return jib->getNodes();
}
std::vector<Beam> Crane::getJibBeams() {
    return jib->getBeams();
}
double Crane::getJibLength() {
    return jib->getTotalBeamLength();
}
void Crane::updateJibDimensions(int jibLength, int jibHeight, int jibNumSegs, int jibSupStyle,
                                bool jibDrop, bool jibBend) {
    jib->updateDimensions(jibLength, jibHeight, jibNumSegs, jibSupStyle, jibDrop, jibBend);
}

// Methods relating to the counterjib
void Crane::createCounterjib() {
    counterjib->create(getJibNodes(), getJibBeams(), tower->getHeight(), tower->getWidth(),
                       getTowerNodes().size(), jib->getSegments(), jib->getSupportStyle(), jib->getHeight());
}
std::vector<Node> Crane::getCounterjibNodes() {
    return counterjib->getNodes();
}
std::vector<Beam> Crane::getCounterjibBeams() {
    return counterjib->getBeams();
}
double Crane::getCounterjibLength() {
    return counterjib->getTotalBeamLength();
}
void Crane::updateCounterjibDimensions(int cjLength, int cjHeight, int cjNumSegs, int cjSupStyle) {
    counterjib->updateDimensions(cjLength, cjHeight, cjNumSegs, cjSupStyle);
}
