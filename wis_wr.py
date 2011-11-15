import networkx as nx
import graphsize

def wis_wr_size_estimate(graph, n_samples=-1):
    # determine the number of samples
    if n_samples == -1: n_samples = graph.size() * 2
    samples = graphsize.WIS_WR(graphsize.degree_weighted_nodes_for(graph), n_samples)
    node_degrees = [graph.degree(node) for node in samples]
    sum_of_degrees = sum(node_degrees)
    sum_of_inverse_degrees = sum(graphsize.inverse_seq(node_degrees))
    collisions = graphsize.collision_count(samples)
    return graphsize.estimate_size(sum_of_degrees, sum_of_inverse_degrees, collisions)

if __name__ == "__main__":    
    graph = nx.read_edgelist("p2p-Gnutella31.txt", delimiter='\t', nodetype=int)
    print "Running extended Gnutella size estimate"
    samples = 1000
    print 'original size', graph.number_of_nodes()
    print 'Estimated graph size ({0} samples): '.format(samples)
    print wis_wr_size_estimate(graph, n_samples = samples)

