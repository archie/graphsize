import graphsize
import unittest

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

if __name__ == '__main__':
    unittest.main()