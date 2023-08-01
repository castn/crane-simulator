//
// Created by castn on 29.07.23.
//

#ifndef MAINWINDOW_WIDGET_H
#define MAINWINDOW_WIDGET_H


#include <QWidget>
#include <QGroupBox>
#include <QLayout>

class Widget {

public:
    static auto layoutToWidget(QLayout *layout, QWidget *parent) -> QWidget *;

    //static auto widgetToLayout(QWidget *widget, QWidget *parent) -> QLayout *;

    static auto createGroupWidget(QLayout *layout, QWidget *parent) -> QGroupBox *;

    static auto createGroupWidget(QLayout *layout, const QString &title,
                                  QWidget *parent) -> QGroupBox *;

    static void createGridRow(QGridLayout *grid, int row, const QString &label, const QString &toolTip,
                              QWidget *widget, QWidget *parent);

};


#endif //MAINWINDOW_WIDGET_H
