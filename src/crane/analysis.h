#ifndef CRANE_ANALYSIS_H
#define CRANE_ANALYSIS_H

#include "truss/components/node.h"
#include "truss/components/beam.h"

class Analysis {
public:
    void analyze();
    void applyForces();
    void resetForces();
    void setGravityInfo();
    void applyGravity();
    void applyHorizontalForces();
private:
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

    void generateConditions();
    
    void applyHorizontalForcesFromFront();
    void applyHorizontalForcesFromBack();
    void applyHorizontalForcesFromLeft();
    void applyHorizontalForcesFromRight();

    bool isEulerBucklingRod();

    void getDOFs();
    void calculateReactionForces();
    void calculateDeformation();
    void calculateGlobalStiffness();
    void getComponentsOfGlobalStiffness();

    void optimize();
};

#endif