#ifndef MAINWINDOW_MAINCONTENT_H
#define MAINWINDOW_MAINCONTENT_H

#include <QSpinBox>
#include "QVBoxLayout"
#include "QWidget"
#include "QTabWidget"
#include "crane/crane.h"
#include "view/settings/cranesettings.h"


class CraneTab;
class CraneSettings;
class Renderer;

class MainContent : public QWidget {
Q_OBJECT
public:
    explicit MainContent(Crane &crane, QWidget *parent = nullptr);

    void createNewCrane(const QString& name);

    std::tuple <int, int, int, int> getTowerSettings();
    std::tuple <int, int, int, int, bool, bool> getJibSettings();
    std::tuple <int, int, int, int> getCounterjibSettings();
private:
    Renderer *renderer = nullptr;
    QGridLayout *mainLayout = nullptr;
    CraneSettings *craneSettings = nullptr;
};


#endif //MAINWINDOW_MAINCONTENT_H
