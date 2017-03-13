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



class DiNode(object):

    def __init__(self, name, edges=None):

        self.name = name
        self.in_edges = []
        self.out_edges = []
        self.explored = False
        self.leader_node = None
        self.finishing_time = None


    def add_edge(self, node_name, kind):


        if kind == "out":
            self.out_edges.append(DiEdge(self.name, node_name, kind))

        elif kind == "in":
            self.in_edges.append(DiEdge(self.name, node_name, kind))

        else:
            raise ValueError("Unknown Edge kind: " + str(kind))



class DiEdge(object):

    def __init__(self, current_node, neighbor_node, kind):

        self.name = neighbor_node

        if kind == "out":
            self.tail = current_node
            self.head = neighbor_node

        elif kind == "in":
            self.head = current_node
            self.tail = neighbor_node

        else:
            raise ValueError("Unknown DiEdge kind: " + str(kind))



class DirectedGraph(object):
    """Class for Directed Graphs"""

    def __init__(self):

        self.nodes = {}
        self.strong_connected_components = {}
        self.reversed = False
        self._finishing_time = 0


    def __repr__(self):

        s = ["DirectedGraph"]

        for node in self.nodes.values():

            s.append("  Node: {}".format(node.name))
            s.append("    Explored: {}".format(node.explored))
            s.append("    Leader: {}".format(node.leader_node))
            s.append("    Finishing Time: {}".format(node.finishing_time))

            edges = [e.name for e in node.out_edges]
            s.append("    Out Edges: {:}".format(edges))

            st = "\n".join(s)

        return st


    def add_node(self, label):

        self.nodes[label] = DiNode(label)


    def add_di_edge(self, tail, head):

        # ipdb.set_trace()
        if tail not in self.nodes:
            self.add_node(tail)

        if head not in self.nodes:
            self.add_node(head)

        self.nodes[tail].add_edge(head, "out")

        self.nodes[head].add_edge(tail, "in")


    def save_graph(self, filename):
        """Save the graph in a DOT file"""

        with open(filename, 'w') as f:

            print("digraph graphname {", file=f)

            for node_name, node in self.nodes.items():

                for edge in node.out_edges:

                    print(str(node.name) + " -> " + str(edge.name) + ";",
                          file=f)

            print("}", file=f)

        # Render the graph into an image
        graphviz.render('dot', 'png', filename)








if __name__ == '__main__':

    a = Graph()

    #a["Hello"] = "Goodbye"
    a.add_node("Hello")
    a.add_node(1, [2,3,4])

    print(a)


    b = DirectedGraph()

    b.add_node(1)
    b.add_node(2)
    # ipdb.set_trace()
    b.add_di_edge(1, 2)
    b.add_di_edge(2, 1)
    b.add_di_edge(1, 3)

    b.save_graph("digraphtest")

    print(b)

