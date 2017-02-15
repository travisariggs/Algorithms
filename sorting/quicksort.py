"""

      Quicksort Algorithm
       by Travis Riggs

    This module implements the quicksort algorithm.

"""


def quick_sort(aList, startIndex=0, endIndex=None):
    """Sort a list from least to greatest using quicksort"""

    if endIndex is None:
        endIndex = len(aList)

    # Base Case
    if endIndex - startIndex <= 1:
        return aList

    # Select the first element as the pivot
    pivot = aList[startIndex]

    # Partition the list between elements greater than and less than
    #  the pivot element

    p = startIndex + 1  # Partition index
    i = startIndex + 1  # Element index

    for elem in aList[startIndex+1:endIndex]:

        # Is this element less than our pivot?
        if elem < pivot:

            # Swap this element with the lowest item in the upper
            #  partition. But only do that if we've created an upper
            #  partition.
            if i != p:
                aList[i] = aList[p]
                aList[p] = elem

            # Move the partition index up to make room for the new
            #  value.
            p += 1

        # Track the index of the next list element
        i += 1

    # Move the pivot element between the partitions
    aList[startIndex] = aList[p-1]
    aList[p-1] = pivot

    ## DEBUG
    # print(aList, aList[startIndex:endIndex], startIndex, endIndex)

    # Rescursively call quick_sort on the upper and lower partitions
    aList = quick_sort(aList, startIndex, p-1)
    aList = quick_sort(aList, p, endIndex)

    # Return the sorted list
    return aList


if __name__ == '__main__':

    a = [4, 2, 234, 9, 1, 10, 2300, 3]
    b = [1, 2, 3, 4, 9, 10, 234, 2300]

    result = quick_sort(a)
