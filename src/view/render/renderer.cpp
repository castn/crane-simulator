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
        std::cout << "Beams haven't been set yet!\n";
        // return polyData;
        // beams.clear();
        // beams.push_back(Beam(Node(0, 0, 0, 0), Node(10, 0, 0, 1)));
        // beams.push_back(Beam(Node(10, 0, 0, 2), Node(10, 10, 0, 3)));
        // beams.push_back(Beam(Node(10, 10, 0, 4), Node(0, 10, 0, 5)));
        // beams.push_back(Beam(Node(0, 10, 0, 6), Node(0, 0, 0, 7)));
        // beams.push_back(Beam(Node(0, 0, 0, 8), Node(0, 0, 10, 9)));
        // beams.push_back(Beam(Node(10, 0, 0, 10), Node(10, 0, 10, 11)));
        // beams.push_back(Beam(Node(10, 10, 0, 12), Node(10, 0, 10, 13)));
        // beams.push_back(Beam(Node(0, 10, 0, 14), Node(10, 0, 10, 15)));
        // beams.push_back(Beam(Node(0, 0, 10, 16), Node(10, 0, 10, 17)));
        // beams.push_back(Beam(Node(10, 0, 10, 18), Node(10, 10, 10, 19)));
        // beams.push_back(Beam(Node(10, 10, 10, 20), Node(0, 10, 10, 21)));
        // beams.push_back(Beam(Node(0, 10, 10, 22), Node(0, 0, 10, 23)));
    }

    // Create a vtkPoints object and store the points in it
    vtkNew<vtkPoints> points;
    vtkNew<vtkPolyLine> polyLine;
    // polyLine->GetPointIds()->SetNumberOfIds((int)beams.size());
    polyLine->GetPointIds()->SetNumberOfIds(24);
    points->InsertNextPoint(0, 0, 0);
    points->InsertNextPoint(10, 0, 0);
    polyLine->GetPointIds()->SetId(0, 1);
    points->InsertNextPoint(10, 0, 0);
    points->InsertNextPoint(10, 10, 0);
    polyLine->GetPointIds()->SetId(2, 3);
    points->InsertNextPoint(10, 10, 0);
    points->InsertNextPoint(0, 10, 0);
    polyLine->GetPointIds()->SetId(4, 5);
    points->InsertNextPoint(0, 10, 0);
    points->InsertNextPoint(0, 0, 0);
    polyLine->GetPointIds()->SetId(6, 7);
    points->InsertNextPoint(0, 0, 0);
    points->InsertNextPoint(0, 0, 10);
    polyLine->GetPointIds()->SetId(8, 9);
    points->InsertNextPoint(10, 0, 0);
    points->InsertNextPoint(10, 0, 10);
    polyLine->GetPointIds()->SetId(10, 11);
    points->InsertNextPoint(10, 10, 0);
    points->InsertNextPoint(10, 10, 10);
    polyLine->GetPointIds()->SetId(12, 13);
    points->InsertNextPoint(0, 10, 0);
    points->InsertNextPoint(0, 10, 10);
    polyLine->GetPointIds()->SetId(14, 15);
    points->InsertNextPoint(0, 0, 10);
    points->InsertNextPoint(10, 0, 10);
    polyLine->GetPointIds()->SetId(16, 17);
    points->InsertNextPoint(10, 0, 10);
    points->InsertNextPoint(10, 10, 10);
    polyLine->GetPointIds()->SetId(18, 19);
    points->InsertNextPoint(10, 10, 10);
    points->InsertNextPoint(0, 10, 10);
    polyLine->GetPointIds()->SetId(20, 21);
    points->InsertNextPoint(0, 10, 10);
    points->InsertNextPoint(0, 0, 10);
    polyLine->GetPointIds()->SetId(22, 23);

    // for (unsigned int i = 0; i < beams.size(); i++) {
    //     Node startNode = beams.at(i).getStart();
    //     Node endNode = beams.at(i).getEnd();

    //     points->InsertNextPoint(startNode.getX(), startNode.getY(), startNode.getZ());
    //     points->InsertNextPoint(endNode.getX(), endNode.getY(), endNode.getZ());

    //     polyLine->GetPointIds()->SetId(2 * i, 2 * i + 1); //(idLoc, idLoc + 1)
    //     // idLoc += 2;
    // }

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
