//
// Created by castn on 29.07.23.
//

#include "tower.h"

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

}
