#include "beam.h"
#include "node.h"

Beam::Beam(Node start, Node end){
    startNode = &start;
    endNode = &end;
    length = (end - start).norm();
}

double Beam::getLength() {
    return length;
}