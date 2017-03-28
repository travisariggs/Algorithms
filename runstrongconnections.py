"""

        Run the Strongly Connected Components algorithm
         by Travis Riggs

    This runs a strongly connected component analysis algorithm
    on a given graph edge file.

"""

from graphs import DirectedGraph


if __name__ == '__main__':

    digraph = DirectedGraph()

    with open("data/SCC.txt", "r") as f:
    # with open("data/smalldigraph.txt", "r") as f:

        for line in f.readlines():

            head, tail = line.strip().split(" ")

            digraph.add_edge(int(head), int(tail))

    print("Loaded graph from file")
    print(len(list(digraph.nodes.keys())))
    print("Beginning strong connection analysis...")

    digraph.strong_connections()

    # print(digraph)
    digraph.print_sccs(limit=10)

