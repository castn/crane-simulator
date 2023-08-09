#ifndef MAINWINDOW_COMPS_H
#define MAINWINDOW_COMPS_H

#include <vector>
#include "beam.h"


class Comps {
public:
    std::vector<std::vector<double>> nodes;
    std::vector<Beam> beams;
};


#endif //MAINWINDOW_COMPS_H