# DWave-BaseExercise-Resources-Allocation
D-Wave project. Base Exercise: Resource Allocation
## Project Name
Resource Allocation
## Description
Program to allocate resources to activities in order to satisfy all the activities

Problem: 

Given a set of Resources {R1,..,RN}, a set of activities {A1,..,AM}, and the capability of each resource to accomplish a subset of possible activities, find the allocation of resources to activities to ensure that all the activities will be covered.

## Resolution Principles
We can build a bipartite graph where:
1. One group of vertices corresponds to the resources.
1. The other group ov vertices corresponds to the activities.
1. The is an edge linking a resource to an activity is this resource can perform the activity.

We have to encode the following constraints:
1. Each activity shall have exactly one resource associate to it.
1. Each resource shall have at most one activity allocated to it.

.