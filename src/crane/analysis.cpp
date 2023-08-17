#include "analysis.h"
#include "truss/components/node.h"
#include "truss/components/beam.h"
#include <xtensor>

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
    
    dofCondition = xt::ones<double>({nodes.size(), 3});
}
    
void Analysis::applyHorizontalForcesFromFront(double force, int cjSupType) {

}
void Analysis::applyHorizontalForcesFromBack(double force, int cjSupType) {

}
void Analysis::applyHorizontalForcesFromLeft(double force, int cjSupType) {

}
void Analysis::applyHorizontalForcesFromRight(double force) {

}

bool Analysis::isEulerBucklingRod() {

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