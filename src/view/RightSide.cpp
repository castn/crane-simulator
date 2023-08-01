//
// Created by carsten on 30.07.23.
//

#include <vtkActor.h>
#include <vtkDataSetMapper.h>
#include <vtkDoubleArray.h>
#include <vtkGenericOpenGLRenderWindow.h>
#include <vtkPointData.h>
#include <vtkProperty.h>
#include <vtkRenderer.h>
#include <vtkSphereSource.h>
#include <QPointer>
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

    vtkNew<vtkDataSetMapper> mapper;
    mapper->SetInputConnection(sphere->GetOutputPort());

    vtkNew<vtkActor> actor;
    actor->SetMapper(mapper);
    actor->GetProperty()->SetEdgeVisibility(true);
    actor->GetProperty()->SetRepresentationToSurface();

    vtkNew<vtkRenderer> renderer;
    renderer->AddActor(actor);

    window->AddRenderer(renderer);

    return vtkRenderWidget;
}
