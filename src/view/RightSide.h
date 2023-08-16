#ifndef MAINWINDOW_RIGHTSIDE_H
#define MAINWINDOW_RIGHTSIDE_H


#include <QWidget>
#include <QVTKOpenGLNativeWidget.h>
#include <QVBoxLayout>
#include <vtkPolyData.h>
#include "src/crane/truss/components/beam.h"

class RightSide : public QWidget {
Q_OBJECT
public:
    explicit RightSide(QWidget *parent);
    QVBoxLayout *renderLayout = nullptr;
    void setBeamsToRender(std::vector<Beam> beams);
private:
    auto addRenderer() -> QWidget *;
    vtkNew<vtkPolyData> createBeamPlot();
    std::vector<Beam> beams;
};


#endif //MAINWINDOW_RIGHTSIDE_H
