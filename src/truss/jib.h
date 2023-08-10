#ifndef MAINWINDOW_JIB_H
#define MAINWINDOW_JIB_H

#include <vector>
#include "beam.h"


enum class JibStyle {
    NONE = 0,
    TRUSS = 1,
    SET_BACK_TRUSS = 2
};

class Jib {
public:
    // Dimension getters and setters
    double getLength();
    double getHeight();
    double getSegments();
    double getTotalBeamLength();
    double getLongestBeam();
    std::vector<Node> getNodes();
    std::vector<Beam> getBeams();
    int getSupportStyle();
    int getEndBase();
    void setLength(double length);
    void setHeight(double height);
    void setSegments(double numberOfSegments);
    void setDimensions(double length, double height, int numSegs, int supStyle,
                       bool dropdown, bool bend);
    void create(std::vector<Node> nodes, std::vector<Beam> beams,
                   double towerHeight, double towerWidth);
private:
    // Jib dimensions
    double length = 0;
    double height = 0;
    double numberOfSegments = 0;
    double totalLength = 0;
    double longestBeam = 0;
    JibStyle supStyle = JibStyle::NONE;
    bool dropdown = false;
    bool bend = false;
    int initBeam = 0;
    int endBase = 0;
    // Tower dimensions
    double startHeight = 0;
    double towerWidth = 0;

    // Create nodes
    void createSegments();
    // Create beams
    void createBeams();
    void createHorizontalBeams(int seg, double valToAdd);
    void createDiagonalBeams(double valToAdd);
    void appendBeam(int startNode, int endNode);
};

#endif //MAINWINDOW_JIB_H
