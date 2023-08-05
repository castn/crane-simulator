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
    void createSegments(bool hasHorizontal, bool isHollow);
    void createNodesPerSegment(double elevation);
    void createBeamsPerSegment(int seg, bool hasHorizontal, bool isHollow);
    void createHorizontalBeams(double valToAdd);
    void appendBeam(int startNode, int endNode);
    void createVerticalBeams(double valToAdd);
    void createDiagonalBeams(double valToAdd);
    void createCrossFaceBeam(double valToAdd);
    void createZigzagFaceBeams(double valToAdd);
    void createParallelFaceBeamsLR(double valToAdd);
    void createParallelFaceBeamsRL(double valToAdd);
private:
    double height = 0;
    double width = 0;
    double numberOfSegments = 0;
    double totalLength = 0;
    double longestBeam = 0;
    int faceStyle = 0;
};


#endif //MAINWINDOW_TOWER_H
