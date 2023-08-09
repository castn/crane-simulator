//
// Created by carsten on 29.07.23.
//

#ifndef MAINWINDOW_CRANE_H
#define MAINWINDOW_CRANE_H


#include "tower.h"
#include "jib.h"
#include "counterjib.h"
#include "beam.h"

class Crane {
public:
    Crane();
    Tower *tower = nullptr;
    Jib *jib = nullptr;
    Counterjib *counterjib = nullptr;
private:
    // Everything related to tower
    void createTower();
    std::vector<std::vector<double>> getTowerNodes();
    std::vector<Beam> getTowerBeams();
    double getTowerLength();
    void setTowerDimensions(double towerHeight, double towerWidth, int towerNumSegs,
                            int towerSupStyle);
    // Everything related to jib
    void createJib();
    std::vector<std::vector<double>> getJibNodes();
    std::vector<Beam> getJibBeams();
    double getJibLength();
    void setJibDimensions(double jibLength, double jibHeight, int jibNumSegs, int jibSupStyle,
                          bool jibDrop, bool jibBend);
    // Everything realted to counterjib
    void createCounterjib();
    std::vector<std::vector<double>> getCounterjibNodes();
    std::vector<Beam> getCounterjibBeams();
    double getCounterjibLength();
    void setCounterjibDimensions();
};


#endif //MAINWINDOW_CRANE_H
