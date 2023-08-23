#ifndef CRANE_ANALYSIS_H
#define CRANE_ANALYSIS_H

#include "truss/components/node.h"
#include "truss/components/beam.h"
#include <Eigen/Dense>

class Analysis {
public:
    void analyze();
    void generateConditions(std::vector<Node> nodes, std::vector<Beam> beams);
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
    double E = 210e9;
    int density = 7850;
    double gravityConst = 9.81;
    int absMaxTension = 0;

    std::vector<Node> nodes;
    std::vector<Beam> beams;
    std::vector<int> defFixedNodes;
    Eigen::Matrix<int, Eigen::Dynamic, 3> dofCondition;
    Eigen::Matrix<double, Eigen::Dynamic, 3> forces;
    Eigen::Vector<double, Eigen::Dynamic> areaPerBeam;

    int towerEnd = 0;
    int jibBaseEnd = 0;
    int jibEnd = 0;
    int cjBaseEnd = 0;
    int cjEnd = 0;
    int numNodes = 0;
    int numBeams = 0;
    
    void applyHorizontalForcesFromFront(double force, int cjSupType);
    void applyHorizontalForcesFromBack(double force, int cjSupType);
    void applyHorizontalForcesFromLeft(double force, int cjSupType);
    void applyHorizontalForcesFromRight(double force);

    bool isEulerBucklingRod(int beam, double force);

    std::tuple<Eigen::MatrixXd, Eigen::MatrixXd> getDOFs();
    void calculateReactionForces();
    std::tuple<Eigen::VectorXd, Eigen::VectorXd> calculateDeformation(Eigen::VectorXd defFreeNodes,
                                                                      std::vector<Beam> beams,
                                                                      int dof, int numNodes);
    Eigen::VectorXd getNonZeros(Eigen::VectorXd vecToClean);
    void calculateGlobalStiffness(int DOF, int numOfElements, int totalNumOfDOF);
    std::tuple<Eigen::MatrixXd, Eigen::MatrixXd, Eigen::MatrixXd> getComponentsOfGlobalStiffness(Eigen::MatrixXd K, Eigen::MatrixXd freeDOF, Eigen::MatrixXd supportDOF);

    void optimize();
};

#endif