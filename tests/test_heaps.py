#!/usr/bin/python3
"""

        Test the Heaps Module
         by Travis Riggs

"""

import unittest
import ipdb

from heaps import Heap


class TestHeap(unittest.TestCase):

    def test_AddElement(self):
        h = Heap()
        h.add_element(1)

    def test_ExtractMin(self):
        h = Heap()
        h.add_element(1)
        self.assertEqual(h.extract_min(), 1)

    def test_ExtractFromEmpty(self):
        h = Heap()
        nothing = h.extract_min()

    def test_ExtractMin_2(self):
        h = Heap()
        h.add_element(3)
        h.add_element(7)
        h.add_element(2)
        self.assertEqual(h.extract_min(), 2)

    def test_ExtractMinFiveTimes(self):
        # ipdb.set_trace()
        h = Heap()
        h.add_element(10)
        h.add_element(13)
        h.add_element(9)
        h.add_element(11)
        h.add_element(12)
        h.add_element(8)
        h.add_element(4)
        h.add_element(7)
        h.add_element(9)
        min4 = h.extract_min()
        min7 = h.extract_min()
        min8 = h.extract_min()
        min9 = h.extract_min()
        min9 = h.extract_min()
        self.assertEqual(min9, 9)

    def test_ExtractLength(self):
        h = Heap()
        h.add_element(9)
        h.add_element(5)
        h.add_element(7)
        h.add_element(2)
        h.add_element(4)
        amin = h.extract_min()
        self.assertEqual(len(h._heap), 4)


if __name__ == "__main__":

    unittest.main()
