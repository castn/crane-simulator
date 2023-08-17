//
// Created by carsten on 30.07.23.
//

#ifndef MAINWINDOW_RENDERER_H
#define MAINWINDOW_RENDERER_H


#include <QWidget>
#include <QVTKOpenGLNativeWidget.h>
#include <QVBoxLayout>
#include <vtkPolyData.h>

class Renderer : public QWidget {
Q_OBJECT
public:
    explicit Renderer(QWidget *parent);
    QVBoxLayout *renderLayout = nullptr;

private:
    auto addRenderer() -> QWidget *;
    vtkNew<vtkPolyData> createBeamPlot();
};


#endif //MAINWINDOW_RENDERER_H
