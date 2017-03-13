"""

        Test Graphs Module
         by Travis Riggs

"""

import unittest
import graphs as g


class TestDirectedGraph(unittest.TestCase):

    def test_DepthFirstSearch(self):

        d = g.DirectedGraph()
        d.add_di_edge(1, 4)
        d.add_di_edge(4, 7)
        d.add_di_edge(7, 1)
        d.add_di_edge(9, 7)
        d.add_di_edge(9, 3)
        d.add_di_edge(3, 6)
        d.add_di_edge(6, 9)
        d.add_di_edge(8, 6)
        d.add_di_edge(8, 5)
        d.add_di_edge(5, 2)
        d.add_di_edge(2, 8)

        d.depth_first_search(8)

        result = True

        for node in d.nodes.values():

            if not node.explored:
                result = False

        self.assertTrue(result)


if __name__ == '__main__':

    unittest.main()

