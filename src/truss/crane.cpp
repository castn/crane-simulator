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
    tower->createTower(true, true);
}
std::vector<std::vector<double>> Crane::getTowerNodes() {
    return tower->getTowerNodes();
}
std::vector<Beam> Crane::getTowerBeams() {
    return tower->getTowerBeams();
}
double Crane::getTowerLength() {
    return tower->getTowerTotalBeamLength();
}
void Crane::setTowerDimensions(double towerHeight, double towerWidth, int towerNumSegs,
                               int towerSupStyle) {
    tower->setDimensions(towerHeight, towerWidth, towerNumSegs, towerSupStyle);
}

void Crane::createJib() {
    jib->createJib(getTowerNodes(), getTowerBeams(), tower->getTowerHeight(), tower->getTowerWidth());
}
std::vector<std::vector<double>> Crane::getJibNodes() {
    return jib->getJibNodes();
}
std::vector<Beam> Crane::getJibBeams() {
    return jib->getJibBeams();
}
double Crane::getJibLength() {
    return jib->getJibTotalBeamLength();
}
void Crane::setJibDimensions(double jibLength, double jibHeight, int jibNumSegs, int jibSupStyle,
                      bool jibDrop, bool jibBend) {
    jib->setDimensions(jibLength, jibHeight, jibNumSegs, jibSupStyle, jibDrop, jibBend);
}