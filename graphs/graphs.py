"""

        Graphs
         by Travis Riggs

    This module contains algorithms and data structures
    for working with graphs.

"""

import copy
import random
import graphviz


class Graph(dict):

    def __init__(self, *args):

        dict.__init__(self, args)

    def add_node(self, node_name, edges=[]):
        """Add a node to the graph and optionally a set of edges"""
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

    def __init__(self, current_node, neighbor_node, kind, length=None):

        self.name = neighbor_node

        if kind == "out":
            self.tail = current_node
            self.head = neighbor_node

        elif kind == "in":
            self.head = current_node
            self.tail = neighbor_node

        else:
            raise ValueError("Unknown DiEdge kind: " + str(kind))

        if length is not None:
            self.length = length

    def __repr__(self):

        s = []
        if self.length is not None:
            s.append("     DiEdge: {}, Tail: {}, Head: {}, Length: {}".format(
                        self.name,
                        self.tail,
                        self.head,
                        self.length))

        else:

            s.append("     DiEdge: {}, Tail: {}, Head: {}".format(
                        self.name,
                        self.tail,
                        self.head))

        st = "\n".join(s)

        return st


class DiNode(object):

    def __init__(self, name):

        self.name = name
        self.in_edges = []
        self.out_edges = []
        self.explored = False
        self.leader_node = None
        self.finishing_time = None

    def __repr__(self):

        s = ["DiNode: {}".format(self.name)]
        s.append("  Explored: {}".format(self.explored))
        s.append("  Leader: {}".format(self.leader_node))
        s.append("  Finishing Time: {}".format(self.finishing_time))

        if self.out_edges:
            s.append("   Out Edges: [")
            for e in self.out_edges:
                s.append("{}".format(e))
            s.append("   ]")
        else:
            s.append("   Out Edges: []")

        if self.in_edges:
            s.append("   In Edges: [")
            for e in self.in_edges:
                s.append("{}".format(e))
            s.append("   ]")
        else:
            s.append("   In Edges: []")

        st = "\n".join(s)

        return st

    def add_edge(self, node_name, kind, length=None):

        if kind == "out":
            self.out_edges.append(DiEdge(self.name, node_name, kind, length))

        elif kind == "in":
            self.in_edges.append(DiEdge(self.name, node_name, kind, length))

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

        # Print strongly connected components
        if self.sccs:
            s.append(" Strongly Connected Components")

            # Get the top 8 SCC's by size
            sccs = sorted(self.sccs.values(),
                          key=lambda scc: len(scc),
                          reverse=True)

            for scc in sccs[:8]:
                s.append("  SCC {}: {:}".format(max(scc), sorted(scc)))

        # Only print the first 10 nodes
        for node in list(self.nodes.values())[:10]:

            s.append("  {}".format(node))

            # s.append("  Node: {}".format(node.name))
            # s.append("    Explored: {}".format(node.explored))
            # s.append("    Leader: {}".format(node.leader_node))
            # s.append("    Finishing Time: {}".format(node.finishing_time))

            # edges = [e.name for e in node.out_edges]
            # s.append("    Out Edges: {:}".format(edges))

            # edges = [e.name for e in node.in_edges]
            # s.append("    In Edges:  {:}".format(edges))

            st = "\n".join(s)

        return st

    def print_sccs(self, limit=5):
        """Print information about the top n SCC groups"""

        st = None

        # Print strongly connected components
        if self.sccs:

            s = ["Strongly Connected Components"]

            # Get the top N SCC's by size
            sccs = sorted(self.sccs.values(),
                          key=lambda scc: len(scc),
                          reverse=True)

            for scc in sccs[:limit]:
                s.append("  SCC {}: size {}: {:}".format(max(scc), len(scc),
                                                         list(scc)[:10]))

            st = "\n".join(s)

            print(st)

        return st

    def add_node(self, label):

        self.nodes[label] = DiNode(label)

    def add_edge(self, tail, head, length=None):

        if tail not in self.nodes:
            self.add_node(tail)

        if head not in self.nodes:
            self.add_node(head)

        self.nodes[tail].add_edge(head, "out", length)

        self.nodes[head].add_edge(tail, "in", length)

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

    def all_explored(self, node, reverse=False):
        """Have all of this nodes edges been explored?"""

        if reverse:
            edges = node.in_edges
        else:
            edges = node.out_edges

        for edge in edges:
            if not self.nodes[edge.name].explored:
                return False

        return True

    def depth_first_search(self, start_node=None, reverse=False):
        """Perform a depth first search of the graph using an iterative
        algorithm, instead of recursive (because Python is not optimized
        for tail recursion)
        """

        # Keep track of the order that nodes are explored
        explored = []

        # Are we provided with a place to start? If not, just use the 1st
        if start_node is None:
            start_node = list(self.nodes.keys())[0]

        # Use a list as a stack to track the exploration tasks
        stack = [start_node]

        while stack:

            # Don't pop the node off the stack until we have explored its
            #  edges completely. That will get checked later with the
            #  .all_explored() method. Only then will the node be popped
            #  off the stack. This allows us to track the finishing time
            #  of each node properly.
            node_name = stack[-1]
            node = self.nodes[node_name]

            # Has this node been explored?
            if not node.explored:

                # Track the nodes that have been explored. Although this
                #  isn't necessary, I am tracking the explored nodes in
                #  both a set and in the node objects themselves. The
                #  set makes it easy to reference and return later, but
                #  I feel that the node object should know if it were
                #  explored or not.
                # explored.add(node_name)
                explored.append(node_name)
                node.explored = True

            # If a "leader" is defined, set it for this node
            if self._leader_index is not None:
                node.leader_node = self._leader_index
                # Also track the strong connections at the graph level
                try:
                    self.sccs[self._leader_index].add(node.name)
                except:
                    self.sccs[self._leader_index] = set([node.name])

            # Does this node still have edges to explore?
            if not self.all_explored(node, reverse):

                # Should we search through the graph backwards?
                if reverse:
                    edges = sorted(node.in_edges,
                                   key=lambda edge: edge.name,
                                   reverse=True)
                else:
                    edges = sorted(node.out_edges,
                                   key=lambda edge: edge.name,
                                   reverse=True)

                # Add the next unexplored edge to the stack
                for edge in edges:
                    if not self.nodes[edge.name].explored:
                        stack.append(edge.name)
                        break

            else:

                # This node is now "complete".
                stack.pop()

                # If the node doesn't have a finishing time, set it
                if node.finishing_time is None:

                    # Increment the finishing time
                    self._finishing_time += 1

                    # Set the finishing time for the starting node
                    node.finishing_time = self._finishing_time

        return explored

    def depth_first_search_recursive(self, start_node=None, reverse=False):
        """Perform a depth first search of the graph recursively"""

        if start_node is not None:

            node = self.nodes[start_node]

        else:

            node_key = list(self.nodes.keys())[0]
            node = self.nodes[node_key]

        # Mark node as explored
        node.explored = True

        # If a leader is defined, set it for this node
        if self._leader_index is not None:
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

                self.depth_first_search_recursive(start_node=next_node.name,
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

    def dijkstras_shortest_path(self, start, finish):
        """Use Dijkstra's Shortest Path algorithm to find the shortest
        pass in a directed graph.

        Returns a list of nodes and the total distance
        """

        path = [(start, start)]
        distances = {start: 0}
        explored_nodes = [self.nodes[start]]
        explored_names = [start]

        while finish not in explored_names:

            # Clear the minimum distance
            min_distance = None

            # Loop through each of the outgoing edges that are on the
            #  frontier.
            for node in explored_nodes:
                for edge in node.out_edges:

                    # Have we found an edge on the frontier?
                    if edge.head not in explored_names:

                        # Calculate the total distance if we chose this
                        #  edge
                        this_distance = distances[node.name] + edge.length

                        if min_distance is not None:

                            # Is this a better edge to choose?
                            if this_distance < min_distance:
                                min_distance = this_distance
                                previous_node = node
                                next_node = self.nodes[edge.head]

                        else:

                            min_distance = this_distance
                            previous_node = node
                            next_node = self.nodes[edge.head]

            # Now that we've explored all the edges of all of the nodes
            #  on the frontier, add the minimum distance node to the
            #  explored set.
            explored_nodes.append(next_node)
            explored_names.append(next_node.name)
            distances[next_node.name] = min_distance

            # Update the shortest path
            path.append((next_node.name, previous_node.name))

        # Now, work backwards from the finish in the path list to get
        #  the actual shortest path using the parent information
        shortest_path = []
        path_parent = None

        while len(path) > 0:

            node_name, parent_name = path.pop()

            if path_parent is None or node_name == path_parent:
                shortest_path.append(node_name)
                path_parent = parent_name

        # Now shortest_path should be populated with only the node names
        #  that were actually in the shortest path, but they are in
        #  reverse order.
        shortest_path.reverse()

        return shortest_path, distances[finish]

    def save_graph(self, filename):
        """Save the graph in a DOT file"""

        colors = ["cornflowerblue", "crimson", "chartreuse2",
                  "darkorange2", "darkorchid3", "goldenrod1",
                  "darkseagreen3", "cyan3", "deeppink3"]

        with open(filename, 'w') as f:

            print("digraph graphname {", file=f)

            for node in self.nodes.values():

                if node.leader_node:

                    # Color the strongly connected components the same
                    #  color.

                    # Choose a color from the list
                    c = colors[int(node.leader_node) % len(colors)]

                    print("  " + str(node.name) +
                          " [color={},style=filled];".format(c),
                          file=f)

                elif node.explored:

                    # Visually mark the node as explored
                    print("  " + str(node.name) + " [color=chartreuse3" +
                          ",style=filled];",
                          file=f)

                for edge in node.out_edges:

                    print("  " + str(node.name) + " -> " +
                          str(edge.name) + ";",
                          file=f)

            print("}", file=f)

        # Render the graph into an image
        graphviz.render('dot', 'png', filename)


if __name__ == '__main__':

    # A Simple Directed graph with various edge lengths
    d = DirectedGraph()

    d.add_edge(1, 2, length=1)
    d.add_edge(1, 3, length=4)
    d.add_edge(2, 3, length=2)
    d.add_edge(2, 4, length=6)
    d.add_edge(3, 4, length=3)

    print(d)

    path, distance = d.dijkstras_shortest_path(1, 4)

    print("Distance: {}, Path: {}".format(distance, path))

    d.save_graph("digraphtest")

    graph = DirectedGraph()
    graph.add_edge(0, 1, length=1)
    graph.add_edge(1, 2, length=1)
    graph.add_edge(2, 3, length=1)
    graph.add_edge(3, 4, length=1)
    graph.add_edge(4, 5, length=1)
    graph.add_edge(5, 6, length=1)
    graph.add_edge(6, 7, length=1)
    graph.add_edge(7, 8, length=1)
    graph.add_edge(8, 9, length=1)
    graph.add_edge(0, 9, length=8)

    path, distance = graph.dijkstras_shortest_path(0, 9)

    print("Distance: {}".format(distance))
    print("Path: {}".format(path))
