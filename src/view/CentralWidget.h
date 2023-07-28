//
// Created by carsten on 28.07.23.
//

#ifndef MAINWINDOW_CENTRALWIDGET_H
#define MAINWINDOW_CENTRALWIDGET_H

#include "QVBoxLayout"
#include "QWidget"
#include "QTabWidget"

class CentralWidget : public QWidget {
Q_OBJECT
public:
    explicit CentralWidget(QWidget *parent);

    void createNewCrane(const QString& name);

private:
    QTabWidget *tabs = nullptr;
    QVBoxLayout *centralLayout = nullptr;
};


#endif //MAINWINDOW_CENTRALWIDGET_H
