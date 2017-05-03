#!/usr/bin/python3
"""

        Track the running median on a stream of integers
         by Travis Riggs

"""

import heapq as hq
import heapq_max as hm


if __name__ == "__main__":

    low_heap = []
    high_heap = []
    median = None
    size = 0
    medians = []

    with open("data/median.txt", "r") as f:

        for line in f.readlines():

            number = int(line.strip())

            # For first iteration...
            if median is None:
                median = number

            # Which heap should be number be placed in?
            if number <= median:

                # Put it in the lower heap
                hm.heappush_max(low_heap, number)

            else:

                # Put it in the higher heap
                hq.heappush(high_heap, number)

            # Rebalance the heaps, if needed
            #  I am preferring the lower heap. It is either equal in length to
            #  the higher heap or is one element longer.
            if len(low_heap) - len(high_heap) > 1:

                # Move the max element from the low heap to the high heap
                transfer = hm.heappop_max(low_heap)
                hq.heappush(high_heap, transfer)

            elif len(high_heap) > len(low_heap):

                # Move the min element from the high heap to the low heap
                transfer = hq.heappop(high_heap)
                hm.heappush_max(low_heap, transfer)

            # Reset the median. It should always be the maximum of the lower
            #  heap.
            median = low_heap[0]

            # Track all of the medians
            medians.append(median)

            #  # Print Debugging information
            #  combined = sorted(low_heap + high_heap)
            #  print("\n{}".format(combined))

            #  print("Low Heap:  {}".format(low_heap))
            #  print("High Heap: {}".format(high_heap))

            #  # Calculate the actual median (for comparison)
            #  if len(combined) % 2 == 0:
            #      actualMedian = combined[int((len(combined)-2)/2)]
            #  else:
            #      actualMedian = combined[int((len(combined)-1)/2)]
            #
            #  print("Actual, My median: {}, {}".format(actualMedian, median))

    # Sum the medians and modulo the results
    medianSum = sum(medians)
    result = medianSum % 10000

    print("Median sum: {}".format(medianSum))
    print("Median result: {}".format(result))
