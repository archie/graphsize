import networkx as nx
import random
import graphsize

def UIS_WR(seq, n):
    """returns n random elements from seq with replacement"""
    return [random.choice(seq) for i in xrange(n)]

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

def estimate_size(graph, n_samples=-1):
    # determine the number of samples
    if n_samples == -1: n_samples = graph.size() * 2

    #uniform sample so degree ratios fixed to 1
    sum_of_degrees = n_samples
    sum_of_inverse_degrees = n_samples
    node_samples = UIS_WR(graph.nodes(), n_samples)
    collisions = graphsize.collision_count(node_samples)
    return graphsize.estimate_size(sum_of_degrees, sum_of_inverse_degrees, collisions)

