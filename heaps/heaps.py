#!/usr/bin/python3
"""

        Heap Data Structures
         by Travis Riggs

    This module implements Heap data structures.

"""

import ipdb


class Heap(object):


    def __init__(self):
        self._heap = []


    def __repr__(self):

        s = []

        level = 0
        index = 0

        ipdb.set_trace()

        while index < len(self._heap):

            line = []
            for j in range(2**level):
                try:
                    line.append(str(self._heap[index]))
                    index += 1
                except:
                    break

            s.append("\t".join(line))
            level += 1

        return "\n".join(s)


    def add_element(self, element):

        # Add the element to the end of the array
        self._heap.append(element)
        element_index = len(self._heap) - 1

        # Now, bubble it up to the appropriate place
        while True:

            parent_index = self._get_parent_index(element_index)

            if parent_index is not None:

                # Is the parent greater than the child?
                if self._heap[parent_index] > self._heap[element_index]:
                    # Swap them
                    parent = self._heap[parent_index]
                    self._heap[parent_index] = element
                    self._heap[element_index] = parent

                    # Reassign the element's index
                    element_index = parent_index

                else:
                    # We have satisfied the heap criteria
                    break

            else:
                # We have reached the root of the heap tree
                break


    def extract_min(self):

        # Is the heap empty?
        if len(self._heap) == 0:
            return None

        the_min = self._heap[0]

        # Place the last element into the root position
        self._heap[0] = self._heap[-1]

        # Pop off the last element
        self._heap.pop()

        # Is the heap empty?
        if len(self._heap) == 0:
            return the_min

        element = self._heap[0]
        element_index = 0

        # Now bubble it down to its appropriate place
        while True:

            # Think of the children!! ;)
            left_child_index  = self._get_left_child_index(element_index)
            right_child_index = self._get_right_child_index(element_index)

            if left_child_index is not None:
                left_child = self._heap[left_child_index]
            if right_child_index is not None:
                right_child = self._heap[right_child_index]

            # Does this element have children?
            if left_child_index is None and right_child_index is None:

                # We have satisified the heap criteria
                break

            # Does this element have 2 children?
            elif left_child_index is not None and right_child_index is not None:

                # Which child is less?
                if left_child < right_child:
                    min_child = left_child
                    min_child_index = left_child_index
                else:
                    min_child = right_child
                    min_child_index = right_child_index

            elif left_child_index is not None:

                # This element only has a Left Child
                min_child = left_child
                min_child_index = left_child_index

            elif right_child_index is not None:

                # This element only has a Right Child
                min_child = right_child
                min_child_index = right_child_index

            # Is this parent greater than either of its children?
            if element > min_child:

                # Swap them
                self._heap[element_index] = min_child
                self._heap[min_child_index] = element

                # Reassign the element's index
                element_index = min_child_index

            else:
                # We have satified the heap criteria
                break

        return the_min


    def _get_parent_index(self, element_index):

        if element_index == 0:
            return None

        if element_index % 2 == 0:
            return int(element_index/2 - 1)
        else:
            return int((element_index - 1)/2)


    def _get_left_child_index(self, element_index):

        index = int(2*element_index + 1)

        if index > len(self._heap) - 1:
            return None
        else:
            return index


    def _get_right_child_index(self, element_index):

        index = int(2*element_index + 2)

        if index > len(self._heap) - 1:
            return None
        else:
            return index


    def _bubble_up(self, element_index):
        pass


if __name__ == "__main__":


    heap = Heap()
    heap.add_element(10)
    heap.add_element(13)
    heap.add_element(9)
    heap.add_element(11)
    # heap.add_element(12)
    # heap.add_element(8)
    # heap.add_element(4)
    # heap.add_element(7)
    # heap.add_element(9)

    print(heap)

    min4 = heap.extract_min()
    min7 = heap.extract_min()
    min8 = heap.extract_min()
    min9 = heap.extract_min()
    min9 = heap.extract_min()

