#ifndef MAINWINDOW_COUNTERJIB_H
#define MAINWINDOW_COUNTERJIB_H
#include <vector>

class Counterjib {
public:
    // Dimension getters and setters
    double getCounterjibLength();
    double getCounterjibHeight();
    double getCounterjibSegments();
    double getCounterjibTotalBeamLength();
    double getCounterjibLongestBeam();
    std::vector<std::vector<double>> getCounterjibNodes();
    std::vector<std::vector<int>> getCounterjibBeams();
    int getEndBase();
    void setCounterjibLength(double length);
    void setCounterjibHeight(double height);
    void setCounterjibSegments(double numberOfSegments);
    void setDimensions();
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
private:
    double length = 0;
    double height = 0;
    double numberOfSegments = 0;
    double totalLength = 0;
    double longestBeam = 0;
    int supportType = 0;

    double startHeight = 0;
    double towerWidth = 0;
    int endBase = 0;
    int endTower = 0;
    int endJib = 0;
    int jibSegments = 0;
    int jibSupport = 0;
    double jibHeight = 0;
};

#endif //MAINWINDOW_COUNTERJIB_H