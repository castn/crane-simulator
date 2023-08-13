//
// Created by castn on 29.07.23.
//

#include <QLabel>

#include "widget.h"

auto Widget::layoutToWidget(QLayout *layout, QWidget *parent) -> QWidget * {
    auto *widget = new QWidget(parent);
    widget->setLayout(layout);
    return widget;
}

//auto Widget::widgetToLayout(QWidget *widget, QWidget *parent) -> QLayout* {
//    auto *layout = new QLayout(parent);
//    layout
//
//    return nullptr;
//}

auto Widget::createGroupWidget(QLayout *layout, QWidget *parent) -> QGroupBox * {
    auto *box = new QGroupBox(parent);
    box->setLayout(layout);
    return box;
}

auto Widget::createGroupWidget(QLayout *layout, const QString &title, QWidget *parent) -> QGroupBox * {
    auto *box = createGroupWidget(layout, parent);
    box->setTitle(title);
    return box;
}

void Widget::createGridRow(QGridLayout *grid, int row, const QString &label, const QString &toolTip, QWidget *widget,
                           QWidget *parent) {
    auto *rowLabel = new QLabel(label, parent);
    rowLabel->setToolTip(toolTip);

    grid->addWidget(rowLabel, row, 0);
    grid->addWidget(widget, row, 1);
}


