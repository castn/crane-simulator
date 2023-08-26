#include "analysis.h"
#include <iostream>
#include "truss/components/node.h"
#include "truss/components/beam.h"
#include <Eigen/Dense>

std::tuple<Eigen::VectorXd, Eigen::VectorXd, Eigen::VectorXi> Analysis::analyze() {
    int numNodes = nodes.size();
    int numBeams = beams.size();
    // Degrees of freedom
    int DOF = 3;
    int totalNumOfDOF = DOF * numNodes;
    auto DOFs = getDOFs();
    auto freeDOF = std::get<0>(DOFs);
    auto supportDOF = std::get<1>(DOFs);
    // Structural analysis
    Eigen::VectorXd distance;
    for (int i = 0; i < numBeams; i++) {
        distance(i) = beams.at(i).getLength();
    }
    auto L = distance; //???
    auto rotation = distance.transpose().array() / L.array();
    Eigen::VectorXd transformationVector;
    transformationVector << - rotation.transpose(), rotation.transpose();
    // Stiffness
    auto K = calculateGlobalStiffness(DOF, numBeams, totalNumOfDOF);
    auto Kcomps = getComponentsOfGlobalStiffness(K, freeDOF, supportDOF);
    auto KBottomLeft = std::get<0>(Kcomps);
    auto KBottomRight = std::get<1>(Kcomps);
    auto KTopLeft = std::get<2>(Kcomps);
    // Temp for return so no errors
    Eigen::VectorXd axialForce;
    Eigen::VectorXd reactionForce;
    Eigen::VectorXi deformation;
    return std::make_tuple(axialForce, reactionForce, deformation);
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
    // int nodesSize = nodes.size();
    Eigen::Matrix<double, Eigen::Dynamic, 3> p; // put actual value here
    p.fill(0.0);

    p(jibBaseEnd - 2, 2) += jibLeftForce;
    p(jibBaseEnd - 1, 2) += jibRightForce;
    p(cjBaseEnd - 2, 2) += cjLeftForce;
    p(cjBaseEnd - 1, 2) += cjRightForce;
    this->jibLeftForce = jibLeftForce;
    this->jibRightForce = jibRightForce;
    this->cjLeftForce = cjLeftForce;
    this->cjRightForce = cjRightForce;

    forces = p;
}
void Analysis::setGravityInfo(int density, double gravityConst) {
    this->density = density;
    this->gravityConst = gravityConst;
}
void Analysis::applyGravity() {
    for (int i = 0; i < (int)nodes.size(); i++) {
        std::vector<int> beamsConnToNodeIndex;
        // Collect all beams connected to a specific node
        Node nodeToCheck = nodes.at(i);
        for (int j = 0; j < (int)beams.size(); j++) {
            if (beams.at(j).getStart() == nodeToCheck || beams.at(j).getEnd() == nodeToCheck) {
                beamsConnToNodeIndex.push_back(j);
            }
        }
        // Calculate volume of all beams connected to node
        double volume = 0;
        for (int k = 0; k < (int)beamsConnToNodeIndex.size(); k++) {
            volume += (beams.at(beamsConnToNodeIndex.at(k)).getLength() / 2) * areaPerBeam(beamsConnToNodeIndex.at(k));
        }
        // Apply approximate force of gravity
        forces(i, 2) -= volume * density * gravityConst;

        beamsConnToNodeIndex.clear();
    }
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
    // Calculate needed measurements
    double length = beams.at(beam).getLength();
    double mass = length * areaPerBeam(beam) * density;
    double I = (1 / 12) * mass * pow(length, 2);
    // Check if the beam buckles
    if (force >= (pow(M_PI, 2) / pow(length, 2)) * E * I) {
        return false;
    } else if (force >= ((pow(M_PI, 2)) / pow(0.7 * length, 2)) * E * I) {
        return false;
    }
    return true;
}

