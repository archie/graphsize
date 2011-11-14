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

def UIS_WR(seq, n):
    """returns n random elements from seq with replacement"""
    return [random.choice(seq) for i in xrange(n)]

def UIS_WOR(seq, n):
    """returns n random elements from seq without replacement"""
    return random.sample(seq, n)

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


def inverse_seq(seq):
    # assuming graph has no disconnected nodes, as in given data, so ignore div 0 degree error
    return [1.0/x for x in seq]

def estimate_size(graph, n_samples=-1):
    # determine the number of samples
    if n_samples == -1: n_samples = graph.size() * 4

    #sample the graph and process the results
    node_samples = UIS_WR(graph.nodes(), n_samples)
    degrees = [graph.degree(node) for node in node_samples]
    sum_of_degrees = sum(degrees)
    sum_of_inverse_degrees = sum(inverse_seq(degrees))

    collisions = collision_count(node_samples)

    print 'Y1: ', sum_of_degrees
    print 'Y2: ', sum_of_inverse_degrees
    print 'Repeated samples: ', collisions

    return calculate_size(sum_of_degrees, sum_of_inverse_degrees, collisions)

def estimate_size_with_mhrw(graph, n_samples=-1, thinning=1, random_walk_length=20):
    # determine the number of samples
    if n_samples == -1: n_samples = graph.size() * 4

    #sample the graph and process the results
    node_samples = MHRW(graph, graph.nodes(), n_samples, length=random_walk_length, thinning=thinning)
    degrees = [graph.degree(node) for node in node_samples]
    sum_of_degrees = sum(degrees)
    sum_of_inverse_degrees = sum(inverse_seq(degrees))

    collisions = collision_count(node_samples)

    print 'Sum of degrees: ', sum_of_degrees
    print 'Sum of inverse degrees: ', sum_of_inverse_degrees
    print 'Repeated samples: ', collisions

    return calculate_size(sum_of_degrees, sum_of_inverse_degrees, collisions)


def calculate_size(degrees, inverse_degrees, identical_samples):
    return ((degrees * inverse_degrees) / (2 * identical_samples))

def collision_count(sample):
    '''counts the unique value pair sets present in sample'''
    total = bin_samples(sample)
    collisions = sum([(n*(n-1))/2 for item, n in total if n > 1])
    if collisions == 0: raise Exception("no collisions found")
    else: return collisions

def bin_samples(samples):
    """produces a histogram-like bin of sample occurence counts"""
    uniques = set(samples)
    return [(item, samples.count(item)) for item in uniques]

def MHRW(original_graph, graph, sample_size, start_node=None, length=20, thinning=1):
    ''' Metropolis-Hasting Random Walk'''
    collected = []

    while (len(collected) <= sample_size):
        start_node = random.choice(graph) # always start at random node
        collected = collected + do_mhrw_walk(original_graph, graph, start_node, length, thinning)

    # truncate if we got too many samples in walk
    if (len(collected) > sample_size):
        collected = collected[:-(len(collected) - sample_size)]

    return collected

def do_mhrw_walk(original_graph, graph, start_node, length, thinning):
    collected_in_walk = []
    next_node = start_node
    current_node = start_node

    for k in xrange(length):
        neighbour = random.choice(original_graph[current_node].keys())
        if (len(original_graph[neighbour]) < len(original_graph[current_node])):
            next_node = neighbour
        else:
            probability_of_transition = float(len(original_graph[current_node])) / float(len(original_graph[next_node]))
            if (random.random() < probability_of_transition):
                next_node = neighbour
            else:
                next_node = current_node

        # only store every k value
        if (k % thinning) == 0:
            collected_in_walk.append(next_node)

        current_node = next_node

    return collected_in_walk


def gnutella_truncated():
    """a reduced-size graph example"""
    graph = nx.read_edgelist("p2p-Gnutella31.truncated.txt", delimiter='\t', nodetype=int)
    print "Running truncated Gnutella size estimate"
    graph_size = graph.number_of_nodes()
    samples = graph_size * 8
    print 'original size', graph_size
    print 'Estimated graph size ({0}): '.format(samples), estimate_size(graph, n_samples = samples)

def gnutella():
    graph = nx.read_edgelist("p2p-Gnutella31.txt", delimiter='\t', nodetype=int)
    print "Running extended Gnutella size estimate"
    graph_size = graph.number_of_nodes()
    samples = graph_size * 2
    print 'original size', graph_size
    print 'Estimated graph size ({0}): '.format(samples), estimate_size(graph, n_samples = samples)

def gnutella_mhrw(samples, length, thinning):
    graph = nx.read_edgelist("p2p-Gnutella31.txt", delimiter='\t', nodetype=int)
    print "Running extended Gnutella size estimate with MHRW sampling"
    graph_size = graph.number_of_nodes()
    print 'Original size: ', graph_size
    print 'Sample size: ', samples
    print 'Random walk length: ', length
    estimated_size = estimate_size_with_mhrw(graph, n_samples=samples, thinning = thinning, random_walk_length=length)
    print 'Estimated graph size: ', estimated_size
    return estimated_size


if __name__ == "__main__":    
    print 'hej'

    #graph = nx.read_edgelist("p2p-Gnutella31.txt", delimiter='\t', nodetype=int)    
    #print 'mhrw: ', MHRW(graph, graph.nodes(), 5, thinning = 5)
    
