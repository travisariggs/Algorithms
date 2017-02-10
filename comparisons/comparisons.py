"""

    Comparisons Module
     by Travis Riggs

  This module contains functions for performing
  various comparisons of objects.

"""


def count_inversions(aList):
    """Count the number of Inversions in a List

    Returns the inversion count

    On an error, Returns None
    """

    inversionCount = None

    # Get the inversion count
    inversionCount, sortedList = sort_and_count_inversions(aList)

    return inversionCount


def sort_and_count_inversions(aList):
    """Return an inversion count and sorted list"""

    inversionCount = 0
    sortedList = []

    n = len(aList)

    # Check base case
    if n <= 1:
        # If the list has 1 or 0 elements, there are no inversions
        #  and nothing to sort
        return 0, aList

    # Recursively call for first half of list
    firstCount, firstList = sort_and_count_inversions(aList[0:n/2])

    # Recursively call for second half of list
    secondCount, secondList = sort_and_count_inversions(aList[n/2:])

    # Merge the two lists together while looking for split inversions
    firstLength = len(firstList)
    secondLength = len(secondList)
    i = 0
    j = 0

    for z in range(n):

        # Make sure we won't try to access past the end of the array
        #  If we've reachd the end of the first array, then
        #  add the element from the second array.
        if i == firstLength:
            sortedList.append(secondList[j])
            j += 1

        # If we've reached the end of the second array, then add
        #  the element from the first array
        elif j == secondLength:
            sortedList.append(firstList[i])
            i += 1

        # The normal case (before we've reached the end of the arrays)
        elif firstList[i] < secondList[j]:
            sortedList.append(firstList[i])
            i += 1

        else:
            sortedList.append(secondList[j])
            j += 1
            # Here are some split inversions!
            #  ...which is equal to the number of items remaining
            #  in the first list.
            inversionCount += firstLength - i


    # Add the non-split inversions for the final total of inversions
    inversionCount += firstCount + secondCount


    return inversionCount, sortedList

