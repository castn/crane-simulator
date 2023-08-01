//
// Created by castn on 01.08.23.
//

#ifndef MAINWINDOW_JIBSETTINGS_H
#define MAINWINDOW_JIBSETTINGS_H


#include <QWidget>
#include <QSpinBox>
#include <QComboBox>
#include <QGroupBox>
#include <QCheckBox>

class JibSettings : public QWidget {
Q_OBJECT
public:
    explicit JibSettings(QWidget *parent);

    QGroupBox *jibSettings = nullptr;

private:
    QSpinBox *jibLength = nullptr;
    QSpinBox *jibHeight = nullptr;
    QSpinBox *jibSegments = nullptr;
    QComboBox *jibSupportType = nullptr;
    QCheckBox *heightDegrease = nullptr;
    QCheckBox *upwardBend = nullptr;

    QLayout *createSettings();
};


#endif //MAINWINDOW_JIBSETTINGS_H
