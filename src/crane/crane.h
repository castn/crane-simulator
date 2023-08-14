//
// Created by carsten on 29.07.23.
//

#ifndef MAINWINDOW_CRANE_H
#define MAINWINDOW_CRANE_H


#include "crane/truss/tower.h"
#include "crane/truss/jib.h"
#include "crane/truss/counterjib.h"

class Crane {
public:
    Crane();

    Tower *tower = nullptr;
    Jib *jib = nullptr;
    Counterjib *counterjib = nullptr;

    void updateDimensions(int towerHeight, int towerWidth, int towerNumSegs, int towerSupStyle,
                          int jibLength, int jibHeight, int jibNumSegs, int jibSupStyle,
                          bool jibDrop, bool jibBend, int cjLength, int cjHeight, int cjNumSegs, int cjSupStyle);
    void createCrane();
private:
    // Everything related to tower
    void createTower();
    std::vector<Node> getTowerNodes();
    std::vector<Beam> getTowerBeams();
    double getTowerLength();
    void updateTowerDimensions(int towerHeight, int towerWidth, int towerNumSegs, int towerSupStyle);
    // Everything related to jib
    void createJib();
    std::vector<Node> getJibNodes();
    std::vector<Beam> getJibBeams();
    double getJibLength();
    void updateJibDimensions(int jibLength, int jibHeight, int jibNumSegs, int jibSupStyle,
                             bool jibDrop, bool jibBend);
    // Everything realted to counterjib
    void createCounterjib();
    std::vector<Node> getCounterjibNodes();
    std::vector<Beam> getCounterjibBeams();
    double getCounterjibLength();
    void updateCounterjibDimensions(int cjLength, int cjHeight, int cjNumSegs, int cjSupStyle);
};

#endif //MAINWINDOW_CRANE_H
