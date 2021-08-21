# DWave-BaseExercise-Resources-Allocation
D-Wave project. Base Exercise: Resource Allocation
## Description
Given a set of Resources {R1,..,Rn}, a set of activities {A1,..,Am}, and the capability of each resource to accomplish a subset of possible activities, find the allocation of resources to activities to ensure that all the activities will be covered.

## Solution
We can describe the problem by building a bipartite graph:
1. One set of vertices corresponds to the resources.
1. The other set of vertices corresponds to the activities.
1. There is an edge linking a resource to an activity if and only if the resource can perform the activity. In general, a resource has one or more links to activities.

To express the constraints of the problem we have to look at the  graph in terms of its "adjacency matrix". Being the graph a bipartite one, only a subset of the matrix is meaningful. We will build a matrix as follows:
1. Each row of the matrix represents a resource.
1. Each column of the matrix represents an activity.
1. A cell in the matrix has value 1 if there is a link between the resource and the activity, 0 otherwise. This means that the resource can execute the activity,
1. Once done, we can associate a QUBO variable to each cell of the matrix with value 1. This is equivalent to assigning a qubit to each edge of the graph.

We can now encode the constraints:
1. **Each activity shall have exactly one resource associate to it:**
     * Consider the colums of the matrix corresponing to an activity. Consider all the QUBO variables in this column.
     * Encode the constraind "Exactly 1" among all the variables. This can be expressed with the following formula:

         min((1- x1 -x2 - ... -xn)^2)
     * Expanding the quadratic form we get:
         * All the variables have a linear term with weight "-1"
         * There is a quadratic term for each combination of variables, with weight "2"


1. **Each resource shall have at most one activity allocated to it:**
     * Consider the row of the matrix corresponing to a resource. Consider all the QUBO variables in this row.
     * Encode the constraint "At most 1" among all the variables. This can be expressed with the following formula:

         min(x1x2 + x1x3 + ...+x1xn + x2x3 + ... +x2xn + ...)
    * There is a quadratic term for each combination of variables, with weight "1"
