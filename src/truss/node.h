#ifndef MAINWINDOW_NODE_H
#define MAINWINDOW_NODE_H

class Node {
public:
    Node(double x, double y, double z);
    double getX();
    double getY();
    double getZ();
private:
    double x;
    double y;
    double z;
};

#endif