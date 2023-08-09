#ifndef MAINWINDOW_TOWER_H
#define MAINWINDOW_TOWER_H

#include <vector>
#include "beam.h"


enum class TowerStyle {
    NONE = 0,
    CROSS = 1,
    ZIGZAG = 2,
    DIAGONAL = 3
};

class Tower {
public:
    // Dimension getters and setters
    double getHeight();
    double getWidth();
    double getSegments();
    double getTotalBeamLength();
    double getLongestBeam();
    double getTotalHeight();
    std::vector<std::vector<double>> getNodes();
    std::vector<Beam> getBeams();
    void setHeight(double height);
    void setWidth(double width);
    void setSegments(double numberOfSegments);
    void setDimensions(double height, double width, int numSegs, int supStyle);
    void create(bool hasHorizontal, bool isHollow);
private:
    // Tower dimensions
    double height = 0;
    double width = 0;
    double numberOfSegments = 0;
    double totalLength = 0;
    double longestBeam = 0;
    TowerStyle supStyle = TowerStyle::NONE;

    // Creates nodes
    void createNodesPerSegment(double elevation);
    // Creates beams
    void createSegments(bool hasHorizontal, bool isHollow);
    void createBeamsPerSegment(int seg, bool hasHorizontal, bool isHollow);
    void createHorizontalBeams(double valToAdd);
    void createVerticalBeams(double valToAdd);
    void createDiagonalBeams(double valToAdd);
    void createCrossFaceBeam(double valToAdd);
    void createZigzagFaceBeams(double valToAdd);
    void createParallelFaceBeamsLR(double valToAdd);
    void createParallelFaceBeamsRL(double valToAdd);
    void appendBeam(int startNode, int endNode);
};


#endif //MAINWINDOW_TOWER_H
