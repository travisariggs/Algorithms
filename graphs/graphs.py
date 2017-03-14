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


class DirectedGraph(object):
    """Class for Directed Graphs"""

    def __init__(self):

        self.nodes = {}
        self.sccs = {}
        self.reversed = False

        # Private attributes
        self._finishing_time = 0
        self._leader_index = None


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


    def clear_explored(self):
        """Set all nodes to an 'unexplored' state"""

        for node in self.nodes.values():
            node.explored = False


    def clear_finishing_times(self):
        """Clear finishing times of all nodes"""

        for node in self.nodes.values():
            node.finishing_time = None


    def clear_leaders(self):
        """Clear the leader node labels from all nodes"""

        for node in self.nodes.values():
            node.leader_node = None


    def depth_first_search(self, start_node=None, reverse=False):
        """Perform a depth first search of the graph"""

        if start_node:

            node = self.nodes[start_node]

        else:

            node_key = list(self.nodes.keys())[0]
            node = self.nodes[node_key]

        # Mark node as explored
        node.explored = True

        # If a leader is defined, set it for this node
        if self._leader_index:
            node.leader_node = self._leader_index
            # Also track the strong connections at the graph level
            try:
                self.sccs[self._leader_index].append(node.name)
            except:
                self.sccs[self._leader_index] = [node.name]

        # Is the graph reversed?
        if reverse:
            edges = node.in_edges
        else:
            edges = node.out_edges

        for edge in edges:

            # Get the node
            next_node = self.nodes[edge.name]

            if not next_node.explored:

                self.depth_first_search(start_node=next_node.name,
                                        reverse=reverse)

        # Increment the finishing time
        self._finishing_time += 1

        # Set the finishing time for the starting node
        node.finishing_time = self._finishing_time


    def strong_connections(self):
        """Search the graph for strongly connected components

        This uses Kosarju's 2-pass algorithm
        """

        # Clear the explored, finishing times and leader nodes
        self.clear_explored()
        self.clear_finishing_times()
        self.clear_leaders()

        # Search through the reversed graph to calculate finishing times
        for node_name in sorted(self.nodes.keys(), reverse=True):

            node = self.nodes[node_name]

            if not node.explored:
                # self._leader_index = node_name
                self.depth_first_search(node_name, reverse=True)


        # Clear the explored states for a new search
        self.clear_explored()

        # Search through the normal graph in order of finishing time
        for node in sorted(self.nodes.values(),
                           key=lambda node: node.finishing_time,
                           reverse=True):

            if not node.explored:
                self._leader_index = node.name
                self.depth_first_search(node.name)


    def save_graph(self, filename):
        """Save the graph in a DOT file"""

        with open(filename, 'w') as f:

            print("digraph graphname {", file=f)

            for node in self.nodes.values():

                if node.explored:
                    print(str(node.name) + " [color=chartreuse3" + \
                          ",style=filled];",
                          file=f)

                for edge in node.out_edges:

                    print("  " + str(node.name) + " -> " + str(edge.name) + ";",
                          file=f)

            print("}", file=f)

        # Render the graph into an image
        graphviz.render('dot', 'png', filename)



if __name__ == '__main__':

    # a = Graph()

    # #a["Hello"] = "Goodbye"
    # a.add_node("Hello")
    # a.add_node(1, [2,3,4])

    # print(a)


    # b = DirectedGraph()

    # b.add_node(1)
    # b.add_node(2)
    # # ipdb.set_trace()
    # b.add_di_edge(1, 2)
    # b.add_di_edge(2, 1)
    # b.add_di_edge(1, 3)

    # b.save_graph("digraphtest")

    d = DirectedGraph()
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

    # d.depth_first_search(9)

    print(d)

    d.save_graph("digraphtest")

