import graphsize
import unittest

class GraphSizeTest(unittest.TestCase):
    def test_collision_count_raises_on_no_errors(self):
        '''collision_count should raise error when no collisions'''
        self.assertRaises(Exception, graphsize.collision_count, [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()