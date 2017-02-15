"""

    Test the Quicksort module
     by Travis Riggs

"""

import unittest

import sorting as s


class TestQuicksort(unittest.TestCase):


    def test_case_1(self):
        a = [8,7,6,5,4,3,2,1]
        b = [1,2,3,4,5,6,7,8]
        self.assertEqual(b, s.quick_sort(a))

    def test_case_2(self):
        a = [2,4,1,3]
        b = [1,2,3,4]
        self.assertEqual(b, s.quick_sort(a))

    def test_odd_length(self):
        a = [3,5,1,7,2]
        b = [1,2,3,5,7]
        self.assertEqual(b, s.quick_sort(a))

    def test_already_sorted(self):
        a = [1,2,3,4,5,6]
        self.assertEqual(a, s.quick_sort(a))


if __name__ == '__main__':

    unittest.main()