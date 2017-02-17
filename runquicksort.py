"""

    Exercise the Quicksort algorithm
     by Travis Riggs

   This runs the quicksort algorithm in a few different
   scenarios to test its performance.

"""

import os
import copy
import sorting as s


if __name__ == '__main__':

    # Read a large unsorted array from a file
    with open('/Users/travis/Desktop/quicksort.txt', 'r') as f:

        unsorted = []

        for line in f.readlines():
            unsorted.append(int(line))


    # Create a copy of the array for multiple use because quicksort
    #  sorts the list in place
    original = copy.copy(unsorted)


    # Sort the array with quicksort, using the first element as pivot
    sortedList, comparisons = s.quick_sort_simple_first(unsorted,
                                                        comparisons=True)

    #from ipdb import set_trace; set_trace()

    anotherWay = sorted(copy.copy(original))

    if sortedList == anotherWay:
        print("It's sorted!")
    else:
        print("The sorting didn't work...")

    print("Comparison count: " + str(comparisons))


    # Sort the array with quicksort, using the last element as pivot
    sortedList, comparisons = s.quick_sort_simple_last(copy.copy(original),
                                                       comparisons=True)

    if sortedList == anotherWay:
        print("It's sorted!")
    else:
        print("The sorting didn't work...")

    print("Comparison count: " + str(comparisons))


    # Sort the array with quicksort, using the median of the first,
    #  middle and last element as the pivot
    sortedList, comparisons = s.quick_sort_median(copy.copy(original),
                                                  comparisons=True)

    if sortedList == anotherWay:
        print("It's sorted!")
    else:
        print("The sorting didn't work...")

    print("Comparison count: " + str(comparisons))


    # Sort the array with quicksort, using the median of the first,
    #  middle and last element as the pivot
    sortedList, comparisons = s.quick_sort_random(copy.copy(original),
                                                  comparisons=True)

    if sortedList == anotherWay:
        print("It's sorted!")
    else:
        print("The sorting didn't work...")

    print("Comparison count: " + str(comparisons))
