import networkx as nx
import graphsize
import plotter

def wis_wr_size_estimate(graph, n_samples=-1):
    # determine the number of samples
    if n_samples == -1: n_samples = graph.size() * 2
    samples = graphsize.WIS_WR(graphsize.degree_weighted_nodes_for(graph), n_samples)
    node_degrees = [graph.degree(node) for node in samples]
    sum_of_degrees = sum(node_degrees)
    sum_of_inverse_degrees = sum(graphsize.inverse_seq(node_degrees))
    collisions = graphsize.collision_count(samples)
    return graphsize.estimate_size(sum_of_degrees, sum_of_inverse_degrees, collisions)

def sample():
    """run a WIS_WR sample and print the results to a file for plotting"""
    graph = nx.read_edgelist("p2p-Gnutella31.txt", delimiter='\t', nodetype=int)
    collected = {}
    for size in xrange(0, 30001, 5000):
        if size == 0: continue
        print 'WIS_WR sample size: ', size
        collected[size] = plotter.run(3, wis_wr_size_estimate,
                                      {'n_samples': size,
                                       'graph': graph})
    
    plotter.print_data('wis_wr.data', collected)
    print 'Finished'

if __name__ == "__main__":    
    sample()
