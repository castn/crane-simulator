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
#include "renderer.h"

Renderer::Renderer(QWidget *parent) : QWidget(parent) {
    renderLayout = new QVBoxLayout(this);
    renderLayout->addWidget(addRenderer());
}

auto Renderer::addRenderer() -> QWidget * {
    QPointer<QVTKOpenGLNativeWidget> vtkRenderWidget = new QVTKOpenGLNativeWidget(this);
    // VTK part
    vtkNew<vtkGenericOpenGLRenderWindow> window;
    vtkRenderWidget->setRenderWindow(window.Get());

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

vtkNew<vtkPolyData> Renderer::createBeamPlot() {
    // Create a polydata to store everything in
    vtkNew<vtkPolyData> polyData;

    if (beams.empty()) {
        std::cout << "Beams haven't been set yet!";
        return polyData;
    }

    // Create a vtkPoints object and store the points in it
    vtkNew<vtkPoints> points;
    vtkNew<vtkPolyLine> polyLine;
    polyLine->GetPointIds()->SetNumberOfIds(beams.size());

    for (unsigned int i = 0; i < beams.size(); i++) {
        Node startNode = beams.at(i).getStart();
        Node endNode = beams.at(i).getEnd();

        points->InsertNextPoint(startNode.getX(), startNode.getY(), startNode.getZ());
        points->InsertNextPoint(endNode.getX(), endNode.getY(), endNode.getZ());

        polyLine->GetPointIds()->SetId(2 * i, 2 * i + 1); //(idLoc, idLoc + 1)
        // idLoc += 2;
    }

    // Create a cell array to store the lines in and add the lines to it
    vtkNew<vtkCellArray> cells;
    cells->InsertNextCell(polyLine);

    // Add the points to the dataset
    polyData->SetPoints(points);

    // Add the lines to the dataset
    polyData->SetLines(cells);

    return polyData;
}

void Renderer::setBeamsToRender(std::vector<Beam> beams) {
    this->beams = beams;
}
