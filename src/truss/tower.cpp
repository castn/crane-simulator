#include "tower.h"
#include <vector>
#include <cmath>
// #include <Eigen/Dense>
// #include <xtensor/xarray.hpp>

class Comps {
public:
    std::vector<std::vector<double>> nodes;
    // xt::xarray<double> nodes;
    std::vector<std::vector<int>> beams;
};
Comps comps;


double Tower::getTowerHeight() {
    return height;
}

double Tower::getTowerWidth() {
    return width;
}

double Tower::getTowerSegments() {
    return numberOfSegments;
}

double Tower::getTowerTotalBeamLength() {
    return totalLength;
}

double Tower::getTowerLongestBeam() {
    return longestBeam;
}

double Tower::getTowerTotalHeight() {
    return height * numberOfSegments;
}

std::vector<std::vector<double>> Tower::getTowerNodes() {
    return comps.nodes;
}

std::vector<std::vector<int>> Tower::getTowerBeams() {
    return comps.beams;
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


void Tower::createSegments(bool hasHorizontal, bool isHollow) {
    double segmentHeight = 1000;
    for (int i = 0; i <= numberOfSegments; i++) {
        double elevation = segmentHeight * i;
        createNodesPerSegment(elevation);
    }

    for (int i = 0; i <= numberOfSegments; i++) {
        createBeamsPerSegment(i, hasHorizontal, isHollow);
    }
}

void Tower::createNodesPerSegment(double elevation) {
    // Create all nodes so the beams of a segment can connect to them
    comps.nodes.push_back({0, 0, elevation});
    comps.nodes.push_back({0, width, elevation});
    comps.nodes.push_back({width, 0, elevation});
    comps.nodes.push_back({width, width, elevation});
}

void Tower::createBeamsPerSegment(int seg, bool hasHorizontal, bool isHollow) {
    double valToAdd = 4 * seg;
    if (hasHorizontal) {
        createHorizontalBeams(valToAdd);
    }
    if (!isHollow) {
        appendBeam(0 + valToAdd, 2 + valToAdd);
    }
    if (seg < numberOfSegments) {
        createVerticalBeams(valToAdd);
        createDiagonalBeams(valToAdd);
    }
}

void Tower::createHorizontalBeams(double valToAdd) {
    appendBeam(0 + valToAdd, 1 + valToAdd);  // front horizontal beam
    appendBeam(1 + valToAdd, 3 + valToAdd);  // right horizontal beam
    appendBeam(3 + valToAdd, 2 + valToAdd);  // rear horizontal beam
    appendBeam(2 + valToAdd, 0 + valToAdd);  // left horizontal beam
    if (valToAdd != 0) {
        appendBeam(0 + valToAdd, 3 + valToAdd);
    }
}

void Tower::createVerticalBeams(double valToAdd) {
    appendBeam(0 + valToAdd, 4 + valToAdd);  // front left vertical beam
    appendBeam(1 + valToAdd, 5 + valToAdd);  // front right vertical beam
    appendBeam(3 + valToAdd, 7 + valToAdd);  // rear left vertical beam
    appendBeam(2 + valToAdd, 6 + valToAdd);  // rear right vertical beam
}

void Tower::createDiagonalBeams(double valToAdd) {
    if (faceStyle == 3) { //style.DIAGONAL
        createParallelFaceBeamsLR(valToAdd);
    }
    else if (faceStyle == 1) { //style.CROSS
        createCrossFaceBeam(valToAdd);
    }
    else if (faceStyle == 2) { //style.ZIGZAG
        createZigzagFaceBeams(valToAdd);
    }
}

void Tower::createCrossFaceBeam(double valToAdd) {
    // front face
    appendBeam(0 + valToAdd, 5 + valToAdd);
    appendBeam(4 + valToAdd, 1 + valToAdd);
    // right face
    appendBeam(5 + valToAdd, 3 + valToAdd);
    appendBeam(1 + valToAdd, 7 + valToAdd);
    // rear face
    appendBeam(2 + valToAdd, 7 + valToAdd);
    appendBeam(6 + valToAdd, 3 + valToAdd);
    // left face
    appendBeam(6 + valToAdd, 0 + valToAdd);
    appendBeam(2 + valToAdd, 4 + valToAdd);
}

void Tower::createZigzagFaceBeams(double valToAdd) {
    int valToCheck = valToAdd / 4;
    if (valToCheck % 2 == 0) {
        // For even numbers create diagonal from left to right
        createParallelFaceBeamsLR(valToAdd);
    } else {
        // For odd numbers create diagonal from right to left
        createParallelFaceBeamsRL(valToAdd);
    }
}

void Tower::createParallelFaceBeamsLR(double valToAdd) {
    appendBeam(0 + valToAdd, 5 + valToAdd);  // front face
    appendBeam(5 + valToAdd, 3 + valToAdd);  // right face
    appendBeam(3 + valToAdd, 6 + valToAdd);  // rear face
    appendBeam(6 + valToAdd, 0 + valToAdd);  // left face
}

void Tower::createParallelFaceBeamsRL(double valToAdd) {
    appendBeam(4 + valToAdd, 1 + valToAdd);  // front face
    appendBeam(1 + valToAdd, 7 + valToAdd);  // right face
    appendBeam(7 + valToAdd, 2 + valToAdd);  // rear face
    appendBeam(2 + valToAdd, 4 + valToAdd);  // left face
}

void Tower::appendBeam(int startNode, int endNode) {
    // // Create a beam between the two given nodes
    comps.beams.push_back({startNode, endNode});

    // Calculate the length of the beam
    auto startVector = comps.nodes[startNode];
    auto endVector = comps.nodes[endNode];
    std::vector<double> lenVector = {endVector[0] - startVector[0], endVector[1] - startVector[1], endVector[2] - startVector[2]};
    double length = sqrt(pow(lenVector[0], 2) + pow(lenVector[1], 2) + pow(lenVector[2], 2));

    // Update the longest beam and total length
    longestBeam = std::max(length, longestBeam);
    totalLength += length;
}
