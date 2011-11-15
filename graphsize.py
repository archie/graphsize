"""
Implement formula (1) from "Estimating Sizes of Social Networks 
via Biased Sampling". Apply it to nodes collected by:
(a) UIS WOR, -- impossible, no collisions
(b) UIS WR, TODO: fix
(c) WIS WR (with weights equal to node degrees), TODO: implement
(d) RW (using all nodes, or every k-th node; the weights are 
node degrees). TODO: fix

What do you observe?
"""

""" 
graphs: 
  estimated size using different sampling techniques over increasing number of samples
  compare random walks
  effect of thinning
  effect of burn-in
""" 

import networkx as nx
import random
import math

def inverse_seq(seq):
    # assuming graph has no disconnected nodes, as in given data, so ignore div 0 degree error
    return [1.0/x for x in seq]

def estimate_size(degrees, inverse_degrees, identical_samples):
    return ((float(degrees) * float(inverse_degrees)) / (2 * identical_samples))

def collision_count(vertices):
    '''counts the unique value pair sets present in sample'''
    vertex_counts = bin_samples(vertices)
    collisions = sum([(n*(n-1))/2 for vertex, n in vertex_counts if n > 1])
    if collisions == 0: raise Exception("no collisions found")
    else: return collisions

def bin_samples(vertices):
    """produces a histogram-like bin of sample occurence counts"""
    uniques = set(vertices)
    return [(item, vertices.count(item)) for item in uniques]



if __name__ == "__main__":    
    print "nothing to see here, run another file"
