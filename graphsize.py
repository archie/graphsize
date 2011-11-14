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

Graph = nx.read_edgelist("p2p-Gnutella31.txt",
                         delimiter='\t',  
                         nodetype=int)

def UIS_WR(I,n):
    return [random.choice(I) for i in xrange(n)]

def UIS_WOR(I,n):
    return random.sample(I,n)

# TODO: needs to take a networkx graph datastructure
def WIS_WR(I_W):
    # From http://code.activestate.com/recipes/117241/
    # I_W is a list of (item,weight) tuples,
    # e.g. I_W = [('A', 1.25),('B', 2.5), ('C', 3.0)]
    weight_sum = sum(weight for item,weight in I_W)
    n = random.uniform(0, weight_sum)
    for item, weight in I_W:
        if n < weight:
            break
        n = n - weight
    return item 

def estimate_size(graph):
    degrees = [Graph.degree(node) for node in graph_sample]
    sum_of_degrees = sum(degrees)
    sum_of_inverse_degrees = sum([1.0/degree for degree in degrees])
    identical_samples = collision_count(graph_sample)
    
    print 'Y1: ', sum_of_degrees
    print 'Y2: ', sum_of_inverse_degrees
    print 'Identicals: ', identical_samples

    size = calculate_size(sum_of_degrees, 
                          sum_of_inverse_degrees, 
                          identical_samples)

    print 'Estimated graph size: ', size

def calculate_size(degrees, inverse_degrees, identical_samples):
    return ((degrees * inverse_degrees) / (2 * identical_samples))

def collision_count(sample): 
    uniques = set(sample)
    total = [(item, sample.count(item)) for item in uniques]
    return sum([(n*(n-1))/2 for item, n in total if n > 1])

def MHRW(sample_size, start_node=None, length=20, thinning=1):
    collected = []

    while (len(collected) <= sample_size):
        start_node = random.choice(Graph) # always start at random node
        collected = collected + do_mhrw_walk(start_node, length, thinning)

    if (len(collected) > sample_size):
        collected = collected[:-len(collected) - sample_size]

    return collected

def do_mhrw_walk(start_node, length, thinning):
    collected_in_walk = []
    current_node = start_node
    collected_in_walk.append(current_node)

    for x in range(length):
        print current_node
        neighbours = Graph[current_node].nodes()
        next_node = random.choice(neighbours)
        current_node = next_node
        if (x % thinning) == 0:
            collected_in_walk.append(next_node)

    return collected_in_walk


if __name__ == "__main__":    
    #print 'original size', Graph.number_of_nodes()
    #graph_sample = UIS_WR(Graph.nodes(), 10000)
    #estimate_size(graph_sample)
    #estimate_size(graph_sample)
    print "Sample:", MHRW(10)
    

#def MHRW(nodes, length):
#     """Metropolis-Hastings Random Walk"""
#     first_node = random.choice(nodes)
#     return _MHRW(length, first_node, thinning)
# 
# def _MHRW(remaining, current):
#     if remaining > 0
#         neighbour = random.choice(neighbours)
#         if degree(neighbour) < degree(current)
#             current = neighbour
#         else
#             probability_of_transition = (degree(current).to_float / degree(neighbour))
#             if random(1) < probability_of_transition
#                 current = neighbour
#         _MHRW(length-1, current)
#     else
#         return current_node
