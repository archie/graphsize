"""
Implement formula (1) from "Estimating Sizes of Social Networks 
via Biased Sampling". Apply it to nodes collected by:
(a) UIS WOR, -- impossible, no collisions
(b) UIS WR, done
(c) WIS WR, done
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

def bin_samples(seq):
    """produces a histogram-like bin of sample occurence counts
    e.g. [1, 1, 2, 3, 3, 3, 3] => [(1, 2), (2, 1), (3, 4)]
    """
    uniques = set(seq)
    return [(item, seq.count(item)) for item in uniques]

def degree_weighted_nodes_for(graph):
    """ given a networkx graph it returns a list of (node, weight) tuples 
    where weight = degree
    e.g. [('A', 24), ('B', 4), ('C', 10)]
    """
    return [(node, graph.degree(node)) for node in graph.nodes()]

def WIS_WR(I_W, n_samples=1):
    ''' returns weighted random samples of I_W, with replacement
    I_W is a list of (item,weight) tuples,
    e.g. I_W = [('A', 1.25),('B', 2.5), ('C', 3.0)]
    From http://code.activestate.com/recipes/117241/
    modified to take n_samples
    '''
    weight_sum = sum([weight for item,weight in I_W])
    samples = []
    for x in xrange(n_samples):
        n = random.uniform(0, weight_sum)
        for item, weight in I_W:
            if n < weight:
                break
            n = n - weight
        samples.append(item)
    return samples

if __name__ == "__main__":    
    print "nothing to see here, run another file"
