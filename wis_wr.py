import networkx as nx
import random

import networkx as nx
import random
import graphsize

def WIS_WR(I_W, n_samples=1):
    ''' From http://code.activestate.com/recipes/117241/
    I_W is a list of (item,weight) tuples,
    e.g. I_W = [('A', 1.25),('B', 2.5), ('C', 3.0)]
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

def degree_weighted_nodes_for(graph):
    """ given a networkx graph it returns a list of (node, weight) tuples 
    where weight = degree
    """
    return [(node, graph.degree(node)) for node in graph.nodes()]

def wis_wr_size_estimate(graph, n_samples=-1):
    # determine the number of samples
    if n_samples == -1: n_samples = graph.size() * 2
    samples = WIS_WR(degree_weighted_nodes_for(graph), n_samples)
    node_degrees = [graph.degree(node) for node in samples]
    sum_of_degrees = sum(node_degrees)
    sum_of_inverse_degrees = sum(graphsize.inverse_seq(node_degrees))
    collisions = graphsize.collision_count(samples)
    return graphsize.estimate_size(sum_of_degrees, sum_of_inverse_degrees, collisions)

if __name__ == "__main__":    
    graph = nx.read_edgelist("p2p-Gnutella31.txt", delimiter='\t', nodetype=int)
    print "Running extended Gnutella size estimate"
    samples = 4000
    print 'original size', graph.number_of_nodes()
    print 'Estimated graph size ({0} samples): '.format(samples)
    print wis_wr_size_estimate(graph, n_samples = samples)

