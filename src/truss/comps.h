#ifndef MAINWINDOW_COMPS_H
#define MAINWINDOW_COMPS_H

#include "node.h"
#include "beam.h"
#include <vector>


class Comps {
public:
    std::vector<Node> nodes;
    std::vector<Beam> beams;
};

#endif //MAINWINDOW_COMPS_H