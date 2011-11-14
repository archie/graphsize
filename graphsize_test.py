import graphsize
import unittest
import networkx as nx
import random

class GraphSizeTest(unittest.TestCase):
    def test_collision_count_raises_on_no_errors(self):
        '''collision_count should raise error when no collisions'''
        self.assertRaises(Exception, graphsize.collision_count, [1, 2, 3, 4])
        self.assertRaises(Exception, graphsize.collision_count, [])


    def test_collision_count_counts_collisions(self):
        '''collision_count should sum the number of all unique like-value set pairs (collisions) found'''
        self.assertEqual(1, graphsize.collision_count([1, 1]))
        self.assertEqual(1, graphsize.collision_count([1, 2, 1]))
        self.assertEqual(1 + 1, graphsize.collision_count([2, 1, 1, 2]))
        self.assertEqual(1 + 3, graphsize.collision_count([4, 6, 4, 6, 6]))

    def test_graph_size(self):
        """sanity-check graph size estmation with artificial graph data"""
        graph = nx.Graph()
        # basic 5 degree-1 nodes
        for i in xrange(2, 5): graph.add_edge(i-1, i)
        estimate = graphsize.estimate_size(graph, 5000)
        self.assertTrue(4 < estimate < 6, estimate)
        # add links resulting in some degrees > 1
        for i in xrange(6, 10000): graph.add_edge(random.randint(1,i-1), i)
        estimate = graphsize.estimate_size(graph, 40000)
        self.assertTrue(9900 < estimate < 11000, estimate)

    def test_graph_size_has_div_0_error(self):
        """the given data is a fully-connected graph (edge list) 
        so we don't care about /0 degree error"""
        graph = nx.Graph()
        for i in xrange(5): graph.add_node(i) # nodes, no edges
        self.assertRaises(Exception, graphsize.estimate_size, graph)

    def test_calculate_size_arithmetic(self):
        """degrees * inverse_degrees / 2 * identical_samples"""
        self.assertEqual(10, graphsize.calculate_size(10, 10, 5))
        self.assertEqual(100.4, graphsize.calculate_size(10, 100.4, 5))

    def test_inverse_seq(self):
        self.assertEqual([1, 2, 4, 1], graphsize.inverse_seq([1, 0.5, 0.25, 1]))

if __name__ == '__main__':
    unittest.main()