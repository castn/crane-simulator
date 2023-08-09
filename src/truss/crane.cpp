//
// Created by carsten on 29.07.23.
//

#include "crane.h"
#include "beam.h"

Crane::Crane() {
    tower = new Tower();
    jib = new Jib();
    counterjib = new Counterjib();
}


void Crane::createTower() {
    tower->create(true, true);
}
std::vector<std::vector<double>> Crane::getTowerNodes() {
    return tower->getNodes();
}
std::vector<Beam> Crane::getTowerBeams() {
    return tower->getBeams();
}
double Crane::getTowerLength() {
    return tower->getTotalBeamLength();
}
void Crane::setTowerDimensions(double towerHeight, double towerWidth, int towerNumSegs,
                               int towerSupStyle) {
    tower->setDimensions(towerHeight, towerWidth, towerNumSegs, towerSupStyle);
}

void Crane::createJib() {
    jib->create(getTowerNodes(), getTowerBeams(), tower->getHeight(), tower->getWidth());
}
std::vector<std::vector<double>> Crane::getJibNodes() {
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
    jib->setDimensions(jibLength, jibHeight, jibNumSegs, jibSupStyle, jibDrop, jibBend);
}

void Crane::createCounterjib() {
    counterjib->create(getJibNodes(), getJibBeams(), tower->getHeight(), tower->getWidth(),
                                 getTowerNodes().size(), jib->getSegments(), jib->getSupportStyle(), jib->getHeight());
}
std::vector<std::vector<double>> Crane::getCounterjibNodes() {
    return counterjib->getNodes();
}
std::vector<Beam> Crane::getCounterjibBeams() {
    return counterjib->getBeams();
}
double Crane::getCounterjibLength() {
    return counterjib->getTotalBeamLength();
}
void Crane::setCounterjibDimensions(double cjLength, double cjHeight, int cjNumSegs, int cjSupStyle) {
    counterjib->setDimensions(cjLength, cjHeight, cjNumSegs, cjSupStyle);
}