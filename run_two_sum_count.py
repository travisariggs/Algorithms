#!/usr/bin/python3
"""

        Count the 2-sum Targets
         by Travis Riggs

    Count the number of target values t in the interval [-10000,10000]
    such that there are distinct numbers (x,y) in the input file that
    satisfy x + y = t

"""

import timeit


def two_sum_with_dict(data, start, end):
    """Perform a 2-sum analysis on the data in a dictionary"""

    targetCount = 0

    for t in range(start, end+1):

        print("Searching for addends for the sum {}".format(t))

        for x in data.values():

            try:
                # Try to lookup the needed addend for this x value that
                #  would sum to t
                y = data[t - x]

                # Make sure that x and y are distinct
                if x == y:

                    print("Found addends ({}, {}) for sum {},"
                          " but they aren't distinct".format(x, y, t))

                else:

                    # If we made it here, we found a valid entry in the data
                    targetCount += 1
                    print("Found addends ({}, {}) for sum {}".format(x, y, t))
                    break

            except:
                pass

    print("Target Count: {}".format(targetCount))


##################################################
if __name__ == "__main__":

    data = {}

    # Load the data into a dictionary
    #  The two_sum analysis answer is 427
    with open("data/two_sum.txt", "r") as f:

        for line in f.readlines():

            num = int(line.strip())
            data[num] = num

    # Perform the 2-sum analysis
    timeWithDict = timeit.timeit(two_sum_with_dict(data, -10000, 10000),
                                 globals=globals(),
                                 number=1)

    print("Time using Dictionary: {} seconds".format(timeWithDict))
