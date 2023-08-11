#ifndef MAINWINDOW_NODE_H
#define MAINWINDOW_NODE_H

class Node {
public:
    Node(double x, double y, double z);
    double getX();
    double getY();
    double getZ();
    double norm();

    Node operator - (const Node& node) const {
        return Node(this->x - node.x, this->y - node.y, this->z - node.z);
    }
private:
    double x;
    double y;
    double z;
};

#endif