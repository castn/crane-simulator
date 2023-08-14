#ifndef MAINWINDOW_LEFTSIDE_H
#define MAINWINDOW_LEFTSIDE_H


#include <QWidget>
#include <QGridLayout>
#include <QSpinBox>
#include <QComboBox>
#include <tuple>
#include "src/view/settings/towersettings.h"
#include "src/view/settings/jibsettings.h"
#include "src/view/settings/counterjibsettings.h"

class LeftSide : public QWidget{
Q_OBJECT
public:
    explicit LeftSide(QWidget *parent);
    QVBoxLayout *leftLayout = nullptr;

    std::tuple <int, int, int, int> getTowerSettings();
    std::tuple <int, int, int, int, bool, bool> getJibSettings();
    std::tuple <int, int, int, int> getCounterjibSettings();
private:
    TowerSettings *towerSettings = nullptr;
    JibSettings *jibSettings = nullptr;
    CounterjibSettings *counterjibSettings = nullptr;
};


#endif //MAINWINDOW_LEFTSIDE_H
