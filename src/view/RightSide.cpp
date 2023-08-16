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
#include "src/crane/truss/components/beam.h"
#include "src/crane/truss/components/node.h"

RightSide::RightSide(QWidget *parent) : QWidget(parent) {
    renderLayout = new QVBoxLayout(this);
    renderLayout->addWidget(addRenderer());
}

auto RightSide::addRenderer() -> QWidget * {
    QPointer<QVTKOpenGLNativeWidget> vtkRenderWidget = new QVTKOpenGLNativeWidget(this);
    // VTK part
    vtkNew<vtkGenericOpenGLRenderWindow> window;
    vtkRenderWidget->setRenderWindow(window.Get());

    // vtkNew<vtkSphereSource> sphere;
    // sphere->SetRadius(1.0);
    // sphere->SetThetaResolution(100);
    // sphere->SetPhiResolution(100);

    auto polyData = createBeamPlot();

    // Setup actor and mapper
    vtkNew<vtkPolyDataMapper> mapper;
    mapper->SetInputData(polyData);

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
    if (beams.empty()) {
        std::cout << "Beams haven't been set yet!";
        return;
    }

    // Create five points.
    // double origin[3] = {0.0, 0.0, 0.0};
    // double p0[3] = {1.0, 0.0, 0.0};
    // double p1[3] = {0.0, 1.0, 0.0};
    // double p2[3] = {0.0, 1.0, 2.0};
    // double p3[3] = {1.0, 2.0, 3.0};

    // Create a vtkPoints object and store the points in it
    vtkNew<vtkPoints> points;
    vtkNew<vtkPolyLine> polyLine;
    polyLine->GetPointIds()->SetNumberOfIds(beams.size());
    // points->InsertNextPoint(origin);
    // points->InsertNextPoint(p0);
    // points->InsertNextPoint(p1);
    // points->InsertNextPoint(p2);
    // points->InsertNextPoint(p3);
    // int idLoc = 0;

    for (unsigned int i = 0; i < beams.size(); i++) {
        Node startNode = beams.at(i).getStart();
        Node endNode = beams.at(i).getEnd();

        points->InsertNextPoint(startNode.getX(), startNode.getY(), startNode.getZ());
        points->InsertNextPoint(endNode.getX(), endNode.getY(), endNode.getZ());

        polyLine->GetPointIds()->SetId(2 * i, 2 * i + 1); //(idLoc, idLoc + 1)
        // idLoc += 2;
    }

    
    // polyLine->GetPointIds()->SetNumberOfIds(5);
    // for (unsigned int i = 0; i < 5; i++)
    // {
    //     polyLine->GetPointIds()->SetId(i, i);
    // }

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

void RightSide::setBeamsToRender(std::vector<Beam> beams) {
    this->beams = beams;
}
