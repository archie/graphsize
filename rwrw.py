import networkx as nx
import random
import math
import graphsize

""" This implementation of Reweighted Random Walk doesn't really work. You've been warned."""

def RWRW(graph, sample_size, start_node=None, length=20, thinning=1):
    collected = []
    while (len(collected) <= sample_size):
        start_node = 0 # always start at the same node
        collected += classic_random_walk(graph, graph.nodes(), start_node, length, thinning)

    # truncate to requested sample length
    if (len(collected) > sample_size):
        collected = collected[:-(len(collected) - sample_size)]

    return reweighted_sample(collected, graph)

def classic_random_walk(original_graph, graph, start_node, length, thinning=1):
    '''
    returns the uncompensated (biased) random walk path, with optional thinning
    start_node should be the node key (id), not node hash
    '''
    collected_in_walk = []
    current_node = start_node
    for k in range(length):
        current_node = random.choice(original_graph[current_node].keys())
        # only store every k value
        if (k % thinning) == 0:
            collected_in_walk.append(current_node)
    return collected_in_walk

def reweighted_sample(samples, graph):
    degrees = [graph.degree(node) for node in samples]
    sum_of_inverse_degrees = sum(graphsize.inverse_seq(degrees))
    num_samples = len(samples)
    binned_samples = graphsize.bin_samples(samples)
    # print "original sample bins", binned_samples
    # reuse the WIS_WR probability distribution sampling method
    # create a tuple list of nodes and weights for each bin element
    #       i.e. [(1, 0.2), (3, 0.4), (2, 0.5) ...}
    hh_weighted_nodes = [
        (node, 
        graphsize.hh_node_weight(graph.degree(node), occurrences, sum_of_inverse_degrees)
        ) 
        for [node, occurrences] in binned_samples
    ]
    new_samples = graphsize.WIS_WR(hh_weighted_nodes, num_samples)
    # print "reweighted sample bins", graphsize.bin_samples(new_samples)
    return new_samples

def rwrw_size_estimate(graph, n_samples=-1, walk_length=200, thinning=40):
    # determine the number of samples
    if n_samples == -1: n_samples = graph.size() * 2
    samples = RWRW(graph, n_samples, length=walk_length, thinning=thinning)
    node_degrees = [graph.degree(node) for node in samples]
    sum_of_degrees = sum(node_degrees)
    sum_of_inverse_degrees = sum(graphsize.inverse_seq(node_degrees))
    collisions = graphsize.collision_count(samples)
    return graphsize.estimate_size(sum_of_degrees, sum_of_inverse_degrees, collisions)

def sample():
    graph = nx.read_edgelist("p2p-Gnutella31.txt", delimiter='\t', nodetype=int)
    print "Running graph size estimate using RWRW on Gnutella"
    samples = 10000
    print 'original size', graph.number_of_nodes()
    print 'Estimated graph size ({0} samples): '.format(samples)
    print rwrw_size_estimate(graph, n_samples = samples, walk_length=10000, thinning=100)

if __name__ == "__main__":    
    sample()

