"""

        Selection Algorithms
         by Travis Riggs

    These are some statistical selection algorithms.

"""

import random


def select_ordered_stat_random(aList, order):
    """Find the ith ordered statistic defined by order in a list

    Returns the value
    """

    # Base case
    if len(aList) == 1:
        return aList[0]

    # Select a pivot randomly
    pivotInd = random.randint(0, len(aList)-1)

    pivot = aList[pivotInd]

    # Swap the pivot into the first position
    aList[pivotInd] = aList[0]
    aList[0] = pivot

    # Track the partion index
    p = 1
    i = 1

    ## DEBUG
    # print(aList, pivot)
    # import ipdb; ipdb.set_trace()

    for elem in aList[1:]:

        if elem < pivot:

            # Swap this element with the lowest element in the upper
            #  partition (only if we have an upper partition)
            if i != p:
                aList[i] = aList[p]
                aList[p] = elem

            # Increment the index of the lower partition boundary
            p += 1

        # Increment the index of the next element to test
        i += 1

    # Swap the pivot into its final place
    aList[0] = aList[p-1]
    aList[p-1] = pivot

    # Did the pivot turn out to be the ordered statistic?
    if order == p:
        return pivot

    elif order < p:
        return select_ordered_stat_random(aList[0:p-1], order)

    elif order > p:
        return select_ordered_stat_random(aList[p:], order - p)


if __name__ == '__main__':

    a = [10,4,1,8,6]

    result = select_ordered_stat_random(a, 3)

    print(a, result)

    a = [1,2,3,4,5]

    result = select_ordered_stat_random(a, 3)

    print(a, result)
