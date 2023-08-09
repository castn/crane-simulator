#include "node.h"

Node::Node(double x, double y, double z) {
    this->x = x;
    this->y = y;
    this->z = z;
}

double Node::getX() {
    return x;
}

double Node::getY() {
    return y;
}

double Node::getZ() {
    return z;
}