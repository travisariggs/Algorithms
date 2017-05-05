#!/usr/bin/python3
"""

        Hash Table
         by Travis Riggs

    This is an implementation of a Hash Table.

"""

import math
import copy
import random


class HashTable(object):
    """A custom implementation of a hash table (for learning)"""

    def __init__(self, salt=None):

        # Start with an array of size 16
        self.size = 8
        self.data = [None]*self.size
        self.occupied = 0

        if salt is None:
            random.seed()
            self.salt = random.randint(11,1001)
        else:
            self.salt = salt

    def _hash(self, key):
        """Calculate the hash value of the key"""

        return key

    def _index_gen(self, aHash):
        """Generator to produce indices into the data array"""

        index = aHash % self.size
        yield index

        while True:
            index = (5*index + self.salt + aHash + 1) % self.size
            yield index
            aHash >>= 5

    def add_elem(self, key, value):
        """Add an element to the hash table"""

        the_hash = self._hash(key)

        for index in self._index_gen(the_hash):

            contents = self.data[index]

            # Is this location occupied?
            if contents is None:

                # Add the hash, key and value to the array
                self.data[index] = (the_hash, key, value)
                self.occupied += 1
                self._check_load()
                break

            # Has this key already been added?
            elif contents[0] == the_hash and contents[1] == key:

                # Only update it if it's changed
                if contents[2] != value:
                    self.data[index] = (the_hash, key, value)

                break

    def get_elem(self, key):
        """Return an element from the hash table.
        Returns None if item isn't found.
        """

        the_hash = self._hash(key)

        for index in self._index_gen(the_hash):

            # Is this location occupied?
            contents = self.data[index]
            if contents is None:

                # This key has not been entered into the hash table
                return None

            # There are contents, but do they match the hash and key?
            elif contents[0] == the_hash and contents[1] == key:
                # We found the desired value!
                return contents[2]

        print("WARNING: We couldn't find the key or an empty spot")
        return None

    def delete_elem(self, key):
        """Delete an element from the hash table"""

        # Delete a hash/key/value set from the array, but place a "dummy"
        #  in its place.
        the_hash = self._hash(key)

        #  for shift in range(0, 32*self.shift, self.shift):
        for index in self._index_gen(the_hash):

            # Is this location occupied?
            contents = self.data[index]
            if contents is None:

                # This key has not been entered into the hash table
                return None

            # There are contents, but do they match the hash and key?
            elif contents[0] == the_hash and contents[1] == key:
                # We found the desired value!
                self.data[index] = (None, None, None)

        print("WARNING: We couldn't find the key or an empty spot")
        return None

    def _check_load(self):
        """Make sure the size the array is large enough to avoid most
        collisions."""

        if self.occupied/self.size > 0.67:

            self._grow_array()

    def _grow_array(self):
        """Grow the size of the array and re-insert the data"""

        # Copy the current array
        olddata = copy.deepcopy(self.data)
        self.occupied = 0

        # Double the size of the array
        self.size = 2*self.size

        self.data = [None]*self.size

        # Re-write the data into the new array
        for contents in olddata:

            if contents is None:
                continue
            elif contents is (None, None, None):
                continue
            else:
                self.add_elem(contents[1], contents[2])
