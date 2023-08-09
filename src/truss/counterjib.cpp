#include "counterjib.h"
#include "comps.h"
#include "beam.h"
#include <iostream>
#include <vector>
#include <cmath>


Comps comps;


double Counterjib::getLength() {
    return length;
}

double Counterjib::getHeight() {
    return height;
}

double Counterjib::getSegments() {
    return numberOfSegments;
}

double Counterjib::getTotalBeamLength() {
    return totalLength;
}

double Counterjib::getLongestBeam() {
    return longestBeam;
}

std::vector<std::vector<double>> Counterjib::getNodes() {
    return comps.nodes;
}

std::vector<Beam> Counterjib::getBeams() {
    return comps.beams;
}

int Counterjib::getEndBase() {
    return endBase;
}

int Counterjib::getEndCJ() {
    return endCJ;
}

void Counterjib::setLength(double length) {
    this->length = length;
}

void Counterjib::setHeight(double height) {
    this->height = height;
}

void Counterjib::setSegments(double numberOfSegments) {
    this->numberOfSegments = numberOfSegments;
}

void Counterjib::setDimensions(double length, double height, int numSegs, int supStyle) {
    comps.nodes.clear();
    comps.beams.clear();

    totalLength = 0;
    longestBeam = 0;

    this->length = length;
    this->height = height;
    numberOfSegments = numSegs;
    switch (supStyle) {
        case 1:
            this->supType = CounterjibStyle::TRUSS;
            break;
        case 2:
            this->supType = CounterjibStyle::TOWER;
            break;
        default:
            this->supType = CounterjibStyle::NONE;
            std::cout << "No support style chosen";
    }
}


void Counterjib::create(std::vector<std::vector<double>> nodes, std::vector<Beam> beams,
                        double towerHeight, double towerWidth, int towerNumNodes,
                        int jibSegs, int jibSupport, double jibHeight) {
    comps.nodes = nodes;
    comps.beams = beams;

    startHeight = towerHeight;
    this->towerWidth = towerWidth;
    endTower = towerNumNodes - 4;
    endJib = nodes.size();
    this-> jibHeight = jibHeight;
    jibSegments = jibSegs;
    this->jibSupport = jibSupport;

    createSegments();
    createBeams();
    endBase = comps.nodes.size();
    createSupport();
    endCJ = comps.nodes.size();
}

void Counterjib::createSegments() {
    for (int i = 0; i < numberOfSegments; i++) {
        if (i != 0) {
            comps.nodes.push_back({- length * i, 0, startHeight});
            comps.nodes.push_back({- length * i, towerWidth, startHeight});
        }
    }
}

void Counterjib::createBeams() {
    int startNodeCJ = endJib;
    for (int i = 0; i < numberOfSegments - 1; i++) {
        double valToAdd = 2 * (i - 1);
        createFrameBeams(i, startNodeCJ, valToAdd);
        createDiagonalBeams(i, startNodeCJ, valToAdd);
    }
}

void Counterjib::createFrameBeams(int seg, int startCJ, double valToAdd) {
    if (seg == 0) {
        appendBeam(endTower, startCJ, true);
        appendBeam(endTower + 1, startCJ + 1, true);
    } else {
        appendBeam(startCJ + valToAdd, startCJ + 2 + valToAdd, true);
        appendBeam(startCJ + 1 + valToAdd, startCJ + 3 + valToAdd, true);
    }
    appendBeam(startCJ + valToAdd + 2, startCJ + 1 + valToAdd + 2, true);
}

void Counterjib::createDiagonalBeams(int seg, int startCJ, double valToAdd) {
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
        std::cout << "No support style chosen";
    }
}

void Counterjib::createTrussSupport() {
    int supportStart = endBase;
    for (int i = 0; i < numberOfSegments; i++) {
        double jibHeightSeg = (jibHeight - height) / 3;
        double topHeight = startHeight + height;
        // creates node on top of tower
        if (i == 0) {
            comps.nodes.push_back({1/2 * towerWidth, 1/2 * towerWidth,
                                   topHeight + 2 * jibHeightSeg});
        // creates first node on top of the support
        } else if (i == 1 && numberOfSegments > 1) {
            comps.nodes.push_back({- length / 2, 1/2 * towerWidth, topHeight + jibHeightSeg});
        }
        // creates all other nodes on top of the support
        else {
            comps.nodes.push_back({- length * ((i * 2) - 1) / 2, 1/2 * towerWidth, topHeight});
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
            double valToAdd = std::max(3 * (i - 2), 0);
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
//         comps.nodes.push_back({towerWidth / 2, towerWidth / 2, startHeight + towerWidth});
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
//     //     comps.nodes.push_back({towerWidth / 2, 0, startHeight + towerWidth});
//     //     comps.nodes.push_back({towerWidth / 2, towerWidth, startHeight + towerWidth});
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
    comps.nodes.push_back({towerWidth / 2, towerWidth / 2, startHeight + towerWidth * 2});
    // Truss support
    int supportStart = endBase;
    for (int i = 0; i < numberOfSegments; i++) {
        // create required nodes
        if (i != 0) {
            comps.nodes.push_back({- startHeight * ((i * 2) - 1) / 2, 
                                   1/2 * towerWidth, startHeight + height});
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
            double valToAdd = std::max(3 * (i - 2), 0);
            appendBeam(0 + startNode + valToAdd, supportStart + i, i != 0);
            appendBeam(1 + startNode + valToAdd, supportStart + i, i != 0);
            appendBeam(2 + startNode + valToAdd, supportStart + i, i != 0);
            appendBeam(3 + startNode + valToAdd, supportStart + i, i != 0);
        }
    }
    // Cables
    double adjustedVal = jibSegments % 2 == 0 ? 2 : (jibSupport != 2 ? 4 : 3);
    int jibNode = (endJib + endTower) / 2 + adjustedVal;
    appendBeam(supportStart, supportStart - 3, false);
    appendBeam(supportStart, supportStart - 4, false);
    appendBeam(supportStart, jibNode, false);
}

void Counterjib::appendBeam(int startNode, int endNode, bool lenCounts) {
    // // Create a beam between the two given nodes
    Beam tempBeam = Beam(comps.nodes[startNode], comps.nodes[endNode]);
    comps.beams.push_back(tempBeam);

    // Calculate the length of the beam
    // auto startVector = comps.nodes[startNode];
    // auto endVector = comps.nodes[endNode];
    // std::vector<double> lenVector = {endVector[0] - startVector[0], endVector[1] - startVector[1], endVector[2] - startVector[2]};
    // double length = sqrt(pow(lenVector[0], 2) + pow(lenVector[1], 2) + pow(lenVector[2], 2));

    // Update the longest beam and total length
    if (lenCounts) {
        longestBeam = std::max(tempBeam.getLength(), longestBeam);
    }
    totalLength += tempBeam.getLength();
}