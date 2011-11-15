import networkx as nx
import random
import graphsize

def MHRW(original_graph, graph, sample_size, start_node=None, length=20, thinning=1):
    ''' Metropolis-Hasting Random Walk'''
    collected = []

    while (len(collected) <= sample_size):
        start_node = graph[0] # always start at the same node
        collected = collected + do_mhrw_walk(original_graph, graph, start_node, length, thinning)

    # truncate if we got too many samples in walk
    if (len(collected) > sample_size):
        collected = collected[:-(len(collected) - sample_size)]

    return collected

def do_mhrw_walk(original_graph, graph, start_node, length, thinning):
    collected_in_walk = []
    next_node = start_node
    current_node = start_node

    for k in xrange(length):
        neighbour = random.choice(original_graph[current_node].keys())
        if (len(original_graph[neighbour]) < len(original_graph[current_node])):
            next_node = neighbour
        else:
            probability_of_transition = float(len(original_graph[current_node])) / float(len(original_graph[next_node]))
            if (random.random() < probability_of_transition):
                next_node = neighbour
            else:
                next_node = current_node

        # only store every k value
        if (k % thinning) == thinning-1:
            collected_in_walk.append(next_node)

        current_node = next_node

    return collected_in_walk

def estimate_size_with_mhrw(graph, n_samples=-1, thinning=1, random_walk_length=20):
    # determine the number of samples
    if n_samples == -1: n_samples = graph.size() * 4

    #sample the graph and process the results
    node_samples = MHRW(graph, graph.nodes(), n_samples, length=random_walk_length, thinning=thinning)
    degrees = [graph.degree(node) for node in node_samples]
    sum_of_degrees = sum(degrees)
    sum_of_inverse_degrees = sum(graphsize.inverse_seq(degrees))

    collisions = graphsize.collision_count(node_samples)

    print 'Sum of degrees: ', sum_of_degrees
    print 'Sum of inverse degrees: ', sum_of_inverse_degrees
    print 'Repeated samples: ', collisions

    return graphsize.estimate_size(sum_of_degrees, sum_of_inverse_degrees, collisions)

def gnutella_mhrw(samples, length, thinning):
    print "Running extended Gnutella size estimate with MHRW sampling"
    graph = nx.read_edgelist("p2p-Gnutella31.txt", delimiter='\t', nodetype=int)
    print 'Original size: ', graph.number_of_nodes()
    print 'Sample size: ', samples
    print 'Random walk length: ', length
    print 'Thinning used: ', thinning
    estimated_size = estimate_size_with_mhrw(graph, n_samples=samples, thinning = thinning, random_walk_length=length)
    print 'Estimated graph size: ', estimated_size
    return estimated_size

if __name__ == "__main__":    
    print gnutella_mhrw(10000, 300, 10)

