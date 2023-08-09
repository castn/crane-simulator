#include "beam.h"
#include <cmath>

Beam::Beam(std::vector<double> start, std::vector<double> end) {
    startNode = start;
    endNode = end;
    std::vector<double> lenVector = {end[0] - start[0], end[1] - start[1], end[2] - start[2]};
    length = sqrt(pow(lenVector[0], 2) + pow(lenVector[1], 2) + pow(lenVector[2], 2));
}

double Beam::getLength() {
    return length;
}