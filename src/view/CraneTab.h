//
// Created by castn on 28.07.23.
//

#ifndef MAINWINDOW_CRANETAB_H
#define MAINWINDOW_CRANETAB_H


#include <QWidget>
#include <QGridLayout>
#include <tuple>
#include "LeftSide.h"
#include "RightSide.h"

class CraneTab : public QWidget {
Q_OBJECT
public:
    explicit CraneTab(QWidget *parent);
    QVBoxLayout *tabLayout = nullptr;

    std::tuple <double, double, int, int> getTowerSettings();
    std::tuple <double, double, int, int, bool, bool> getJibSettings();
    std::tuple <double, double, int, int> getCounterjibSettings();
private:
    LeftSide *leftSide = nullptr;
    RightSide *rightSide = nullptr;
};


#endif //MAINWINDOW_CRANETAB_H
