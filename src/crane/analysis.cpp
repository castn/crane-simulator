#include "analysis.h"
#include <iostream>
#include "truss/components/node.h"
#include "truss/components/beam.h"
#include <Eigen/Dense>

void Analysis::analyze() {

}
void Analysis::applyForces(std::vector<Node> nodes, int towerEnd, int jibEnd, int jibBaseEnd,
                           int cjEnd, int cjBaseEnd, double jibLeftForce, double jibRightForce,
                           double cjLeftForce, double cjRightForce) {
    this->nodes = nodes;
    this->towerEnd = towerEnd;
    this->jibEnd = jibEnd;
    this->jibBaseEnd = jibBaseEnd;
    this->cjEnd = cjEnd;
    this->cjBaseEnd = cjBaseEnd;

    resetForces(jibLeftForce, jibRightForce, cjLeftForce, cjRightForce);
}
void Analysis::resetForces(double jibLeftForce, double jibRightForce, double cjLeftForce,
                           double cjRightForce) {
    int nodesSize = nodes.size();
    Eigen::Matrix<double, Eigen::Dynamic, 3> p;
    p.fill(0.0);

    p(jibBaseEnd - 2, 2) += jibLeftForce;
    p(jibBaseEnd - 1, 2) += jibRightForce;
    p(cjBaseEnd - 2, 2) += cjLeftForce;
    p(cjBaseEnd - 1, 2) += cjRightForce;

    forces = p;
}
void Analysis::setGravityInfo(int density, double gravityConst) {
    this->density = density;
    this->gravityConst = gravityConst;
}
void Analysis::applyGravity() {

}
void Analysis::applyHorizontalForces(int direction, double force, int cjSupType) {
    force = force * kN;
    switch (direction)
    {
    case 0:
        applyHorizontalForcesFromFront(force, cjSupType);
        break;
    case 1:
        applyHorizontalForcesFromBack(force, cjSupType);
        break;
    case 2:
        applyHorizontalForcesFromLeft(force, cjSupType);
        break;
    case 3:
        applyHorizontalForcesFromRight(force);
        break;
    default:
        std::cout << "No direction found!";
    }
}

void Analysis::generateConditions(std::vector<Node> nodes) {
    this->nodes = nodes;

    defFixedNodes = {0, 0, 0,
                     0, 0, 0,
                     0, 0, 0,
                     0, 0, 0,};
    
    Eigen::Matrix<int, Eigen::Dynamic, 3> dofCondition;
    dofCondition.fill(1);
}
    
void Analysis::applyHorizontalForcesFromFront(double force, int cjSupType) {
    for (int tN = 0; tN < towerEnd / 2; tN++) {
        forces(1 + 2 * tN, 1) += force;
    }
    for (int jN = towerEnd; jN < jibEnd / 30; jN++) {
        forces(0 + 3 * jN, 1) += force;
        forces(2 + 3 * jN, 1) += force;
    }
    for (int cjN = jibEnd; cjN < cjBaseEnd / 2; cjN++) {
        forces(jibEnd + (1 + 2 * cjN), 1) += force;
    }
    if (cjSupType == 1) {
        for (int cjN = cjBaseEnd; cjN < cjEnd; cjN++) {
            forces(cjN, 1) += force;
        }
    } else if (cjSupType == 2) {
        forces(cjBaseEnd, 1) += force;
    }
}
void Analysis::applyHorizontalForcesFromBack(double force, int cjSupType) {
    for (int tN = 0; tN < towerEnd / 2; tN++) {
        forces(2 * tN, 1) -= force;
    }
    for (int jN = towerEnd; jN < jibEnd / 30; jN++) {
        forces(0 + 3 * jN, 1) -= force;
        forces(1 + 3 * jN, 1) -= force;
    }
    for (int cjN = jibEnd; cjN < cjBaseEnd / 2; cjN++) {
        forces(jibEnd + (0 + 2 * cjN), 1) -= force;
    }
    if (cjSupType == 1) {
        for (int cjN = cjBaseEnd; cjN < cjEnd; cjN++) {
            forces(cjN, 1) -= force;
        }
    } else if (cjSupType == 2) {
        forces(cjBaseEnd, 1) -= force;
    }
}
void Analysis::applyHorizontalForcesFromLeft(double force, int cjSupType) {
    for (int tN = 0; tN < (towerEnd / 4) - 1; tN++) {
        forces(0 + 4 * tN, 0) += force;
        forces(1 + 4 * tN, 0) += force;
    }
    forces(cjBaseEnd - 2, 0) += force;
    forces(cjBaseEnd - 1, 0) += force;
    if (cjSupType == 1 || cjSupType == 2) {
        forces(cjEnd - 1, 0) += force;
    }
}
void Analysis::applyHorizontalForcesFromRight(double force) {
    for (int tN = 0; tN < (towerEnd / 4) - 1; tN++) {
        forces(2 + 4 * tN, 0) -= force;
        forces(3 + 4 * tN, 0) -= force;
    }
    for (int jN = jibEnd - 3; jN < jibEnd; jN++) {
        forces(jN, 0) -= force;
    }
}

bool Analysis::isEulerBucklingRod() {
    return false;
}

void Analysis::getDOFs() {

}
void Analysis::calculateReactionForces() {

}
void Analysis::calculateDeformation() {

}
void Analysis::calculateGlobalStiffness() {

}
void Analysis::getComponentsOfGlobalStiffness() {

}

void Analysis::optimize() {

}