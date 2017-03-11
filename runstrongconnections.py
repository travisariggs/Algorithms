"""

        Run the Strongly Connected Components algorithm
         by Travis Riggs

    This runs a strongly connected component analysis algorithm
    on a given graph edge file.

"""

from graphs import DirectedGraph

if __name__ == '__main__':


    digraph = DirectedGraph()

    # with open("data/SCC.txt", "r") as f:
    with open("data/smalldigraph.txt", "r") as f:

        for line in f.readlines():

            head, tail = line.strip().split(" ")

            digraph.add_di_edge(head, tail)

    digraph.save_graph("data/smalldigraph.dot")

