#ifndef MAINWINDOW_RENDERER_H
#define MAINWINDOW_RENDERER_H


#include <QWidget>
#include <QVTKOpenGLNativeWidget.h>
#include <QVBoxLayout>
#include <vtkPolyData.h>
#include "src/crane/truss/components/beam.h"

class Renderer : public QWidget {
Q_OBJECT
public:
    explicit Renderer(QWidget *parent);
    QVBoxLayout *renderLayout = nullptr;
    void setBeamsToRender(std::vector<Beam> beams);
    vtkNew<vtkPolyData> createBeamPlot();
private:
    auto addRenderer() -> QWidget *;
    std::vector<Beam> beams;
};


#endif //MAINWINDOW_RENDERER_H
