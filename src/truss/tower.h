#ifndef MAINWINDOW_TOWER_H
#define MAINWINDOW_TOWER_H
#include <vector>


class Tower {
public:
    // Dimension getters and setters
    double getTowerHeight();
    double getTowerWidth();
    double getTowerSegments();
    double getTowerTotalBeamLength();
    double getTowerLongestBeam();
    double getTowerTotalHeight();
    std::vector<std::vector<double>> getTowerNodes();
    std::vector<std::vector<int>> getTowerBeams();
    void setTowerHeight(double height);
    void setTowerWidth(double width);
    void setTowerSegments(double numberOfSegments);
    void setDimensions();
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
private:
    double height = 0;
    double width = 0;
    double numberOfSegments = 0;
    double totalLength = 0;
    double longestBeam = 0;
    int faceStyle = 0;
};


#endif //MAINWINDOW_TOWER_H
