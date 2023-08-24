#ifndef MAINWINDOW_TOWER_H
#define MAINWINDOW_TOWER_H

#include "src/crane/truss/components/node.h"
#include "src/crane/truss/components/beam.h"
#include <vector>


enum class TowerStyle {
    NONE = 0,
    CROSS = 1,
    ZIGZAG = 2,
    DIAGONAL = 3
};

class Tower {
public:
    Tower(int height, int width, int segments, int supStyle);
    // Dimension getters and setters
    int getHeight();
    int getWidth();
    int getSegments();
    double getTotalBeamLength();
    double getLongestBeam();
    int getTotalHeight();
    std::vector<Node> getNodes();
    std::vector<Beam> getBeams();
    void setHeight(int height);
    void setWidth(int width);
    void setSegments(int numSegs);
    void updateDimensions(int height, int width, int numSegs, int supStyle);
    void create(bool hasHorizontal, bool isHollow);
private:
    int nodeIndex = 0;
    // Tower dimensions
    int height = 0;
    int width = 0;
    int numSegs = 0;
    double totalLength = 0;
    double longestBeam = 0;
    TowerStyle supStyle = TowerStyle::NONE;

    // Creates nodes
    void createNodesPerSegment(double elevation);
    // Creates beams
    void createSegments(bool hasHorizontal, bool isHollow);
    void createBeamsPerSegment(int seg, bool hasHorizontal, bool isHollow);
    void createHorizontalBeams(int valToAdd);
    void createVerticalBeams(int valToAdd);
    void createDiagonalBeams(int valToAdd);
    void createCrossFaceBeam(int valToAdd);
    void createZigzagFaceBeams(int valToAdd);
    void createParallelFaceBeamsLR(int valToAdd);
    void createParallelFaceBeamsRL(int valToAdd);
    void appendBeam(int startNode, int endNode);
};


#endif //MAINWINDOW_TOWER_H
