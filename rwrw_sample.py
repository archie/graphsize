import graphsize
import plotter
import rwrw
import networkx as nx

def increasing_sample_size(graph):
    collected = {}
    for sample_size in xrange(0, 30001, 5000):
        if sample_size == 0: continue # ugly hack to skip first
        collected[sample_size] = plotter.run(1, rwrw.rwrw_size_estimate, 
                                             {'graph': graph, 
                                              'n_samples': sample_size, 
                                              'walk_length': 300,
                                              'thinning': 5})
    return collected

def increasing_walk_length_sample_is_10000(graph):
    collected = {}
    for walk in xrange(0,600,50):
        if walk == 0: continue # ugly hack to skip first
        collected[walk] = plotter.run(1, rwrw.rwrw_size_estimate, 
                                      {'graph': graph,
                                       'n_samples': 10000, 
                                       'walk_length': walk,
                                       'thinning': 5})
    return collected


def increasing_thinning_sample_is_10000_walk_is_100(graph):
    collected = {}
    for thinning in xrange(10,101,10):
        collected[thinning] = plotter.run(1, rwrw.rwrw_size_estimate, 
                                          {'graph': graph, 
                                           'n_samples': 10000, 
                                           'walk_length': 300,
                                           'thinning': thinning})
    return collected


if '__main__' == __name__:
    graph = nx.read_edgelist("p2p-Gnutella31.txt", delimiter='\t', nodetype=int)
    sample_size = increasing_sample_size(graph)
    plotter.print_data("rwrw_size.data", sample_size)

    walk = increasing_walk_length_sample_is_10000(graph)
    plotter.print_data("rwrw_walk.data", walk)

    thinning = increasing_thinning_sample_is_10000_walk_is_100(graph)
    plotter.print_data("rwrw_thinning.data", thinning)

#    print '\n\nSample size: ', sample_size
#    print '\nWalk: ', walk
#    print '\Thinning: ', thinning
