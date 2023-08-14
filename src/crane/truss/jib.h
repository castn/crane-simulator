#ifndef MAINWINDOW_JIB_H
#define MAINWINDOW_JIB_H

#include "src/crane/truss/components/node.h"
#include "src/crane/truss/components/beam.h"
#include <vector>


enum class JibStyle {
    NONE = 0,
    TRUSS = 1,
    SET_BACK_TRUSS = 2
};

class Jib {
public:
    Jib(int length, int height, int numSegs, int supStyle, bool dropdown, bool bend);
    // Dimension getters and setters
    int getLength();
    int getHeight();
    int getSegments();
    double getTotalBeamLength();
    double getLongestBeam();
    std::vector<Node> getNodes();
    std::vector<Beam> getBeams();
    int getSupportStyle();
    int getEndBase();
    void setLength(int length);
    void setHeight(int height);
    void setSegments(int numSegs);
    void updateDimensions(int length, int height, int numSegs, int supStyle,
                          bool dropdown, bool bend);
    // Create jib
    void create(std::vector<Node> nodes, std::vector<Beam> beams,
                   int towerHeight, int towerWidth);
private:
    // Jib dimensions
    int length = 0;
    int height = 0;
    int numSegs = 0;
    double totalLength = 0;
    double longestBeam = 0;
    JibStyle supStyle = JibStyle::NONE;
    bool dropdown = false;
    bool bend = false;
    int initBeam = 0;
    int endBase = 0;
    // Tower dimensions
    int startHeight = 0;
    int towerWidth = 0;

    // Create nodes
    void createSegments();
    // Create beams
    void createBeams();
    void createHorizontalBeams(int seg, int valToAdd);
    void createDiagonalBeams(int valToAdd);
    void appendBeam(int startNode, int endNode);
};

#endif //MAINWINDOW_JIB_H
