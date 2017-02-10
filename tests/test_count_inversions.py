"""

    Test Count Inversions
     by Travis Riggs

"""

import unittest

import comparisons as c



class TestCountInversions(unittest.TestCase):


    def test_general_case_1(self):
        # Has inversions (3,2), (5,2) & (5,4) -> 3 inversions
        a = [1, 3, 5, 2, 4, 6]
        self.assertEqual(c.count_inversions(a), 3)

    def test_no_split_inversions(self):
        a = [3, 2, 1, 6, 5, 4]
        self.assertEqual(c.count_inversions(a), 6)



class TestSortAndCountInversions(unittest.TestCase):


    def test_sorted_case_1(self):
        a = [1, 3, 5, 2, 4, 6]
        b = [1, 2, 3, 4, 5, 6]
        i, sortedA = c.sort_and_count_inversions(a)
        self.assertEqual(sortedA, b)

    def test_inv_count_case_1(self):
        a = [1, 3, 5, 2, 4, 6]
        invCount, b = c.sort_and_count_inversions(a)
        self.assertEqual(invCount, 3)



if __name__ == '__main__':

    unittest.main()