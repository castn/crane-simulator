//
// Created by carsten on 29.07.23.
//

#ifndef MAINWINDOW_CRANE_H
#define MAINWINDOW_CRANE_H


#include "tower.h"
#include "jib.h"

class Crane {
public:
    Crane();

    Tower *tower = nullptr;

    Jib *jib = nullptr;
private:


};


#endif //MAINWINDOW_CRANE_H
