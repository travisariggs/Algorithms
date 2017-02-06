#!/usr/bin/python
"""
    Merge Sort
     by Travis Riggs

  Sort an input list from least to greatest.

"""
import pdb


def mergeSort(aList):
    """Sort a list of integers from least to greatest

    Returns None on a failure
    """

    n = len(aList)

    # Check for base case
    if n == 1:
        return aList

    # Split the list into two halves and call recursively
    first = mergeSort(aList[0:n/2])

    second = mergeSort(aList[n/2:n])

    #pdb.set_trace()

    # Perform Merge of two sorted lists
    #  Initialize counters, lengths and the newly sorted array
    i, j = 0, 0
    firstLen = len(first)
    secondLen = len(second)

    sortedList = []

    # Populate the sorted list with the lesser of each half-list
    for k in range(n):

        # Make sure we won't try to access past the end of a list
        #  If we've reached the end of the first array, then
        #  add the element from the second array.
        if i == firstLen:
            sortedList.append(second[j])
            j += 1

        # If we've reached the end of the second array, add
        #  the element from the first array
        elif j == secondLen:
            sortedList.append(first[i])
            i += 1

        # The normal case (before we've reached the end of either array)
        elif first[i] < second[j]:
            sortedList.append(first[i])
            i += 1

        else:
            sortedList.append(second[j])
            j += 1


    return sortedList



if __name__ == "__main__":

    a = [4, 2, 234, 9, 1, 10, 2300, 3]
    result = mergeSort(a)

    print("Input:  " + str(a))
    print("Sorted: " + str(result))

    print("All Done!")
