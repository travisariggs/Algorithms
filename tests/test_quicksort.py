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


if __name__ == '__main__':

    unittest.main()