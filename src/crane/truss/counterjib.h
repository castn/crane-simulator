#ifndef MAINWINDOW_COUNTERJIB_H
#define MAINWINDOW_COUNTERJIB_H

#include "src/crane/truss/components/node.h"
#include "src/crane/truss/components/beam.h"
#include <vector>


enum class CounterjibStyle {
    NONE = 0,
    TRUSS = 1,
    TOWER = 2
};

class Counterjib {
public:
    Counterjib(int length, int height, int numSegs, int supStyle);
    // Dimension getters and setters
    int getLength();
    int getHeight();
    int getSegments();
    double getTotalBeamLength();
    double getLongestBeam();
    std::vector<Node> getNodes();
    std::vector<Beam> getBeams();
    int getEndBase();
    int getEndCJ();
    void setLength(int length);
    void setHeight(int height);
    void setSegments(int numSegs);
    void updateDimensions(int length, int height, int numSegs, int supStyle);
    void create(std::vector<Node> nodes, std::vector<Beam> beams,
                int towerHeight, int towerWidth, int towerNumNodes,
                int jibSegs, int jibSupport, int jibHeight);
private:
    int nodeIndex = 0;
    // Counterjib dimensions
    int length = 0;
    int height = 0;
    int numSegs = 0;
    double totalLength = 0;
    double longestBeam = 0;
    CounterjibStyle supType = CounterjibStyle::NONE;
    int endCJ = 0;
    // Tower and Jib dimensions
    int startHeight = 0;
    int towerWidth = 0;
    int endBase = 0;
    int endTower = 0;
    int endJib = 0;
    int jibSegments = 0;
    int jibSupport = 0;
    int jibHeight = 0;

    // Create nodes
    void createSegments();
    // Create beams
    void createBeams();
    void createFrameBeams(int seg, int startCJ, int valToAdd);
    void createDiagonalBeams(int seg, int startCJ, int valToAdd);
    void createSupport();
    void createTrussSupport();
    void createTowerSupport();
    void appendBeam(int startNode, int endNode, bool lenCounts);
};

#endif //MAINWINDOW_COUNTERJIB_H