#ifndef MAINWINDOW_BEAM_H
#define MAINWINDOW_BEAM_H

#include "node.h"
#include <vector>

class Beam {
public:
    Beam(Node start, Node end);
    double getLength();
    Node getStart();
    Node getEnd();

    Beam operator * (const double toMult) const {
        return Beam(this->startNode * toMult, this->endNode * toMult);
    }
private:
    Node startNode = Node(0, 0, 0, 0);
    Node endNode = Node(0, 0, 0, 0);
    double length;
};

#endif