//
// Created by castn on 30.07.23.
//

#ifndef MAINWINDOW_COUNTERJIBSETTINGS_H
#define MAINWINDOW_COUNTERJIBSETTINGS_H


#include <QWidget>
#include <QGroupBox>
#include <QSpinBox>
#include <QComboBox>

class CounterjibSettings : public QWidget {
Q_OBJECT
public:
    explicit CounterjibSettings(QWidget *parent);

    QGroupBox *counterjibSettings = nullptr;

    int getLength();
    int getHeight();
    int getSegs();
    int getSupType();
private:
    QSpinBox *counterjibLength = nullptr;
    QSpinBox *counterjibHeight = nullptr;
    QSpinBox *counterjibSegments = nullptr;
    QComboBox *counterjibSupportType = nullptr;

    QLayout *createSettings();
};


#endif //MAINWINDOW_COUNTERJIBSETTINGS_H
