''' Helper library to generate statistics from graphsize.py '''

import graphsize
import plotter

def run(no_of_times, function, args):
    collected_results = [function(**args) for x in xrange(no_of_times)]
    average = sum(collected_results) / no_of_times
    return average

def increasing_sample_size():
    collected = {}
    for sample_size in xrange(0, 30001, 5000):
        if sample_size == 0: continue # ugly hack to skip first
        collected[sample_size] = run(3, graphsize.gnutella_mhrw, 
                                     {'samples': sample_size, 
                                      'length': 300,
                                      'thinning': 5})
    return collected

def increasing_walk_length_sample_is_10000():
    collected = {}
    for walk in xrange(0,600,50):
        if walk == 0: continue # ugly hack to skip first
        collected[walk] = run(3, graphsize.gnutella_mhrw, 
                              {'samples': 10000, 
                               'length': walk,
                               'thinning': 5})
    return collected


def increasing_thinning_sample_is_10000_walk_is_100():
    collected = {}
    for thinning in xrange(10,101,10):
        collected[thinning] = run(3, graphsize.gnutella_mhrw, 
                                  {'samples': 10000, 
                                   'length': 300,
                                   'thinning': thinning})
    return collected


if '__main__' == __name__:
    sample_size = increasing_sample_size()
    plotter.print_data("sample_size.data", sample_size)

    walk = increasing_walk_length_sample_is_10000()
    plotter.print_data("walk.data", walk)

    thinning = increasing_thinning_sample_is_10000_walk_is_100()
    plotter.print_data("thinning.data", thinning)

#    print '\n\nSample size: ', sample_size
#    print '\nWalk: ', walk
#    print '\Thinning: ', thinning
