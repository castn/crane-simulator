#ifndef MAINWINDOW_CRANESETTINGS_H
#define MAINWINDOW_CRANESETTINGS_H


#include <QWidget>
#include <QGridLayout>
#include <QSpinBox>
#include <QComboBox>
#include <QPushButton>
#include <tuple>
#include <QCheckBox>
#include "mainwindow.h"

class CraneSettings : public QWidget {
Q_OBJECT
public:
    explicit CraneSettings(Crane &crane, QWidget *parent);

    QVBoxLayout *settingsLayout = nullptr;

    std::tuple<int, int, int, int> getTowerSettings();

    std::tuple<int, int, int, int, bool, bool> getJibSettings();

    std::tuple<int, int, int, int> getCounterjibSettings();

    void connectApply();

private:
    QSpinBox *towerHeight = nullptr;
    QSpinBox *towerWidth = nullptr;
    QSpinBox *towerSegments = nullptr;
    QComboBox *towerSupportType = nullptr;
    QSpinBox *jibLength = nullptr;
    QSpinBox *jibHeight = nullptr;
    QSpinBox *jibSegments = nullptr;
    QComboBox *jibSupportType = nullptr;
    QCheckBox *heightDropdown = nullptr;
    QCheckBox *upwardBend = nullptr;
    QSpinBox *counterjibLength = nullptr;
    QSpinBox *counterjibHeight = nullptr;
    QSpinBox *counterjibSegments = nullptr;
    QComboBox *counterjibSupportType = nullptr;

    QPushButton *applyButton = nullptr;
};


#endif //MAINWINDOW_CRANESETTINGS_H
