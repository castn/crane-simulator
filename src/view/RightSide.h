//
// Created by carsten on 30.07.23.
//

#ifndef MAINWINDOW_RIGHTSIDE_H
#define MAINWINDOW_RIGHTSIDE_H


#include <QWidget>
#include <QVTKOpenGLNativeWidget.h>
#include <QVBoxLayout>
#include <vtkPolyData.h>

class RightSide : public QWidget {
Q_OBJECT
public:
    explicit RightSide(QWidget *parent);
    QVBoxLayout *renderLayout = nullptr;

private:
    auto addRenderer() -> QWidget *;
    vtkNew<vtkPolyData> createBeamPlot();
};


#endif //MAINWINDOW_RIGHTSIDE_H
