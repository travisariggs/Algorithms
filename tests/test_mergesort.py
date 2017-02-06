#!/usr/bin/python
"""

      Test Merge Sort
       by Travis Riggs

"""

import unittest

from mergesort import mergesort as ms


class TestMergeSort(unittest.TestCase):


    def test_general_case_1(self):
        a = [4, 2, 234, 9, 1, 10, 2300, 3]
        b = [1, 2, 3, 4, 9, 10, 234, 2300]
        self.assertEqual(ms.mergeSort(a), b)


    def test_odd_length_array(self):
        a = [3, 9, 2, 4, 1]
        b = [1, 2, 3, 4, 9]
        self.assertEqual(ms.mergeSort(a), b)




if __name__ == '__main__':

    unittest.main()