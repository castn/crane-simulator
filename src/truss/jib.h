#ifndef MAINWINDOW_JIB_H
#define MAINWINDOW_JIB_H
#include <vector>

class Jib {
public:
    // Dimension getters and setters
    double getJibLength();
    double getJibHeight();
    double getJibSegments();
    double getJibTotalBeamLength();
    double getJibLongestBeam();
    std::vector<std::vector<double>> getJibNodes();
    std::vector<std::vector<int>> getJibBeams();
    int getEndBase();
    void setJibLength(double length);
    void setJibHeight(double height);
    void setJibSegments(double numberOfSegments);
    // Create nodes
    void createSegments();
    // Create beams
    void createBeams(double valToAdd);
    void createHorizontalBeams(int seg, double valToAdd);
    void createDiagonalBeams(double valToAdd);
    void appendBeam(int startNode, int endNode);
private:
    double length = 0;
    double height = 0;
    double numberOfSegments = 0;
    double totalLength = 0;
    double longestBeam = 0;
    int supportType = 0;
    bool dropdown = false;
    bool bend = false;
    double startHeight = 0;
    double towerWidth = 0;
    int initBeam = 0;
    int endBase = 0;
};

#endif //MAINWINDOW_JIB_H
