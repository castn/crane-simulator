//
// Created by carsten on 30.07.23.
//

#ifndef MAINWINDOW_LEFTSIDE_H
#define MAINWINDOW_LEFTSIDE_H


#include <QWidget>
#include <QGridLayout>
#include <QSpinBox>
#include <QComboBox>

class LeftSide : public QWidget{
Q_OBJECT
public:
    explicit LeftSide(QWidget *parent);
    QVBoxLayout *leftLayout = nullptr;


};


#endif //MAINWINDOW_LEFTSIDE_H
