//
// Created by carsten on 29.07.23.
//

#ifndef MAINWINDOW_CRANE_H
#define MAINWINDOW_CRANE_H

#include "tower.h"
#include "jib.h"
#include "counterjib.h"
#include "node.h"
#include "beam.h"

class Crane {
public:
    Crane(double towerHeight, double towerWidth, int towerNumSegs, int towerSupStyle,
          double jibLength, double jibHeight, int jibNumSegs, int jibSupStyle,
          bool jibDrop, bool jibBend, double cjLength, double cjHeight, int cjNumSegs, int cjSupStyle);
    Tower *tower = nullptr;
    Jib *jib = nullptr;
    Counterjib *counterjib = nullptr;
    void createCrane();
private:
    // Everything related to tower
    void createTower();
    std::vector<Node> getTowerNodes();
    std::vector<Beam> getTowerBeams();
    double getTowerLength();
    void setTowerDimensions(double towerHeight, double towerWidth, int towerNumSegs,
                            int towerSupStyle);
    // Everything related to jib
    void createJib();
    std::vector<Node> getJibNodes();
    std::vector<Beam> getJibBeams();
    double getJibLength();
    void setJibDimensions(double jibLength, double jibHeight, int jibNumSegs, int jibSupStyle,
                          bool jibDrop, bool jibBend);
    // Everything realted to counterjib
    void createCounterjib();
    std::vector<Node> getCounterjibNodes();
    std::vector<Beam> getCounterjibBeams();
    double getCounterjibLength();
    void setCounterjibDimensions(double cjLength, double cjHeight, int cjNumSegs, int cjSupStyle);
};

#endif //MAINWINDOW_CRANE_H
