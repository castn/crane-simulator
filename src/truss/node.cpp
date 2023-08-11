#include "node.h"
#include <cmath>

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

double Node::norm() {
    return sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2));
}
