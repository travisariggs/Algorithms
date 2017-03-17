"""

        Test Graphs Module
         by Travis Riggs

"""

import unittest
import graphs as g


class TestDirectedGraph(unittest.TestCase):

    def setUp(self):

        self.graph = g.DirectedGraph()
        self.graph.add_di_edge(1, 4)
        self.graph.add_di_edge(4, 7)
        self.graph.add_di_edge(7, 1)
        self.graph.add_di_edge(9, 0)
        self.graph.add_di_edge(0, 7)
        self.graph.add_di_edge(9, 3)
        self.graph.add_di_edge(3, 6)
        self.graph.add_di_edge(6, 9)
        self.graph.add_di_edge(8, 6)
        self.graph.add_di_edge(8, 5)
        self.graph.add_di_edge(5, 2)
        self.graph.add_di_edge(2, 8)

    def test_DepthFirstSearch(self):

        self.graph.depth_first_search_recursive(8)

        result = True

        for node in self.graph.nodes.values():

            if not node.explored:
                result = False

        self.assertTrue(result)

    def test_DepthFirstSearchIter(self):

        self.graph.depth_first_search(8)

        result = True

        for node in self.graph.nodes.values():

            if not node.explored:
                result = False

        self.assertTrue(result)

    def test_StrongConnection_0(self):

        self.graph.strong_connections()
        self.assertEqual(sorted(self.graph.sccs[0]), [0])

    def test_StrongConnection_7(self):

        self.graph.strong_connections()
        self.assertEqual(sorted(self.graph.sccs[7]), [1,4,7])

    def test_StrongConnection_8(self):

        self.graph.strong_connections()
        self.assertEqual(sorted(self.graph.sccs[8]), [2,5,8])

    def test_StrongConnection_9(self):

        self.graph.strong_connections()
        self.assertEqual(sorted(self.graph.sccs[9]), [3,6,9])

if __name__ == '__main__':

    unittest.main()

