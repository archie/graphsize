import networkx as nx
import random
import graphsize

def UIS_WR(seq, n):
    """returns n random elements from seq with replacement"""
    return [random.choice(seq) for i in xrange(n)]

def uis_wr_size_estimate(graph, n_samples=-1):
    # determine the number of samples
    if n_samples == -1: n_samples = graph.size() * 2

    #uniform sample so degree ratios fixed to 1
    sum_of_degrees = n_samples
    sum_of_inverse_degrees = n_samples
    node_samples = UIS_WR(graph.nodes(), n_samples)
    collisions = graphsize.collision_count(node_samples)
    return graphsize.estimate_size(sum_of_degrees, sum_of_inverse_degrees, collisions)

if __name__ == "__main__":    
    graph = nx.read_edgelist("p2p-Gnutella31.txt", delimiter='\t', nodetype=int)
    print "Running extended Gnutella size estimate"
    samples = 10000
    print 'original size', graph.number_of_nodes()
    print 'Estimated graph size ({0} samples): '.format(samples)
    print uis_wr_size_estimate(graph, n_samples = samples)