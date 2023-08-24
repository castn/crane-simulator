#include "counterjib.h"
#include "src/crane/truss/components/comps.h"
#include "src/crane/truss/components/beam.h"
#include <iostream>
#include <vector>
#include <cmath>


Comps cjComps;


Counterjib::Counterjib(int length, int height, int numSegs, int supStyle) {
    updateDimensions(length, height, numSegs, supStyle);
}


void Counterjib::create(std::vector<Node> nodes, std::vector<Beam> beams,
                        int towerHeight, int towerWidth, int towerNumNodes,
                        int jibSegs, int jibSupport, int jibHeight) {
    cjComps.nodes = nodes;
    cjComps.beams = beams;

    startHeight = towerHeight;
    this->towerWidth = towerWidth;
    endTower = towerNumNodes - 4;
    endJib = nodes.size();
    this-> jibHeight = jibHeight;
    jibSegments = jibSegs;
    this->jibSupport = jibSupport;

    createSegments();
    createBeams();
    endBase = cjComps.nodes.size();
    createSupport();
    endCJ = cjComps.nodes.size();
}

void Counterjib::createSegments() {
    for (int i = 0; i < numSegs; i++) {
        if (i != 0) {
            cjComps.nodes.push_back(Node(- length * i, 0, startHeight, nodeIndex));
            nodeIndex++;
            cjComps.nodes.push_back(Node(- length * i, towerWidth, startHeight, nodeIndex));
            nodeIndex++;
        }
    }
}

void Counterjib::createBeams() {
    int startNodeCJ = endJib;
    for (int i = 0; i < numSegs - 1; i++) {
        int valToAdd = 2 * (i - 1);
        createFrameBeams(i, startNodeCJ, valToAdd);
        createDiagonalBeams(i, startNodeCJ, valToAdd);
    }
}

void Counterjib::createFrameBeams(int seg, int startCJ, int valToAdd) {
    if (seg == 0) {
        appendBeam(endTower, startCJ, true);
        appendBeam(endTower + 1, startCJ + 1, true);
    } else {
        appendBeam(startCJ + valToAdd, startCJ + 2 + valToAdd, true);
        appendBeam(startCJ + 1 + valToAdd, startCJ + 3 + valToAdd, true);
    }
    appendBeam(startCJ + valToAdd + 2, startCJ + 1 + valToAdd + 2, true);
}

void Counterjib::createDiagonalBeams(int seg, int startCJ, int valToAdd) {
    if (seg == 0) {
        appendBeam(endTower, startCJ + 1, true);
        appendBeam(endTower + 1, startCJ, true);
    } else {
        appendBeam(startCJ + valToAdd, startCJ + 3 + valToAdd, true);
        appendBeam(startCJ + 1 + valToAdd, startCJ + 2 + valToAdd, true);
    }
}

void Counterjib::createSupport() {
    if (supType == CounterjibStyle::TRUSS) { //Truss
        createTrussSupport();
    } else if (supType == CounterjibStyle::TOWER) { //Tower
        createTowerSupport();
    } else {
        std::cout << "No support style chosen!\n";
    }
}

void Counterjib::createTrussSupport() {
    int supportStart = endBase;
    for (int i = 0; i < numSegs; i++) {
        double jibHeightSeg = (jibHeight - height) / 3;
        double topHeight = startHeight + height;
        // creates node on top of tower
        if (i == 0) {
            cjComps.nodes.push_back(Node(1/2 * towerWidth, 1/2 * towerWidth,
                                   topHeight + 2 * jibHeightSeg, nodeIndex));
            nodeIndex++;
        // creates first node on top of the support
        } else if (i == 1 && numSegs > 1) {
            cjComps.nodes.push_back(Node(- length / 2, 1/2 * towerWidth,
                                         topHeight + jibHeightSeg, nodeIndex));
            nodeIndex++;
        }
        // creates all other nodes on top of the support
        else {
            cjComps.nodes.push_back(Node(- length * ((i * 2) - 1) / 2, 1/2 * towerWidth,
                                         topHeight, nodeIndex));
            nodeIndex++;
        }
        // create 'pyramid' structure on top of tower
        if (i == 1) {
            // diagonal sections
            appendBeam(endTower, supportStart + 1, true);
            appendBeam(endTower + 1, supportStart + 1, true);
            appendBeam(endJib, supportStart + 1, true);
            appendBeam(endJib + 1, supportStart + 1, true);
            // top section
            appendBeam(supportStart, supportStart + 1, true);
        } 
        // create the rest of the 'pyramids'
        else {
            int startNode = 0;
            if (i == 0) {
                startNode = endTower;
                appendBeam(endTower + 4, supportStart, true);
            } else {
                startNode = endJib - std::max(i - 2, 0);
                appendBeam(supportStart + (i - 1), supportStart + i, true);
            }
            // diagonal sections
            int valToAdd = std::max(3 * (i - 2), 0);
            appendBeam(0 + startNode + valToAdd, supportStart + i, true);
            appendBeam(1 + startNode + valToAdd, supportStart + i, true);
            appendBeam(2 + startNode + valToAdd, supportStart + i, true);
            appendBeam(3 + startNode + valToAdd, supportStart + i, true);
        }
    }
}

