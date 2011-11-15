import unittest
import networkx as nx
import uis_wr
import random

class UisWrTest(unittest.TestCase):
    def test_graph_size(self):
        """sanity-check graph size estmation with artificial graph data"""
        graph = nx.Graph()
        # basic 5 degree-1 nodes
        for i in xrange(2, 5): graph.add_edge(i-1, i)
        estimate = uis_wr.estimate_size(graph, 100)
        self.assertTrue(4 < estimate < 6, estimate)
        # add links resulting in some degrees > 1
        for i in xrange(6, 4000): graph.add_edge(random.randint(1,i-1), i)
        estimate = uis_wr.estimate_size(graph, 5000)
        self.assertTrue(3900 < estimate < 4100, estimate)

    def test_graph_size_has_div_0_error(self):
        """the given data is a fully-connected graph (edge list) 
        so we don't care about /0 degree error"""
        graph = nx.Graph()
        for i in xrange(5): graph.add_node(i) # nodes, no edges
        self.assertRaises(Exception, uis_wr.estimate_size, graph)

if __name__ == '__main__':
    unittest.main()
