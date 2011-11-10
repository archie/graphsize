"""
Implement formula (1) from "Estimating Sizes of Social Networks 
via Biased Sampling". Apply it to nodes collected by:
(a) UIS WOR, 
(b) UIS WR, 
(c) WIS WR (with weights equal to node degrees), 
(d) RW (using all nodes, or every k-th node; the weights are 
node degrees). 

What do you observe?
"""

import networkx as nx
import random

Graph = nx.read_edgelist("p2p-Gnutella31.txt",
                         delimiter='\t',  
                         nodetype=int)

def UIS_WR(I,n):
    return [random.choice(I) for i in xrange(n)]

def UIS_WOR(I,n):
    return random.sample(I,n)

def WIS_WR(I_W):
    # From http://code.activestate.com/recipes/117241/
    # I_W is a list of (item,weight) tuples,
    # e.g. I_W = [(‘A', 1.25),(‘B', 2.5), (‘C’, 3.0)]
    weight_sum = sum(weight for item,weight in I_W)
    n = random.uniform(0, weight_sum)
    for item, weight in I_W:
        if n < weight:
            break
        n = n - weight
    return item 

def estimate_size(graph):
    sample = UIS_WR(graph, 1000)
    size = ((Y1 * Y2)/(2*collisions(sample)))
    print size

def collisions(sample):
    return 5
