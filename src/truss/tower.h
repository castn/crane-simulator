//
// Created by castn on 29.07.23.
//

#ifndef MAINWINDOW_TOWER_H
#define MAINWINDOW_TOWER_H


class Tower {
public:
    double getTowerHeight();
    double getTowerWidth();
    double getTowerSegments();
    void setTowerHeight(double height);
    void setTowerWidth(double width);
    void setTowerSegments(double numberOfSegments);
    void createSegments();
    void createNodesPerSegment(double elevation);
private:
    double height = 0;
    double width = 0;
    double numberOfSegments = 0;
};


#endif //MAINWINDOW_TOWER_H
