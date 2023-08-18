#ifndef MAINWINDOW_MAINCONTENT_H
#define MAINWINDOW_MAINCONTENT_H

#include <QSpinBox>
#include "QVBoxLayout"
#include "QWidget"
#include "QTabWidget"
#include "crane/crane.h"


class CraneTab;

class MainContent : public QWidget {
Q_OBJECT
public:
    explicit MainContent(Crane &crane, QWidget *parent = nullptr);

    void createNewCrane(const QString& name);

    std::tuple <double, double, int, int> getTowerSettings();
    std::tuple <double, double, int, int, bool, bool> getJibSettings();
    std::tuple <double, double, int, int> getCounterjibSettings();
private:
    QTabWidget *renderer = nullptr;
    QGridLayout *mainLayout = nullptr;

};


#endif //MAINWINDOW_MAINCONTENT_H
