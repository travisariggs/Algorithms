"""

        Test the Statistical Selection Functions
         by Travis Riggs

"""

import unittest

import selection as s

class TestRandomizedSelection(unittest.TestCase):


    def test_median_case_1(self):
        a = [10,4,1,8,6]
        self.assertEqual(6, s.select_ordered_stat_random(a, 3))

    def test_min_case_1(self):
        a = [100,2,7,9,22]
        self.assertEqual(2, s.select_ordered_stat_random(a, 1))

    def test_max_case_1(self):
        a = [5,1,2,6,9,100,3]
        self.assertEqual(100, s.select_ordered_stat_random(a, 7))

    def test_sorted_median(self):
        a = [2,4,6,8,10]
        self.assertEqual(6, s.select_ordered_stat_random(a, 3))


if __name__ == '__main__':

    unittest.main()