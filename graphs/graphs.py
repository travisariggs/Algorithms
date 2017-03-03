"""

        Graphs
         by Travis Riggs

    This module contains algorithms and data structures
    for working with graphs.

"""

import ipdb
import copy
import random
import graphviz


class Graph(dict):


    def __init__(self, *args):

        dict.__init__(self, args)


    def add_node(self, node_name, edges=[]):
        """Add a node to the graph and optionally a set of edges"""

        #ipdb.set_trace()
        self[node_name] = edges


    def num_of_nodes(self):
        return len(self.keys())


    def save_graph(self, filename):
        """Save the graph in a DOT file"""

        graph = copy.deepcopy(self)

        with open(filename, 'w') as f:

            print("graph graphname {", file=f)

            for node, edges in graph.items():

                for edge in edges:

                    print(str(node) + " -- " + str(edge) + ";", file=f)

                    # Remove the matching edge in the other node
                    #  so that we don't plot a false double edge
                    try:
                        graph[edge].remove(node)

                    except:
                        pass

            print("}", file=f)

        # Render the graph into an image
        graphviz.render('dot', 'png', filename)


    def random_min_cut(self):
        """Use the randomized contraction algorithm to attempt
        to find the minimum cut of the graph

        Returns the contracted graph
        """

        random.seed()

        # Copy the current graph before modifying it
        graph = copy.deepcopy(self)


        while graph.num_of_nodes() > 2:

            # Randomly select an edge to contract
            firstNode = random.choice(list(graph.keys()))
            secondNode = random.choice(graph[firstNode])

            # ipdb.set_trace()

            # Remove the edge reference from the first and second node
            graph[firstNode].remove(secondNode)
            graph[secondNode].remove(firstNode)

            # Combine the two nodes (their edges) for the selected edge
            graph[firstNode].extend(graph[secondNode])
            graph.pop(secondNode)

            # Update the name of any edge reference to the second node
            for node, edges in graph.items():

                for e in range(len(edges)):
                    if edges[e] == secondNode:
                        edges[e] = firstNode

            # Remove any self-loop edges
            selfLoops = graph[firstNode].count(firstNode)

            for s in range(selfLoops):
                graph[firstNode].remove(firstNode)

        nodes = list(graph.keys())

        # Get the number of edges from the first node (there are only
        #  two nodes and their edges should be symmetric)
        edgesCount = len(graph[nodes[0]])

        return edgesCount



if __name__ == '__main__':

    a = Graph()

    #a["Hello"] = "Goodbye"
    a.add_node("Hello")
    a.add_node(1, [2,3,4])



    print(a)

