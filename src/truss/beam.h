#ifndef MAINWINDOW_BEAM_H
#define MAINWINDOW_BEAM_H

#include <vector>


class Beam {
public:
    Beam(std::vector<double> start, std::vector<double> end);
    double getLength();
private:
    std::vector<double> startNode;
    std::vector<double> endNode;
    double length;
};

#endif