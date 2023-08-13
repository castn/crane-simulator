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

    double getLength();
    double getWidth();
    int getSegs();
    int getSupType();
private:
    QDoubleSpinBox *counterjibLength = nullptr;
    QDoubleSpinBox *counterjibWidth = nullptr;
    QSpinBox *counterjibSegments = nullptr;
    QComboBox *counterjibSupportType = nullptr;

    QLayout *createSettings();
};


#endif //MAINWINDOW_COUNTERJIBSETTINGS_H
