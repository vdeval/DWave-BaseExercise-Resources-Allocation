# Test program for assigning activities to resources.
#
# Problem:
# Given:  A bipartite graph connecting a set of resources to a set of activities, with
#         edges representing links between a resource Ri and an activity Ai that the 
#         resource is able to execute:
#         G = {R={Ri} + A={Ai}}, E={Ei=(r,a): r belongs to R, a belongs to A}}

# Goal:   Find a subset of E such that:
#         1 - All the activities are assigned to exactly one resource
#         2 - Each resource has at most 1 activity assigned
#
# Implementation principles:
# 1 - Convert the  graph in an "adjacency matrix":
#     a - Each row represent a resource.
#     b - Each column represent an activity.
#     c - A cell in the matrix has value 1 if the resource can execute the activity, 0 otherwise.
# 2 - Assign a variable Xi to each element of the matrix set to 1. This is equivalent to
#     assigning a qubit to each edge of the graph.
# 3 - Implement constraint 1 (All the activities are assigned to exactly one resource):
#     For each activity, exactly one of its edges must be selected.
#     Constraint "Exactly 1" among all the variables corresponding to activity's edges.
#     min((1- x1 -x2 - ... -xn)^2)
# 4 - Implement constraint 2 (Each resource has at most 1 activity assigned):
#     For each resource, 0 or 1 of its edges must be selected.
#     Constraints "At most 1" among all the variables corresponding to resource's edges.
#     min(x1x2 + x1x3 + ...+x1xn + x2x3 + ... +x2xn + ...)

# ------- Import -------

# Python library import section
import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict

# D-Wave library import section
from dwave.system import DWaveSampler, EmbeddingComposite
import dwave_networkx as dnx

# Custom Library for Graph Drawing
import MyGraph as mg

# ------- Code section -------

#  ------- Print a graph -------
def DrawG(G,filename):
    node_pos = nx.get_node_attributes(G,'pos')
    nx.draw(G,node_size=200, pos=node_pos, edgelist=list(G.edges), nodelist=list(G.nodes), with_labels = True)
    plt.savefig(filename, facecolor='white', dpi=100)
    plt.clf()


#  ------- Main -------

# Test graph ()
label1 = "Test02_Graph_1"
G=nx.Graph()
G.add_node("R1", pos=(1,2))
G.add_node("R2", pos=(2,2))
G.add_node("R3", pos=(3,2))
G.add_node("R4", pos=(4,2))
G.add_node("R5", pos=(5,2))
G.add_node("A1", pos=(1,0))
G.add_node("A2", pos=(2,0))
G.add_node("A3", pos=(3,0))
G.add_node("A4", pos=(4,0))
G.add_node("A5", pos=(5,0))
G.add_edges_from([("R1","A1"),("R1","A2"),
                  ("R2","A1"),("R2","A5"),
                  ("R3","A1"),
                  ("R4","A2"),("R4","A4"),("R4","A5"),
                  ("R5","A3"),("R5","A5")])
DrawG(G, (label1 + "_Original"))

# ------- Create the QUBO -------

# Initialize the Q matrix
Q = defaultdict(int)

# ------- Constraint 1: All the activities are assigned to exactly one resource -------
for x in G.nodes():
    if x.startswith('A'):        # The node is an Activity
        edgeList = []
        for (u,v) in G.edges():
            if (u==x):
                edgeList.append(x+v)
            elif (v==x):
                edgeList.append(x+u)
        # Now edgeList contains the list of edges exiting from the activity
        # print(x, " --> ", edgeList)
        # Set linear weight -1 to each element 
        for e in edgeList:
            Q[(e,e)] += -1
            # print("----------(", e, ",", e,")")
        # Set quadratic weigth + 2 to each pair
        for i in range(len(edgeList)):
            for j in range ((i+1), len(edgeList)):
                Q[(edgeList[i],edgeList[j])] += 2
                # print("----------(", edgeList[i], ",", edgeList[j],")")

# ------- Constraint 2: Each resource has at most 1 activity assigned -------
for x in G.nodes():
    if x.startswith('R'):        # The node is an Activity
        edgeList = []
        for (u,v) in G.edges():
            if (u==x):
                edgeList.append(v+u)
            elif (v==x):
                edgeList.append(v+x)
        # Now edgeList contains the list of edges exiting from the resource
        # print(x, " --> ", edgeList)
        # Set quadratic weigth + 1 to each pair
        for i in range(len(edgeList)):
            for j in range ((i+1), len(edgeList)):
                Q[(edgeList[i],edgeList[j])] += 1
                # print("----------(", edgeList[i], ",", edgeList[j],")")
        
# print(Q)

# ------- Run our QUBO on the QPU -------

# Run the QUBO on the solver from your config file
sampler = EmbeddingComposite(DWaveSampler())
response = sampler.sample_qubo(Q,
                               chain_strength=10,   # Arbitrary choice...
                               num_reads=100,
                               label=label1)

print(response)


# ------- Update the graph and print it-------

# Select first response and extract active edges
print ("Variables:")
print (response.variables)

print ("Sample[0]:")
print (response.record.sample[0])

print ("Sample.first:")
print (response.first)

 # Usiamo first?
# TODO Creare dizionario edgeDict che contiene gli edge attivi
edgeDict = defaultdict(int)
#print(sample)
for (e,v) in response.first:
    if v==1:
        


# Select the color for each node
def edgeColor(u,v):
    e1 = u + v
    e2 = v + u
    if (e1 in edgeDict) or (e2 in edgeDict): return 'red'
    else:                                    return 'black'
edge_color = [edgeColor(u,v) for (u,v) in G.edges]

# TODO Modificare funzione di stampa per gestire colore nodi e archi (settarli come attributi di nodi e archi?)


