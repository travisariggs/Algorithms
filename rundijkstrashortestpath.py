#!/usr/bin/python3
"""

        Run Dijkstra's Shortest Path Algorithm
         by Travis Riggs

    Run Dijkstra's Shortest Path algorithm on a large directed
    graph loaded from a text file.

"""

from graphs import DirectedGraph


if __name__ == "__main__":

    digraph = DirectedGraph()

    print("Loading graph...")

    with open("data/dijkstraData.txt", "r") as f:

        for line in f.readlines():

            # Split the line on tabs first
            segments = line.strip().split("\t")

            # The node is the first part
            node = int(segments[0])

            # The following segments are pairs of (edge,length)
            for segment in segments[1:]:

                edgeStr, lengthStr = segment.split(",")

                digraph.add_edge(node, int(edgeStr), length=int(lengthStr))


    # print("Saving graph...")
    # digraph.save_graph("testgraph2")

    print(digraph)

    destinations = (7, 37, 59, 82, 99, 115, 133, 165, 188, 197)

    for destination in destinations:

        print("Running Dijkstra's Shortest Path on 1 to {}".format(destination))
        path, distance = digraph.dijkstras_shortest_path(1, destination)
        print("Distance from 1 to {}: {}".format(destination, distance))