// void Counterjib::createTowerSupport() {
//     int cableStart = endBase;
//     // if (one_tower) {
//         cjComps.nodes.push_back({towerWidth / 2, towerWidth / 2, startHeight + towerWidth});
//         // tower to new top
//         for (int i = 0; i < 4; i++) {
//             appendBeam(endTower + i, cableStart, true);
//         }
//         // jib to new top
//         appendBeam(endTower + 4, cableStart, true);
//         // new top to end counterjib
//         appendBeam(cableStart, cableStart - 1, false);
//         appendBeam(cableStart, cableStart - 2, false);
//     // } else {
//     //     cjComps.nodes.push_back({towerWidth / 2, 0, startHeight + towerWidth});
//     //     cjComps.nodes.push_back({towerWidth / 2, towerWidth, startHeight + towerWidth});
//     //     // tower to new tops
//     //     for (int i = 0; i < 2; i++) {
//     //         appendBeam(endTower + i, cableStart + i, true);
//     //         appendBeam(endTower + i + 2, cableStart + i, true);
//     //     }
//     //     // between new tops
//     //     appendBeam(cableStart, cableStart + 1, true);
//     //     // jib to new tops
//     //     appendBeam(endTower + 4, cableStart, true);
//     //     appendBeam(endTower + 4, cableStart + 1, true);
//     //     // new tops to end counterjib
//     //     appendBeam(cableStart, cableStart - 2, false);
//     //     appendBeam(cableStart + 1, cableStart - 1, false);
//     // }
//     // reinforce base
//     appendBeam(endTower + 1, endBase - 2, false);
//     appendBeam(endTower, endBase - 1, false);
//     appendBeam(endTower, endBase - 2, false);
//     appendBeam(endTower + 1, endBase - 1, false);
// }
void Counterjib::createTowerSupport() {
    cjComps.nodes.push_back(Node(towerWidth / 2, towerWidth / 2, startHeight + towerWidth * 2, nodeIndex));
    nodeIndex++;
    // Truss support
    int supportStart = endBase;
    for (int i = 0; i < numSegs; i++) {
        // create required nodes
        if (i != 0) {
            cjComps.nodes.push_back(Node(- startHeight * ((i * 2) - 1) / 2, 
                                       1/2 * towerWidth, startHeight + height, nodeIndex));
            nodeIndex++;
        }
        // second batch
        if (i == 1) {
            // diagonal sections
            appendBeam(endTower, supportStart + 1, true);
            appendBeam(endTower + 1, supportStart + 1, true);
            appendBeam(endJib, supportStart + 1, true);
            appendBeam(endJib + 1, supportStart + 1, true);
        }
        // the rest
        else {
        int startNode = 0;
            if (i == 0) {
                startNode = endTower;
            } else {
                startNode = endJib - std::max(i - 2, 0);
                appendBeam(supportStart + (i - 1), supportStart + i, true);
            }
            // diagonal sections
            int valToAdd = std::max(3 * (i - 2), 0);
            appendBeam(0 + startNode + valToAdd, supportStart + i, i != 0);
            appendBeam(1 + startNode + valToAdd, supportStart + i, i != 0);
            appendBeam(2 + startNode + valToAdd, supportStart + i, i != 0);
            appendBeam(3 + startNode + valToAdd, supportStart + i, i != 0);
        }
    }
    // Cables
    int adjustedVal = jibSegments % 2 == 0 ? 2 : (jibSupport != 2 ? 4 : 3);
    int jibNode = (endJib + endTower) / 2 + adjustedVal;
    appendBeam(supportStart, supportStart - 3, false);
    appendBeam(supportStart, supportStart - 4, false);
    appendBeam(supportStart, jibNode, false);
}

void Counterjib::appendBeam(int startNode, int endNode, bool lenCounts) {
    // // Create a beam between the two given nodes
    Beam tempBeam = Beam(cjComps.nodes[startNode], cjComps.nodes[endNode]);
    cjComps.beams.push_back(tempBeam);
    // Update the longest beam and total length
    if (lenCounts) {
        longestBeam = std::max(tempBeam.getLength(), longestBeam);
    }
    totalLength += tempBeam.getLength();
}


void Counterjib::updateDimensions(int length, int height, int numSegs, int supStyle) {
    cjComps.nodes.clear();
    cjComps.beams.clear();

    totalLength = 0;
    longestBeam = 0;

    this->length = length;
    this->height = height;
    this->numSegs = numSegs;
    switch (supStyle) {
        case 1:
            this->supType = CounterjibStyle::TRUSS;
            break;
        case 2:
            this->supType = CounterjibStyle::TOWER;
            break;
        default:
            this->supType = CounterjibStyle::NONE;
            std::cout << "No support style chosen!S\n";
    }

    nodeIndex = 0;
}

int Counterjib::getLength() {
    return length;
}

int Counterjib::getHeight() {
    return height;
}

int Counterjib::getSegments() {
    return numSegs;
}

double Counterjib::getTotalBeamLength() {
    return totalLength;
}

double Counterjib::getLongestBeam() {
    return longestBeam;
}

std::vector<Node> Counterjib::getNodes() {
    return cjComps.nodes;
}

std::vector<Beam> Counterjib::getBeams() {
    return cjComps.beams;
}

int Counterjib::getEndBase() {
    return endBase;
}

int Counterjib::getEndCJ() {
    return endCJ;
}

void Counterjib::setLength(int length) {
    this->length = length;
}

void Counterjib::setHeight(int height) {
    this->height = height;
}

void Counterjib::setSegments(int numSegs) {
    this->numSegs = numSegs;
}