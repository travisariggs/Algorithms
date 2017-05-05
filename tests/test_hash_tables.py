#!/usr/bin/python3
"""

        Test the Hash Tables Module
         by Travis Riggs

"""

import unittest
from hash_tables import HashTable
import ipdb


class TestHashTables(unittest.TestCase):

    def setUp(self):
        pass

    def test_initial(self):
        ht = HashTable()

    def test_insert_1(self):
        ht = HashTable()
        ht.add_elem(1, "one")
        self.assertEqual("one", ht.get_elem(1))

    def test_repeated_insert(self):
        ht = HashTable()
        ht.add_elem(1, "one")
        ht.add_elem(1, "one")
        count = 0

        for contents in ht.data:
            if contents is not None:
                if contents[1] == 1 and contents[2] == "one":
                    count += 1

        self.assertEqual(1, count)

    def test_collision_1(self):
        ht = HashTable(salt=0)
        ht.add_elem(0, "zero")
        ht.add_elem(8, "eight")
        self.assertEqual("eight", ht.get_elem(8))

    def test_collision_2(self):
        ht = HashTable(salt=0)
        ht.add_elem(8, "eight")
        ht.add_elem(0, "zero")
        self.assertEqual("zero", ht.get_elem(0))

    def test_grow_1(self):
        ht = HashTable()
        for i in range(6):
            ht.add_elem(i, i)

        self.assertEqual(16, ht.size)

    @unittest.skip("To save time...")
    def test_large_data(self):
        with open("data/two_sum.txt", "r") as f:
            keys = []
            ht = HashTable()
            #  ht = {}
            for line in f.readlines():
                num = int(line.strip())
                keys.append(num)
                ht.add_elem(num, num)
                #  ht[num] = num

        foundAllKeys = True
        for key in keys:
            if ht[key] != key:
            #  if ht.get_elem(key) != key:
                foundAllKeys = False

        self.assertTrue(foundAllKeys)


if __name__ == "__main__":

    unittest.main()
