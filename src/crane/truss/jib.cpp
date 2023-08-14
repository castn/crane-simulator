#include "jib.h"
#include "src/crane/truss/components/comps.h"
#include "src/crane/truss/components/beam.h"
#include <iostream>
#include <vector>
#include <cmath>


Comps jibComps;


Jib::Jib(int height, int width, int numSegs, int supStyle, bool dropdown, bool bend) {
    updateDimensions(height, width, numSegs, supStyle, dropdown, bend);
}


void Jib::create(std::vector<Node> nodes, std::vector<Beam> beams,
                   int towerHeight, int towerWidth) {
    jibComps.nodes = nodes;
    jibComps.beams = beams;
    startHeight = towerHeight;
    this->towerWidth = towerWidth;

    createSegments();
    createBeams();
}

void Jib::createSegments() {
    for (int i = 0; i < numSegs; i++) {
        double jibLength_m = numSegs * length / 1000;
        double lenIn_m = towerWidth / 1000 + length / 1000 * i;
        double bendGrad = 0.01 * pow(30, 1/jibLength_m * lenIn_m) * 1000;
        double botHeight = bend ? (startHeight + bendGrad) : startHeight;
        // skips the first run-through if nodes already exist
        if (i != 0) {
            jibComps.nodes.push_back(Node(towerWidth + length * i, 0, botHeight));
            jibComps.nodes.push_back(Node(towerWidth + length * i, towerWidth, botHeight));
        }
        double topHeight = 0;
        if (dropdown) {
            if (i <= 3 * numSegs / 7) {
                topHeight = height;
            } else if (i >= 5 * numSegs / 7) {
                topHeight = 0.76 * height;
            } else {
                double count = i - 2 * numSegs / 7;
                topHeight = height - count * (0.24 * 7 * height / (2 * jibLength_m));
                topHeight = std::max(topHeight, 0.76 * height);
            }
        } else {
            topHeight = height;
        }
        // adds top nodes
        if (i < numSegs) { //supType 1 -> truss
            jibComps.nodes.push_back(Node(supStyle == JibStyle::TRUSS ? towerWidth + length * i + length / 2 : towerWidth * 1.15 + length * i,
                                  length / 2, botHeight + topHeight));
        }
    }
}

void Jib::createBeams() {
    for (int i = 0; i < numSegs; i++) {
        int valToAdd = 3 * i + initBeam;
        createHorizontalBeams(i, valToAdd);
        createDiagonalBeams(valToAdd);
    }
}

void Jib::createHorizontalBeams(int seg, int valToAdd) {
    // if (i == 0 and not Dims.IS_CONNECTED) {
    //     appendBeam(0 + valToAdd, 1 + valToAdd);  // first horizontal (0-1)
    // }
    if (seg < numSegs - 1) {
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

void Jib::createDiagonalBeams(int valToAdd) {
    appendBeam(0 + valToAdd, 2 + valToAdd);
    appendBeam(1 + valToAdd, 2 + valToAdd);
    appendBeam(4 + valToAdd, 2 + valToAdd);
    appendBeam(3 + valToAdd, 2 + valToAdd);
}

void Jib::appendBeam(int startNode, int endNode) {
    // // Create a beam between the two given nodes
    Beam tempBeam = Beam(jibComps.nodes[startNode], jibComps.nodes[endNode]);
    jibComps.beams.push_back(tempBeam);
    // Update the longest beam and total length
    longestBeam = std::max(tempBeam.getLength(), longestBeam);
    totalLength += tempBeam.getLength();
}


void Jib::updateDimensions(int length, int height, int numSegs, int supStyle,
                           bool dropdown, bool bend) {
    // Reset arrays
    jibComps.nodes.clear();
    jibComps.beams.clear();
    // Reset calculated dimensions
    totalLength = 0;
    longestBeam = 0;
    // Set remaining parameters
    this->height = height;
    this->length = length;
    this->numSegs = numSegs;
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

int Jib::getLength() {
    return length;
}

int Jib::getHeight() {
    return height;
}

int Jib::getSegments() {
    return numSegs;
}

double Jib::getTotalBeamLength() {
    return totalLength;
}

double Jib::getLongestBeam() {
    return longestBeam;
}

std::vector<Node> Jib::getNodes() {
    return jibComps.nodes;
}

std::vector<Beam> Jib::getBeams() {
    return jibComps.beams;
}

int Jib::getSupportStyle() {
    switch (supStyle) {
        case JibStyle::TRUSS:
            return 1;
        case JibStyle::SET_BACK_TRUSS:
            return 2;
        default:
            return 0;
    }
}

int Jib::getEndBase() {
    return jibComps.nodes.size();
}

void Jib::setLength(int length) {
    this->length = length;
}

void Jib::setHeight(int height) {
    this->height = height;
}

void Jib::setSegments(int numSegs) {
    this->numSegs = numSegs;
}