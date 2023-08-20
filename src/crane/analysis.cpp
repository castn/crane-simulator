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
void Analysis::setGravityInfo(int density = 7850, double gravityConst) {
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
        std::cout << "No direction found!\n";
    }
}

void Analysis::generateConditions(std::vector<Node> nodes, std::vector<Beam> beams) {
    this->nodes = nodes;
    this->beams = beams;

    defFixedNodes = {0, 0, 0,
                     0, 0, 0,
                     0, 0, 0,
                     0, 0, 0,};
    
    dofCondition.fill(1);
    areaPerBeam.fill(pow(0.05, 2));
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

bool Analysis::isEulerBucklingRod(int beam, double force) {
    double length = beams.at(beam).getLength();
    double mass = length * areaPerBeam(beam) * density;
    double I = (1 / 12) * mass * pow(length, 2);
    if (force >= (pow(M_PI, 2) / pow(length, 2)) * E * I) {
        return false;
    } else if (force >= ((pow(M_PI, 2)) / pow(0.7 * length, 2)) * E * I) {
        return false;
    }
    return true;
}

std::tuple<Eigen::MatrixXd, Eigen::MatrixXd> Analysis::getDOFs() {
    // converted by Bard so no guarantee that it works
    Eigen::MatrixXd freeDOF = Eigen::MatrixXd::Zero(dofCondition.rows(), dofCondition.cols());
    Eigen::MatrixXd supportDOF = Eigen::MatrixXd::Zero(dofCondition.rows(), dofCondition.cols());

    for (int i = 0; i < dofCondition.rows(); i++) {
        if (dofCondition(i, i) != 0) {
        freeDOF(i, i) = 1;
        } else {
        supportDOF(i, i) = 1;
        }
    }

    return std::make_tuple(freeDOF, supportDOF);
}
void Analysis::calculateReactionForces() {

}
Eigen::MatrixXd Analysis::calculateDeformation(Eigen::MatrixXd defFreeNodes, std::vector<Beam> beams, int dof, Eigen::MatrixXd freeDOF, int numNodes, Eigen::MatrixXd supportDOF) {
    // Eigen::MatrixXd deformation = Eigen::MatrixXd::Zero(numNodes, dof);

    // // Set the deformations of the free nodes.
    // deformation[freeDOF] = defFreeNodes;

    // // Set the deformations of the fixed nodes to 0.
    // deformation[supportDOF] = Eigen::MatrixXd::Zero(supportDOF.rows(), dof);

    // // Combine the deformations of the two nodes in each beam.
    // for (int i = 0; i < beams.size(); i++) {
    //     auto node1 = beams.at(i).getStart();
    //     auto node2 = beams.at(i).getEnd();
    //     int node1_row = node1.operator[]();
    //     int node2_row = node2.operator[]();
    //     deformation.row(node1_row) = (deformation.row(node1_row) + deformation.row(node2_row)) / 2;
    // }

    // return deformation;
}
void Analysis::calculateGlobalStiffness() {

}
std::tuple<Eigen::MatrixXd, Eigen::MatrixXd, Eigen::MatrixXd> Analysis::getComponentsOfGlobalStiffness(Eigen::MatrixXd K, Eigen::MatrixXd freeDOF, Eigen::MatrixXd supportDOF) {
    Eigen::MatrixXd KTopLeft = K.block(freeDOF.rows(), 0, freeDOF.rows(), freeDOF.rows());
    Eigen::MatrixXd KTopRight = K.block(freeDOF.rows(), freeDOF.rows(), supportDOF.rows(), supportDOF.rows());
    Eigen::MatrixXd KBottomLeft = KTopRight.transpose();
    Eigen::MatrixXd KBottomRight = K.block(freeDOF.rows(), supportDOF.rows(), freeDOF.rows(), supportDOF.rows());

    return std::make_tuple(KBottomLeft, KBottomRight, KTopLeft);
}

void Analysis::optimize() {

}