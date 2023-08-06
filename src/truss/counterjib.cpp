#include "counterjib.h"
#include <vector>
#include <cmath>


class Comps {
public:
    std::vector<std::vector<double>> nodes;
    std::vector<std::vector<int>> beams;
};
Comps comps;


double Counterjib::getCounterjibLength() {
    return length;
}

double Counterjib::getCounterjibHeight() {
    return height;
}

double Counterjib::getCounterjibSegments() {
    return numberOfSegments;
}

double Counterjib::getCounterjibTotalBeamLength() {
    return totalLength;
}

double Counterjib::getCounterjibLongestBeam() {
    return longestBeam;
}

std::vector<std::vector<double>> Counterjib::getCounterjibNodes() {
    return comps.nodes;
}

std::vector<std::vector<int>> Counterjib::getCounterjibBeams() {
    return comps.beams;
}

int Counterjib::getEndBase() {
    return 0;
}

void Counterjib::setCounterjibLength(double length) {
    this->length = length;
}

void Counterjib::setCounterjibHeight(double height) {
    this->height = height;
}

void Counterjib::setCounterjibSegments(double numberOfSegments) {
    this->numberOfSegments = numberOfSegments;
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
    if (supportType == 1) { //Truss
        createTrussSupport();
    } else if (supportType == 2) { //Tower
        createTowerSupport();
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
    comps.beams.push_back({startNode, endNode});

    // Calculate the length of the beam
    auto startVector = comps.nodes[startNode];
    auto endVector = comps.nodes[endNode];
    std::vector<double> lenVector = {endVector[0] - startVector[0],
                                     endVector[1] - startVector[1],
                                     endVector[2] - startVector[2]};
    double length = sqrt(pow(lenVector[0], 2) + pow(lenVector[1], 2) + pow(lenVector[2], 2));

    // Update the longest beam and total length
    if (lenCounts) {
        longestBeam = std::max(length, longestBeam);
    }
    totalLength += length;
}