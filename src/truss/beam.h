#ifndef MAINWINDOW_BEAM_H
#define MAINWINDOW_BEAM_H

#include "node.h"
#include <vector>


class Beam {
public:
    Beam(Node start, Node end);
    double getLength();
private:
    Node *startNode = nullptr;
    Node *endNode = nullptr;
    double length;
};

#endif