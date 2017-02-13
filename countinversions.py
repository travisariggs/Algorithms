"""

        Count the number of split inversions
        from numbers in a text file.
         by Travis Riggs

"""
import pdb
import comparisons


if __name__ == "__main__":

    # Load all of the numbers from the text file into a list
    with open("/Users/travis/Desktop/IntegerArray.txt", "r") as f:

        numbers = []

        for line in f.readlines():
            numbers.append(int(line))


    # Count the number of inversions in the list
    inversions = comparisons.count_inversions(numbers)

    print("Inversion count = " + str(inversions))