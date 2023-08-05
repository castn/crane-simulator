//
// Created by castn on 29.07.23.
//

#include "tower.h"
#include <vector>

class Comps {
public:
    std::vector<std::vector<double>> nodes;
    std::vector<double> beams;
};
Comps comps;

enum class Style {
    NONE = 0,
    CROSS = 1,
    ZIGZAG = 2,
    DIAGONAL = 3
};

class Dims {
public:
    double SEGMENT_WIDTH;
    double SEGMENT_HEIGHT;
    double SEGMENTS;
    double TOTAL_LENGTH;
    Style SUPPORT_TYPE;
    double LONGEST_BEAM;
};
Dims dims;

double Tower::getTowerHeight() {
    return height;
}

double Tower::getTowerWidth() {
    return width;
}

double Tower::getTowerSegments() {
    return numberOfSegments;
}

void Tower::setTowerHeight(double height) {
    this->height = height;
}

void Tower::setTowerWidth(double width) {
    this->width = width;
}

void Tower::setTowerSegments(double numberOfSegments) {
    this->numberOfSegments = numberOfSegments;
}

void Tower::createSegments() {
    double segmentHeight = 1000;
    for (int i = 1; i <= numberOfSegments; i++) {
        double elevation = segmentHeight * i;
        createNodesPerSegment(elevation);
    }
}

void Tower::createNodesPerSegment(double elevation) {
    // Create all nodes so the beams of a segment can connect to them
    comps.nodes.push_back({0, 0, elevation});
    comps.nodes.push_back({0, dims.SEGMENT_WIDTH, elevation});
    comps.nodes.push_back({dims.SEGMENT_WIDTH, 0, elevation});
    comps.nodes.push_back({dims.SEGMENT_WIDTH, dims.SEGMENT_WIDTH, elevation});
}
