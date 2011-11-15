import networkx as nx
import random


# TODO: needs to take a networkx graph datastructure
def WIS_WR(I_W):
    # From http://code.activestate.com/recipes/117241/
    # I_W is a list of (item,weight) tuples,
    # e.g. I_W = [('A', 1.25),('B', 2.5), ('C', 3.0)]
    weight_sum = sum(weight for item,weight in I_W)
    n = random.uniform(0, weight_sum)
    for item, weight in I_W:
        if n < weight:
            break
        n = n - weight
    return item 
