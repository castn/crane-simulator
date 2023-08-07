#include "jib.h"
#include <iostream>
#include <vector>
#include <cmath>


class Comps {
public:
    std::vector<std::vector<double>> nodes;
    std::vector<std::vector<int>> beams;
};
Comps comps;


double Jib::getJibLength() {
    return length;
}

double Jib::getJibHeight() {
    return height;
}

double Jib::getJibSegments() {
    return numberOfSegments;
}

double Jib::getJibTotalBeamLength() {
    return totalLength;
}

double Jib::getJibLongestBeam() {
    return longestBeam;
}

std::vector<std::vector<double>> Jib::getJibNodes() {
    return comps.nodes;
}

std::vector<std::vector<int>> Jib::getJibBeams() {
    return comps.beams;
}

int Jib::getEndBase() {
    return comps.nodes.size();
}

void Jib::setJibLength(double length) {
    this->length = length;
}

void Jib::setJibHeight(double height) {
    this->height = height;
}

void Jib::setJibSegments(double numberOfSegments) {
    this->numberOfSegments = numberOfSegments;
}

void Jib::setDimensions(double length, double height, int numSegs, int supStyle,
                   bool dropdown, bool bend) {
    // Reset arrays
    comps.nodes.clear();
    comps.beams.clear();
    // Reset calculated dimensions
    totalLength = 0;
    longestBeam = 0;
    // Set remaining parameters
    this->height = height;
    this->length = length;
    numberOfSegments = numSegs;
    switch (supStyle) {
        case 1:
            this->supStyle = JibStyle::TRUSS;
            break;
        case 2:
            this->supStyle = JibStyle::SET_BACK_TRUSS;
            break;
        default:
            this->supStyle = JibStyle::NONE;
            std::cout << "No support style chosen";
    }
    this->dropdown = dropdown;
    this->bend = bend;
}


void Jib::createJib(std::vector<std::vector<double>> nodes, std::vector<std::vector<int>> beams,
                   double towerHeight, double towerWidth) {
    comps.nodes = nodes;
    comps.beams = beams;
    startHeight = towerHeight;
    this->towerWidth = towerWidth;

    createSegments();
    createBeams();
}

void Jib::createSegments() {
    for (int i = 0; i < numberOfSegments; i++) {
        double jibLength_m = numberOfSegments * length / 1000;
        double lenIn_m = towerWidth / 1000 + length / 1000 * i;
        double bendGrad = 0.01 * pow(30, 1/jibLength_m * lenIn_m) * 1000;
        double botHeight = bend ? (startHeight + bendGrad) : startHeight;
        // skips the first run-through if nodes already exist
        if (i != 0) {
            comps.nodes.push_back({towerWidth + length * i, 0, botHeight});
            comps.nodes.push_back({towerWidth + length * i, towerWidth, botHeight});
        }
        double topHeight = 0;
        if (dropdown) {
            if (i <= 3 * numberOfSegments / 7) {
                topHeight = height;
            } else if (i >= 5 * numberOfSegments / 7) {
                topHeight = 0.76 * height;
            } else {
                double count = i - 2 * numberOfSegments / 7;
                topHeight = height - count * (0.24 * 7 * height / (2 * jibLength_m));
                topHeight = std::max(topHeight, 0.76 * height);
            }
        } else {
            topHeight = height;
        }
        // adds top nodes
        if (i < numberOfSegments) { //supType 1 -> truss
            comps.nodes.push_back({supStyle == JibStyle::TRUSS ? towerWidth + length * i + length / 2 : towerWidth * 1.15 + length * i,
                                   length / 2, botHeight + topHeight});
        }
    }
}

void Jib::createBeams() {
    for (int i = 0; i < numberOfSegments; i++) {
        double valToAdd = 3 * i + initBeam;
        createHorizontalBeams(i, valToAdd);
        createDiagonalBeams(valToAdd);
    }
}

void Jib::createHorizontalBeams(int seg, double valToAdd) {
    // if (i == 0 and not Dims.IS_CONNECTED) {
    //     appendBeam(0 + valToAdd, 1 + valToAdd);  // first horizontal (0-1)
    // }
    if (seg < numberOfSegments - 1) {
        appendBeam(2 + valToAdd, 5 + valToAdd);  // top connection
    }
    // if (i == Dims.SEGMENTS - 1 and Dims.SUPPORT_TYPE != Style.TRUSS) {
    //     appendBeam(2 + valToAdd, 5 + valToAdd);
    // }
    appendBeam(1 + valToAdd, 4 + valToAdd);
    appendBeam(4 + valToAdd, 3 + valToAdd);
    appendBeam(3 + valToAdd, 0 + valToAdd);
    appendBeam(1 + valToAdd, 3 + valToAdd);     // bottom diagonal beam
}

void Jib::createDiagonalBeams(double valToAdd) {
    appendBeam(0 + valToAdd, 2 + valToAdd);
    appendBeam(1 + valToAdd, 2 + valToAdd);
    appendBeam(4 + valToAdd, 2 + valToAdd);
    appendBeam(3 + valToAdd, 2 + valToAdd);
}

void Jib::appendBeam(int startNode, int endNode) {
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