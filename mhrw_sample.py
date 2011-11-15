''' Helper library to generate statistics from graphsize.py '''
import mhrw
import graphsize
import plotter


def increasing_sample_size():
    collected = {}
    for sample_size in xrange(0, 30001, 5000):
        if sample_size == 0: continue # ugly hack to skip first
        collected[sample_size] = plotter.run(3, mhrw.gnutella_mhrw, 
                                             {'samples': sample_size, 
                                              'length': 300,
                                              'thinning': 5})
    return collected

def increasing_walk_length_sample_is_10000():
    collected = {}
    for walk in xrange(0,600,50):
        if walk == 0: continue # ugly hack to skip first
        collected[walk] = plotter.run(3, mhrw.gnutella_mhrw, 
                                      {'samples': 10000, 
                                       'length': walk,
                                       'thinning': 5})
    return collected


def increasing_thinning_sample_is_10000_walk_is_100():
    collected = {}
    for thinning in xrange(1,20,1):
        collected[thinning] = plotter.run(1, mhrw.gnutella_mhrw, 
                                          {'samples': 10000, 
                                           'length': 300,
                                           'thinning': thinning})
    return collected


if '__main__' == __name__:
#    sample_size = increasing_sample_size()
#    plotter.print_data("mhrw_size.data", sample_size)

#    walk = increasing_walk_length_sample_is_10000()
#    plotter.print_data("mhrw_walk.data", walk)

    thinning = increasing_thinning_sample_is_10000_walk_is_100()
    plotter.print_data("mhrw_thinning_2.data", thinning)

#    print '\n\nSample size: ', sample_size
#    print '\nWalk: ', walk
#    print '\Thinning: ', thinning
