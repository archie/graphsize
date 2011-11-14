import networkx as nx
import random
import math

def RWRW(graph, sample_size, start_node=None, length=20, thinning=1):
    collected = []
    while (len(collected) <= sample_size):
        start_node = random.choice(graph) # always start at random node
        collected += do_classic_random_walk(graph, start_node, length, thinning)

    # truncate if we got too many samples in walk
    if (len(collected) > sample_size):
        collected = collected[:-(len(collected) - sample_size)]
    return reweight_sample(collected)

def do_classic_random_walk(graph, start_node, length, thinning):
    collected_in_walk = []
    current_node = start_node
    for k in range(length):
        current_node = graph[random.choice(current_node.keys())]
        # only store every k value
        if (k % thinning) == 0:
            collected_in_walk.append(next_node)
    return collected_in_walk

def reweight_sample(samples):
    binned_samples = bin_samples(samples)

if __name__ == "__main__":    
    graph = nx.read_edgelist("p2p-Gnutella31.txt", delimiter='\t', nodetype=int)
    print "Sample:", RWRW(graph, 20, thinning=5)
