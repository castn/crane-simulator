#include "beam.h"
#include "node.h"
#include <cmath>

Beam::Beam(Node start, Node end) : startNode(start), endNode(end) {
    // this->startNode = start;
    // this->endNode = end;
    // Node lenVector = end - start;//{end.getX() - start.getX(), end.getY() - start.getY(), end.getZ() - start.getZ()};
    length = (end - start).norm();//sqrt(pow(lenVector[0], 2) + pow(lenVector[1], 2) + pow(lenVector[2], 2));
}

double Beam::getLength() {
    return length;
}