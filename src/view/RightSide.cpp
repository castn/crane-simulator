//
// Created by carsten on 30.07.23.
//

#include <vtkActor.h>
#include <vtkDataSetMapper.h>
#include <vtkPolyDataMapper.h>
#include <vtkDoubleArray.h>
#include <vtkGenericOpenGLRenderWindow.h>
#include <vtkPointData.h>
#include <vtkProperty.h>
#include <vtkRenderer.h>
#include <vtkSphereSource.h>
#include <QPointer>
#include <vtkCellArray.h>
#include <vtkPolyLine.h>
#include "RightSide.h"

RightSide::RightSide(QWidget *parent) : QWidget(parent) {
    renderLayout = new QVBoxLayout(this);
    renderLayout->addWidget(addRenderer());
}

auto RightSide::addRenderer() -> QWidget * {
    QPointer<QVTKOpenGLNativeWidget> vtkRenderWidget = new QVTKOpenGLNativeWidget(this);
    // VTK part
    vtkNew<vtkGenericOpenGLRenderWindow> window;
    vtkRenderWidget->setRenderWindow(window.Get());

    vtkNew<vtkSphereSource> sphere;
    sphere->SetRadius(1.0);
    sphere->SetThetaResolution(100);
    sphere->SetPhiResolution(100);

    // Create five points.
    double origin[3] = {0.0, 0.0, 0.0};
    double p0[3] = {1.0, 0.0, 0.0};
    double p1[3] = {0.0, 1.0, 0.0};
    double p2[3] = {0.0, 1.0, 2.0};
    double p3[3] = {1.0, 2.0, 3.0};

    auto polyData = createBeamPlot();

    // Setup actor and mapper
    vtkNew<vtkPolyDataMapper> mapper;
    mapper->SetInputData(polyData);

    // Setup render window, renderer, and interactor
//    vtkNew<vtkRenderer> renderer;
//    vtkNew<vtkRenderWindow> renderWindow;
//    renderWindow->SetWindowName("PolyLine");
//    renderWindow->AddRenderer(renderer);
//    vtkNew<vtkRenderWindowInteractor> renderWindowInteractor;
//    renderWindowInteractor->SetRenderWindow(renderWindow);
//    renderer->AddActor(actor);

//    renderWindow->Render();
//    renderWindowInteractor->Start();

//    vtkNew<vtkDataSetMapper> mapper;
//    mapper->SetInputConnection(sphere->GetOutputPort());

    vtkNew<vtkActor> actor;
    actor->SetMapper(mapper);
    actor->GetProperty()->SetEdgeVisibility(true);
    actor->GetProperty()->SetRepresentationToSurface();

    vtkNew<vtkRenderer> renderer;
    renderer->AddActor(actor);

    window->AddRenderer(renderer);

    return vtkRenderWidget;
}

vtkNew<vtkPolyData> RightSide::createBeamPlot() {
    // Create five points.
    double origin[3] = {0.0, 0.0, 0.0};
    double p0[3] = {1.0, 0.0, 0.0};
    double p1[3] = {0.0, 1.0, 0.0};
    double p2[3] = {0.0, 1.0, 2.0};
    double p3[3] = {1.0, 2.0, 3.0};

    // Create a vtkPoints object and store the points in it
    vtkNew<vtkPoints> points;
    points->InsertNextPoint(origin);
    points->InsertNextPoint(p0);
    points->InsertNextPoint(p1);
    points->InsertNextPoint(p2);
    points->InsertNextPoint(p3);

    vtkNew<vtkPolyLine> polyLine;
    polyLine->GetPointIds()->SetNumberOfIds(5);
    for (unsigned int i = 0; i < 5; i++)
    {
        polyLine->GetPointIds()->SetId(i, i);
    }

    // Create a cell array to store the lines in and add the lines to it
    vtkNew<vtkCellArray> cells;
    cells->InsertNextCell(polyLine);

    // Create a polydata to store everything in
    vtkNew<vtkPolyData> polyData;

    // Add the points to the dataset
    polyData->SetPoints(points);

    // Add the lines to the dataset
    polyData->SetLines(cells);

    return polyData;
}
