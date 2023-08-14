#include "tower.h"
#include "src/crane/truss/components/comps.h"
#include "src/crane/truss/components/node.h"
#include "src/crane/truss/components/beam.h"
#include <iostream>
#include <vector>
#include <cmath>


Comps towerComps;


Tower::Tower(int height, int width, int numSegs, int supStyle) {
    updateDimensions(height, width, numSegs, supStyle);
}

void Tower::create(bool hasHorizontal, bool isHollow) {
    createSegments(hasHorizontal, isHollow);
}

void Tower::createSegments(bool hasHorizontal, bool isHollow) {
    for (int i = 0; i <= numSegs; i++) {
        double elevation = height * i;
        createNodesPerSegment(elevation);
    }

    for (int i = 0; i <= numSegs; i++) {
        createBeamsPerSegment(i, hasHorizontal, isHollow);
    }
}

void Tower::createNodesPerSegment(double elevation) {
    // Create all nodes so the beams of a segment can connect to them
    towerComps.nodes.emplace_back(0, 0, elevation);
    towerComps.nodes.emplace_back(0, width, elevation);
    towerComps.nodes.emplace_back(width, 0, elevation);
    towerComps.nodes.emplace_back(width, width, elevation);
}

void Tower::createBeamsPerSegment(int segment, bool hasHorizontal, bool isHollow) {
    int valToAdd = 4 * segment;
    if (hasHorizontal) {
        createHorizontalBeams(valToAdd);
    }
    if (!isHollow) {
        appendBeam(0 + valToAdd, 2 + valToAdd);
    }
    if (segment < numSegs) {
        createVerticalBeams(valToAdd);
        createDiagonalBeams(valToAdd);
    }
}

void Tower::createHorizontalBeams(int valToAdd) {
    appendBeam(0 + valToAdd, 1 + valToAdd);  // front horizontal beam
    appendBeam(1 + valToAdd, 3 + valToAdd);  // right horizontal beam
    appendBeam(3 + valToAdd, 2 + valToAdd);  // rear horizontal beam
    appendBeam(2 + valToAdd, 0 + valToAdd);  // left horizontal beam
    if (valToAdd != 0) {
        appendBeam(0 + valToAdd, 3 + valToAdd);
    }
}

void Tower::createVerticalBeams(int valToAdd) {
    appendBeam(0 + valToAdd, 4 + valToAdd);  // front left vertical beam
    appendBeam(1 + valToAdd, 5 + valToAdd);  // front right vertical beam
    appendBeam(3 + valToAdd, 7 + valToAdd);  // rear left vertical beam
    appendBeam(2 + valToAdd, 6 + valToAdd);  // rear right vertical beam
}

void Tower::createDiagonalBeams(int valToAdd) {
    if (supStyle == TowerStyle::DIAGONAL) { //style.DIAGONAL/3
        createParallelFaceBeamsLR(valToAdd);
    }
    else if (supStyle == TowerStyle::CROSS) { //style.CROSS/1
        createCrossFaceBeam(valToAdd);
    }
    else if (supStyle == TowerStyle::ZIGZAG) { //style.ZIGZAG/2
        createZigzagFaceBeams(valToAdd);
    }
}

void Tower::createCrossFaceBeam(int valToAdd) {
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

void Tower::createZigzagFaceBeams(int valToAdd) {
    int valToCheck = valToAdd / 4;
    if (valToCheck % 2 == 0) {
        // For even numbers create diagonal from left to right
        createParallelFaceBeamsLR(valToAdd);
    } else {
        // For odd numbers create diagonal from right to left
        createParallelFaceBeamsRL(valToAdd);
    }
}

void Tower::createParallelFaceBeamsLR(int valToAdd) {
    appendBeam(0 + valToAdd, 5 + valToAdd);  // front face
    appendBeam(5 + valToAdd, 3 + valToAdd);  // right face
    appendBeam(3 + valToAdd, 6 + valToAdd);  // rear face
    appendBeam(6 + valToAdd, 0 + valToAdd);  // left face
}

void Tower::createParallelFaceBeamsRL(int valToAdd) {
    appendBeam(4 + valToAdd, 1 + valToAdd);  // front face
    appendBeam(1 + valToAdd, 7 + valToAdd);  // right face
    appendBeam(7 + valToAdd, 2 + valToAdd);  // rear face
    appendBeam(2 + valToAdd, 4 + valToAdd);  // left face
}

void Tower::appendBeam(int startNode, int endNode) {
    // // Create a beam between the two given nodes
    Beam tempBeam = Beam(towerComps.nodes[startNode], towerComps.nodes[endNode]);
    towerComps.beams.push_back(tempBeam);
    // Update the longest beam and total length
    longestBeam = std::max(tempBeam.getLength(), longestBeam);
    totalLength += tempBeam.getLength();
}

void Tower::updateDimensions(int height, int width, int numSegs, int supStyle) {
    // Reset arrays
    towerComps.nodes.clear();
    towerComps.beams.clear();
    // Reset calculated dimensions
    totalLength = 0;
    longestBeam = 0;
    // Set remaining parameters
    this->height = height;
    this->width = width;
    this->numSegs = numSegs;
    switch (supStyle) {
        case 1:
            this->supStyle = TowerStyle::CROSS;
            break;
        case 2:
            this->supStyle = TowerStyle::ZIGZAG;
            break;
        case 3:
            this->supStyle = TowerStyle::DIAGONAL;
            break;
        default:
            this->supStyle = TowerStyle::NONE;
            std::cout << "No support style chosen";
    }
}

int Tower::getHeight() {
    return height;
}

int Tower::getWidth() {
    return width;
}

int Tower::getSegments() {
    return numSegs;
}

double Tower::getTotalBeamLength() {
    return totalLength;
}

double Tower::getLongestBeam() {
    return longestBeam;
}

int Tower::getTotalHeight() {
    return height * numSegs;
}

std::vector<Node> Tower::getNodes() {
    return towerComps.nodes;
}

std::vector<Beam> Tower::getBeams() {
    return towerComps.beams;
}

void Tower::setHeight(int height) {
    this->height = height;
}

void Tower::setWidth(int width) {
    this->width = width;
}

void Tower::setSegments(int numSegs) {
    this->numSegs = numSegs;
}
