//
// Created by carsten on 29.07.23.
//

#include "crane.h"
#include "node.h"
#include "beam.h"

Crane::Crane(double towerHeight, double towerWidth, int towerNumSegs, int towerSupStyle,
             double jibLength, double jibHeight, int jibNumSegs, int jibSupStyle, bool jibDrop, bool jibBend,
             double cjLength, double cjHeight, int cjNumSegs, int cjSupStyle) {
    tower = new Tower(towerHeight, towerWidth, towerNumSegs, towerSupStyle);
    jib = new Jib(jibLength, jibHeight, jibNumSegs, jibSupStyle, jibDrop, jibBend);
    counterjib = new Counterjib(cjLength, cjHeight, cjNumSegs, cjSupStyle);
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
void Crane::setTowerDimensions(double towerHeight, double towerWidth, int towerSegs,
                               int towerSupStyle) {
    tower->updateDimensions(towerHeight, towerWidth, towerSegs, towerSupStyle);
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
void Crane::setJibDimensions(double jibLength, double jibHeight, int jibNumSegs, int jibSupStyle,
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
void Crane::setCounterjibDimensions(double cjLength, double cjHeight, int cjNumSegs, int cjSupStyle) {
    counterjib->updateDimensions(cjLength, cjHeight, cjNumSegs, cjSupStyle);
}