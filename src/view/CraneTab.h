//
// Created by castn on 28.07.23.
//

#ifndef MAINWINDOW_CRANETAB_H
#define MAINWINDOW_CRANETAB_H


#include <QWidget>
#include <QGridLayout>

class CraneTab : public QWidget {
Q_OBJECT
public:
    explicit CraneTab(QWidget *parent);
    QVBoxLayout *tabLayout = nullptr;
};


#endif //MAINWINDOW_CRANETAB_H
