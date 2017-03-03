"""

        Run the Minimum Cut Graph Algorithm
         by Travis Riggs

    This runs the randomized minimum cut graph
    algorithm in the graphs module.

"""

from graphs import Graph



if __name__ == '__main__':

    a = Graph()

    # a.add_node(1, [1,2,3])
    # a.add_node(2, [1,3])
    # a.add_node(3, [1,2])

    # a.save_graph("test.dot")

    # print(a)

    print("Loading graph data file...")

    # with open("data/smallgraph.txt", "r") as f:
    with open("data/kargerMinCut.txt", "r") as f:

        for line in f.readlines():

            refs = [int(e) for e in line.strip().split("\t")]

            node = refs.pop(0)

            a.add_node(node, refs)

    # a.save_graph("data/smallgraph.dot")
    # a.save_graph("data/kargerMinCut.dot")

    # print(a)

    print("Beginning randomized min cut")

    iterations = 10000
    results = []

    for i in range(iterations):

        result = a.random_min_cut()
        results.append(result)

        print("Cuts: " + str(result))

        # result.save_graph("data/smallcut.dot")
        # result.save_graph("data/kargerResult.dot")

    # Find the minimum edge count of all of the randomized cuts
    min_cut = min(results)

    print(min_cut)

