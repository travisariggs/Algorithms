"""

      Quicksort Algorithm
       by Travis Riggs

    This module implements the quicksort algorithm.

"""


def quick_sort_simple_first(aList, startIndex=0, endIndex=None,
                            comparisons=False):
    """Sort a list from least to greatest using quicksort

    Returns a sorted list

    If 'comparisons' is set to True, it returns the sorted list and the
    number of comparisons

    It chooses the first element in the list as the pivot.
    """

    if endIndex is None:
        endIndex = len(aList)

    # Base Case
    if endIndex - startIndex <= 1:

        if comparisons:
            return aList, 0
        else:
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
    #print(aList, aList[startIndex:endIndex], startIndex, endIndex)

    ## DEBUG
    #import ipdb; ipdb.set_trace()

    if comparisons:
        compares = len(aList[startIndex:endIndex]) - 1

        # Rescursively call quick_sort on the upper and lower partitions
        aList, lowerCompares = quick_sort_simple_first(aList,
                                                       startIndex,
                                                       p-1,
                                                       True)
        aList, upperCompares = quick_sort_simple_first(aList,
                                                       p,
                                                       endIndex,
                                                       True)

        totalCompares = compares + lowerCompares + upperCompares

        return aList, totalCompares

    else:

        # Rescursively call quick_sort on the upper and lower partitions
        aList = quick_sort_simple_first(aList, startIndex, p-1)
        aList = quick_sort_simple_first(aList, p, endIndex)

        # Return the sorted list
        return aList


def quick_sort_simple_last(aList, startIndex=0, endIndex=None,
                           comparisons=False):
    """Sort a list from least to greatest using quicksort

    Returns a sorted list

    If 'comparisons' is set to True, it returns the sorted list and the
    number of comparisons

    It chooses the last element in the list as the pivot.
    """

    if endIndex is None:
        endIndex = len(aList)

    # Base Case
    if endIndex - startIndex <= 1:

        if comparisons:
            return aList, 0
        else:
            return aList

    # Select the last element as the pivot
    pivot = aList[endIndex-1]

    # Switch the last element with the first
    aList[endIndex-1] = aList[startIndex]
    aList[startIndex] = pivot

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
    #print(aList, aList[startIndex:endIndex], startIndex, endIndex)

    ## DEBUG
    #import ipdb; ipdb.set_trace()

    if comparisons:
        compares = len(aList[startIndex:endIndex]) - 1

        # Rescursively call quick_sort on the upper and lower partitions
        aList, lowerCompares = quick_sort_simple_last(aList,
                                                       startIndex,
                                                       p-1,
                                                       True)
        aList, upperCompares = quick_sort_simple_last(aList,
                                                       p,
                                                       endIndex,
                                                       True)

        totalCompares = compares + lowerCompares + upperCompares

        return aList, totalCompares

    else:

        # Rescursively call quick_sort on the upper and lower partitions
        aList = quick_sort_simple_last(aList, startIndex, p-1)
        aList = quick_sort_simple_last(aList, p, endIndex)

        # Return the sorted list
        return aList


def quick_sort_median(aList, startIndex=0, endIndex=None,
                      comparisons=False):
    """Sort a list from least to greatest using quicksort

    Returns a sorted list

    If 'comparisons' is set to True, it returns the sorted list and the
    number of comparisons

    It chooses the median of the first, middle and last element in the
    list as the pivot.
    """

    if endIndex is None:
        endIndex = len(aList)

    # Base Case
    if endIndex - startIndex <= 1:

        if comparisons:
            return aList, 0
        else:
            return aList

    ## DEBUG
    #import ipdb; ipdb.set_trace()
    #print(aList[startIndex:endIndex])

    # Find the median of the first, middle and last elements
    first = aList[startIndex]
    if (endIndex - startIndex) % 2 == 0:
        middle = aList[startIndex + int((endIndex-startIndex)/2)-1]
    else:
        middle = aList[startIndex + int((endIndex-startIndex)/2)]
    last = aList[endIndex-1]

    # Is the first element the median of the three?
    if middle < first < last or last < first < middle:
        pivot = first

    # Is the middle element the median of the three?
    elif first < middle < last or last < middle < first:
        pivot = middle
        # Swap the middle with the first
        if (endIndex - startIndex) % 2 == 0:
            aList[startIndex + int((endIndex-startIndex)/2)-1] = aList[startIndex]
        else:
            aList[startIndex + int((endIndex-startIndex)/2)] = aList[startIndex]
        aList[startIndex] = pivot

    # The last element must be the median of the three...
    else:
        pivot = last
        # Switch the last element with the first
        aList[endIndex-1] = aList[startIndex]
        aList[startIndex] = pivot

    ## DEBUG
    #print(aList, aList[startIndex:endIndex], first, middle, last, pivot)

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
    #import ipdb; ipdb.set_trace()

    if comparisons:
        compares = len(aList[startIndex:endIndex]) - 1

        # Rescursively call quick_sort on the upper and lower partitions
        aList, lowerCompares = quick_sort_median(aList,
                                                 startIndex,
                                                 p-1,
                                                 True)
        aList, upperCompares = quick_sort_median(aList,
                                                 p,
                                                 endIndex,
                                                 True)

        totalCompares = compares + lowerCompares + upperCompares

        return aList, totalCompares

    else:

        # Rescursively call quick_sort on the upper and lower partitions
        aList = quick_sort_median(aList, startIndex, p-1)
        aList = quick_sort_median(aList, p, endIndex)

        # Return the sorted list
        return aList



if __name__ == '__main__':

    a = [4, 2, 234, 9, 1, 10, 2300, 3]
    b = [1, 2, 3, 4, 9, 10, 234, 2300]

    result, comparisons = quick_sort_simple_first(a, comparisons=True)

    print(result, comparisons)

    a = [4, 2, 234, 9, 1, 10, 2300, 3]
    b = [1, 2, 3, 4, 9, 10, 234, 2300]

    result, comparisons = quick_sort_simple_last(a, comparisons=True)

    print(result, comparisons)

    a = [4, 2, 234, 9, 1, 10, 2300, 3]
    b = [1, 2, 3, 4, 9, 10, 234, 2300]

    result, comparisons = quick_sort_median(a, comparisons=True)

    print(result, comparisons)
