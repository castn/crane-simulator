//
// Created by castn on 30.07.23.
//

#ifndef MAINWINDOW_TOWERSETTINGS_H
#define MAINWINDOW_TOWERSETTINGS_H


#include <QWidget>
#include <QSpinBox>
#include <QComboBox>
#include <QLabel>
#include <QGroupBox>
#include <QGridLayout>

class TowerSettings : public QWidget {
Q_OBJECT
public:
    explicit TowerSettings(QWidget *parent);

    QGroupBox *towerSettings = nullptr;

    int getHeight();
    int getWidth();
    int getSegs();
    int getSupType();
private:
    QSpinBox *towerHeight = nullptr;
    QSpinBox *towerWidth = nullptr;
    QSpinBox *towerSegments = nullptr;
    QComboBox *towerSupportType = nullptr;

    QLayout *createSettings();
};


#endif //MAINWINDOW_TOWERSETTINGS_H
