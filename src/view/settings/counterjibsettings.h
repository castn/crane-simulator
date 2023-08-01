//
// Created by castn on 30.07.23.
//

#ifndef MAINWINDOW_COUNTERJIBSETTINGS_H
#define MAINWINDOW_COUNTERJIBSETTINGS_H


#include <QWidget>
#include <QGroupBox>
#include <QSpinBox>
#include <QComboBox>

class CounterJibSettings : public QWidget {
Q_OBJECT
public:
    explicit CounterJibSettings(QWidget *parent);

    QGroupBox *counterjibSettings = nullptr;
private:
    QSpinBox *counterjibLength = nullptr;
    QSpinBox *counterjibWidth = nullptr;
    QSpinBox *counterjibSegments = nullptr;
    QComboBox *counterjibSupportType = nullptr;

    QLayout *createSettings();
};


#endif //MAINWINDOW_COUNTERJIBSETTINGS_H
