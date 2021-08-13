# DWave-BaseExercise-Resources-Allocation
D-Wave project. Base Exercise: Resource Allocation
## Description
Given a set of Resources {R1,..,Rn}, a set of activities {A1,..,Am}, and the capability of each resource to accomplish a subset of possible activities, find the allocation of resources to activities to ensure that all the activities will be covered.

## Solution
We can describe the prblem by building a bipartite graph:
1. One set of vertices corresponds to the resources.
1. The other set of vertices corresponds to the activities.
1. The is an edge linking a resource to an activity if this resource can perform the activity. In general, a resource has one or more links to activities.

To express the constraints of the problem we have to look at the  graph in terms of its "adjacency matrix":
1. Each row of the matrix represents a resource.
1. Each column of the matrix represents an activity.
1. A cell in the matrix has value 1 if there is a link between the resource and the activity, 0 otherwise. This means that the resource can execute the activity,
1. Once done, we can associate a QUBO variable to each cell of the matrix with value 1. This is equivalent to assigning a qubit to each edge of the graph.

We can now encode the constraints:
1. **All the activities are assigned to exactly one resource**:
    2. For each activity, exactly one of its edges must be selected.
    2. 
# 3 - Implement constraint 1 (All the activities are assigned to exactly one resource):
#     For each activity, exactly one of its edges must be selected.
#     Constraint "Exactly 1" among all the variables corresponding to activity's edges.
#     min((1- x1 -x2 - ... -xn)^2)
# 4 - Implement constraint 2 (Each resource has at most 1 activity assigned):
#     For each resource, 0 or 1 of its edges must be selected.
#     Constraints "At most 1" among all the variables corresponding to resource's edges.
#     min(x1x2 + x1x3 + ...+x1xn + x2x3 + ... +x2xn + ...)

We have to encode the following constraints:
1. Each activity shall have exactly one resource associate to it.
1. Each resource shall have at most one activity allocated to it.
