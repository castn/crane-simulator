#ifndef CRANE_ANALYSIS_H
#define CRANE_ANALYSIS_H

#include "truss/components/node.h"
#include "truss/components/beam.h"
#include <Eigen/Dense>

class Analysis {
public:
    void analyze();
    void applyForces(std::vector<Node> nodes, int towerEnd, int jibEnd, int jibBaseEnd,
                     int cjEnd, int cjBaseEnd, double jibLeftForce, double jibRightForce,
                     double cjLeftForce, double cjRightForce);
    void resetForces(double jibLeftForce, double jibRightForce, double cjLeftForce,
                     double cjRightForce);
    void setGravityInfo(int density, double gravityConst);
    void applyGravity();
    void applyHorizontalForces(int direction, double force, int cjSupType);
private:
    int kN = 1e3;
    std::vector<Node> nodes;
    std::vector<int> defFixedNodes;
    Eigen::Matrix<int, Eigen::Dynamic, Eigen::Dynamic> dofCondition;
    Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic> forces;

    int towerEnd = 0;
    int jibBaseEnd = 0;
    int jibEnd = 0;
    int cjBaseEnd = 0;
    int cjEnd = 0;
    int numNodes = 0;
    int numBeams = 0;

    int density = 0;
    double gravityConst = 0;
    int absMaxTension = 0;

    void generateConditions(std::vector<Node> nodes);
    
    void applyHorizontalForcesFromFront(double force, int cjSupType);
    void applyHorizontalForcesFromBack(double force, int cjSupType);
    void applyHorizontalForcesFromLeft(double force, int cjSupType);
    void applyHorizontalForcesFromRight(double force);

    bool isEulerBucklingRod();

    void getDOFs();
    void calculateReactionForces();
    void calculateDeformation();
    void calculateGlobalStiffness();
    void getComponentsOfGlobalStiffness();

    void optimize();
};

#endif