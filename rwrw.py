import networkx as nx
import random
import math
import graphsize

def RWRW(graph, sample_size, start_node=None, length=20, thinning=1):
    collected = []
    while (len(collected) <= sample_size):
        start_node = 0 # always start at the same node
        collected += classic_random_walk(graph, graph.nodes(), start_node, length, thinning)

    # truncate to requested sample length
    if (len(collected) > sample_size):
        collected = collected[:-(len(collected) - sample_size)]

    return reweight_sample(collected, graph)

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

def hh_node_weight(graph, node, occurrences, sum_of_inverse_degrees):
    return (occurrences / graph.degree(node)) / sum_of_inverse_degrees

def reweight_sample(samples, graph):
#    print samples
    degrees = [graph.degree(node) for node in samples]
    sum_of_inverse_degrees = sum(graphsize.inverse_seq(degrees))
    num_samples = len(samples)
    binned_samples = graphsize.bin_samples(samples)

    #print binned_samples
    
    # create a dict of p values for each element in the bin
    #       i.e. {0.2: 1, 0.4: 3, :0.5: 2, ...}
    # for sample in xrange(num_samples):
        # sample the samples using the HH estimator reweighting
        # i.e. find the first key in the dict greater than random.random
        #       and add its value to results
    sample_probability_distribution = dict([
        # TODO This doesn't work, it needs to increment the previous p value by its own value;
        #  and we must make sure the first is > 0 and the last is < 1
        (hh_node_weight(graph, node, occurrences, sum_of_inverse_degrees), node)
        for [node, occurrences] in binned_samples
    ])

    print sample_probability_distribution

    results = []
    for sample in xrange(num_samples):
        rand = random.random() # once per sample

        #TODO: sorting needed? reversed(sorted(sample_prob_distr.keys())):
        sorted_prob = sample_probability_distribution.keys()
        sorted_prob.sort()
        for prob in sorted_prob:
            if rand < prob:
                node = sample_probability_distribution[prob]
                results.append(node)
                break #out of for loop over prob distr

    return results

if __name__ == "__main__":    
    graph = nx.read_edgelist("p2p-Gnutella31.txt", delimiter='\t', nodetype=int)
    print "Sample:", RWRW(graph, 100, thinning=5)
