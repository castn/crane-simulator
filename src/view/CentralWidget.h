//
// Created by carsten on 28.07.23.
//

#ifndef MAINWINDOW_CENTRALWIDGET_H
#define MAINWINDOW_CENTRALWIDGET_H

#include "QVBoxLayout"
#include "QWidget"
#include "QTabWidget"
#include "src/view/CraneTab.h"

class CentralWidget : public QWidget {
Q_OBJECT
public:
    explicit CentralWidget(QWidget *parent);

    void createNewCrane(const QString& name);

    std::tuple <double, double, int, int> getTowerSettings();
    std::tuple <double, double, int, int, bool, bool> getJibSettings();
    std::tuple <double, double, int, int> getCounterjibSettings();
private:
    QTabWidget *tabs = nullptr;
    QVBoxLayout *centralLayout = nullptr;
    CraneTab *craneTab = nullptr;
};


#endif //MAINWINDOW_CENTRALWIDGET_H