void Analysis::calculateReactionForces() {

}
std::tuple<Eigen::VectorXi, Eigen::VectorXd> Analysis::calculateDeformation(Eigen::VectorXd defFreeNodes, std::vector<Beam> beams, int dof, int numNodes) {
    // Flatten dofCondition
    // Eigen::VectorXd deformation;
    // for (int i = 0; i < dofCondition.size(); i++) {
    //     for (int j = 0; j < dofCondition.cols(); j++) {
    //         deformation(3 * i + j) = dofCondition(i, j);
    //     }
    // }
    auto deformation = dofCondition.reshaped<Eigen::RowMajor>().transpose();

    // Replaces get_DOFs method but no gurantee about supportDOF
    // Eigen::VectorXi freeDOF = getNonZeros(dofCondition.reshaped<Eigen::RowMajor>()); //.transpose()
    // Eigen::VectorXi supportDOF = getNonZeros(dofCondition.reshaped<Eigen::RowMajor>().cwiseEqual(0)); //.transpose()
    auto DOFs = getDOFs();
    auto freeDOF = std::get<0>(DOFs);
    auto supportDOF = std::get<1>(DOFs);

    // Set the deformations of the free nodes.
    int indexFree = 0;
    for (int i = 0; i < (int)freeDOF.size(); i++) {
        // Unsure abt all the int casts but otherwise throws errors
        deformation((int)freeDOF(i)) = (int)defFreeNodes(indexFree);
        // quickDefo((int)freeDOF(i)) = (int)defFreeNodes(indexFree);
        indexFree++;
    }

    // Set the deformations of the fixed nodes to 0.
    int indexFixed = 0;
    for (int i = 0; i < (int)supportDOF.size(); i++) {
        // Unsure abt all the int casts but otherwise throws errors
        deformation((int)freeDOF(i)) = (int)defFreeNodes(indexFixed);
        // quickDefo((int)freeDOF(i)) = (int)defFreeNodes(indexFixed);
        indexFixed++;
    }
    deformation = deformation.reshaped(numNodes, dof);
    // rough implementation of what happens inside concatenate
    Eigen::VectorXd defoBeams0;
    Eigen::VectorXd defoBeams1;
    for (int i = 0; i < (int)beams.size(); i++) {
        defoBeams0(i) = deformation(beams.at(i).getStart().getNodeNum());
        defoBeams1(i) = deformation(beams.at(i).getEnd().getNodeNum());
    }
    Eigen::VectorXd u;
    u << defoBeams0, defoBeams1;

    return std::make_tuple(deformation, u);
}
std::tuple<Eigen::VectorXi, Eigen::VectorXi> Analysis::getDOFs() {
    Eigen::VectorXi freeDOF = getNonZeros(dofCondition.reshaped<Eigen::RowMajor>(), true); //.transpose()
    Eigen::VectorXi supportDOF = getNonZeros(dofCondition.reshaped<Eigen::RowMajor>(), false);

    return std::make_tuple(freeDOF, supportDOF);
}
Eigen::VectorXi Analysis::getNonZeros(Eigen::VectorXi vecToIndex, bool zeros) {
    Eigen::VectorXi nzIndexes;
    int index = 0;
    for (int i = 0; i < (int)vecToIndex.size(); i++) {
        if (zeros && vecToIndex(i) != 0) {
                nzIndexes(index) = i;
                index++;
        } else if (vecToIndex(i) == 0) {
                nzIndexes(index) = i;
                index++;
        }
    }

    return nzIndexes;
}
Eigen::MatrixXd Analysis::calculateGlobalStiffness(int DOF, int numOfElements, int totalNumOfDOF) {
    Eigen::MatrixXd K = Eigen::MatrixXd::Zero(totalNumOfDOF, totalNumOfDOF);
    for (int i = 0; i < numOfElements; i++) {
        auto tmp = beams.at(i) * (double)DOF;
    }

    return K;
}
std::tuple<Eigen::MatrixXd, Eigen::MatrixXd, Eigen::MatrixXd> Analysis::getComponentsOfGlobalStiffness(Eigen::MatrixXd K, Eigen::MatrixXd freeDOF, Eigen::MatrixXd supportDOF) {
    Eigen::MatrixXd KTopLeft = K.block(freeDOF.rows(), 0, freeDOF.rows(), freeDOF.rows());
    Eigen::MatrixXd KTopRight = K.block(freeDOF.rows(), freeDOF.rows(), supportDOF.rows(), supportDOF.rows());
    Eigen::MatrixXd KBottomLeft = KTopRight.transpose();
    Eigen::MatrixXd KBottomRight = K.block(freeDOF.rows(), supportDOF.rows(), freeDOF.rows(), supportDOF.rows());

    return std::make_tuple(KBottomLeft, KBottomRight, KTopLeft);
}

std::tuple<Eigen::VectorXd, Eigen::VectorXd, Eigen::VectorXd, Eigen::VectorXd> Analysis::optimize(int horzDir, double horzForce, int cjSupType, bool hasHorzForces, bool hasGrav) {
    Eigen::MatrixXd optimAPB;
    std::vector<int> directions = {0, 1, 2, 3};
    for (auto direction : directions) {
        areaPerBeam.fill(pow(0.05, 2));
        resetForces(jibLeftForce, jibRightForce, cjLeftForce, cjRightForce);
        if (hasGrav) {
            applyGravity();
        }
        if (hasHorzForces) {
            applyHorizontalForces(direction, horzForce, cjSupType);
        }
        for (int i = 0; i < 20; i++) {
            auto axialForce = std::get<0>(analyze());
            auto oldAPB(areaPerBeam);
            adjustCrossSectionArea(axialForce);
            if (oldAPB == areaPerBeam) {
                break;
            }
            resetForces(jibLeftForce, jibRightForce, cjLeftForce, cjRightForce);
            if (hasGrav) {
                applyGravity();
            }
        }
        if (!hasHorzForces) {
            break;
        }
        // is this the same as append? or is it concatenate?
        optimAPB.conservativeResize(optimAPB.rows(), optimAPB.cols() + 1);
        optimAPB.col(optimAPB.cols() - 1) = areaPerBeam;
    }
    resetForces(jibLeftForce, jibRightForce, cjLeftForce, cjRightForce);
    if (hasGrav) {
        applyGravity();
    }
    if (hasHorzForces) {
        for (int i = 0; i < (int)areaPerBeam.size(); i++) {
            double highest1 = std::max(optimAPB(i, 0), optimAPB(i, 1));
            double highest2 = std::max(optimAPB(i, 2), optimAPB(i, 3));
            double highest = std::max(highest1, highest2);
            areaPerBeam(i) = highest;
        }
        applyHorizontalForces(horzDir, horzForce, cjSupType);
    }
    auto complAna = analyze();
    auto axialForce = std::get<0>(complAna);
    auto reactionForce = std::get<1>(complAna);
    auto deformation = std::get<1>(complAna);

    return std::make_tuple(axialForce, reactionForce, deformation, areaPerBeam);
}
void Analysis::adjustCrossSectionArea(Eigen::VectorXd axialForce) {
    for (int i = 0; i < (int)areaPerBeam.size(); i++) {
        double currentTension = std::abs(axialForce(i) / areaPerBeam(i));
        if (currentTension > absMaxTension) {
            areaPerBeam(i) = pow(sqrt(areaPerBeam(i)) + 0.01, 2);
        }
    }
}
Eigen::VectorXd Analysis::getAreaPerBeam() {
    return areaPerBeam;
}