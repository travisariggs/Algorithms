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
        self.assertEqual(c.countInversions(a), 3)


if __name__ == '__main__':

    unittest.main()