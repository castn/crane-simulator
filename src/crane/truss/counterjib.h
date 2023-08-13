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
    Counterjib(double length, double height, int numSegs, int supStyle);
    // Dimension getters and setters
    double getLength();
    double getHeight();
    double getSegments();
    double getTotalBeamLength();
    double getLongestBeam();
    std::vector<Node> getNodes();
    std::vector<Beam> getBeams();
    int getEndBase();
    int getEndCJ();
    void setLength(double length);
    void setHeight(double height);
    void setSegments(double numSegs);
    void updateDimensions(double length, double height, int numSegs, int supStyle);
    void create(std::vector<Node> nodes, std::vector<Beam> beams,
                double towerHeight, double towerWidth, int towerNumNodes,
                int jibSegs, int jibSupport, double jibHeight);
private:
    // Counterjib dimensions
    double length = 0;
    double height = 0;
    double numSegs = 0;
    double totalLength = 0;
    double longestBeam = 0;
    CounterjibStyle supType = CounterjibStyle::NONE;
    int endCJ = 0;
    // Tower and Jib dimensions
    double startHeight = 0;
    double towerWidth = 0;
    int endBase = 0;
    int endTower = 0;
    int endJib = 0;
    int jibSegments = 0;
    int jibSupport = 0;
    double jibHeight = 0;

    // Create nodes
    void createSegments();
    // Create beams
    void createBeams();
    void createFrameBeams(int seg, int startCJ, double valToAdd);
    void createDiagonalBeams(int seg, int startCJ, double valToAdd);
    void createSupport();
    void createTrussSupport();
    void createTowerSupport();
    void appendBeam(int startNode, int endNode, bool lenCounts);
};

#endif //MAINWINDOW_COUNTERJIB_H