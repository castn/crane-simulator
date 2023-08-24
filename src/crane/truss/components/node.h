#ifndef MAINWINDOW_NODE_H
#define MAINWINDOW_NODE_H

class Node {
public:
    Node(double x, double y, double z, int nodeNum);
    double getX();
    double getY();
    double getZ();
    double norm();
    int getNodeNum();

    Node operator - (const Node& node) const {
        return Node(this->x - node.x, this->y - node.y, this->z - node.z, nodeNum);
    }
    Node operator * (const double toMult) const {
        return Node(this->x * toMult, this->y * toMult, this->z * toMult, nodeNum);
    }
    bool operator == (const Node& node) const {
        return (this->x == node.x && this->y == node.y && this->z == node.z);
    }
private:
    double x = 0;
    double y = 0;
    double z = 0;
    int nodeNum;
};

#endif