//
// Created by castn on 28.07.23.
//

#ifndef MAINWINDOW_CRANESETTINGS_H
#define MAINWINDOW_CRANESETTINGS_H


#include <QWidget>
#include <QVBoxLayout>

class CraneSettings : public QWidget {
Q_OBJECT
public:
    explicit CraneSettings(QWidget *parent);
    QVBoxLayout *settingsLayout = nullptr;

};


#endif //MAINWINDOW_CRANESETTINGS_H
