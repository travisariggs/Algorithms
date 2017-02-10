#!/usr/bin/python
"""

      Test Merge Sort
       by Travis Riggs

"""

import unittest
import random

import sorting as s


class TestMergeSort(unittest.TestCase):


    def test_general_case_1(self):
        a = [4, 2, 234, 9, 1, 10, 2300, 3]
        b = [1, 2, 3, 4, 9, 10, 234, 2300]
        self.assertEqual(s.merge_sort(a), b)

    def test_odd_length_array(self):
        a = [3, 9, 2, 4, 1]
        b = [1, 2, 3, 4, 9]
        self.assertEqual(s.merge_sort(a), b)

    def test_long_random_array(self):
        a = [random.randint(-100000, 100000) for i in range(100000)]
        self.assertEqual(s.merge_sort(a), sorted(a))


if __name__ == '__main__':

    unittest.main()