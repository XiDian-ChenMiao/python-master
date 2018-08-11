#!/usr/bin/env python
# coding=utf-8


from __future__ import print_function
import unittest


try:
    raw_input
except NameError:
    raw_input = input


class Heap(object):
    """
    the heap data structure
    :param data: stored data
    :param cursize: the size of heap
    """
    def __init__(self):
        self.data = []
        self.cursize = 0


    def left_child(self, i):
        """
        the left-child location of given index
            :param i: given index
        """
        if 2 * i + 1 < self.cursize:
            return 2 * i + 1
        return None


    def right_child(self, i):
        """
        the right-child location of given index
            :param i: given index
        """
        if 2 * i + 2 < self.cursize:
            return 2 * i + 2
        return None


    def max_heapify(self, index):
        """
        heapify the heap to be maxium
            :param index: the index location
        """
        if index < self.cursize:
            m = index
            left, right = self.left_child(index), self.right_child(index)
            if left is not None and self.data[left] > self.data[m]:
                m = left
            if right is not None and self.data[right] > self.data[m]:
                m = right
            if m != index:
                self.data[index], self.data[m] = self.data[m], self.data[index]
                self.max_heapify(m)


    def build_heap(self, arr):
        """
        build a heap with array data
            :param arr: array data
        """
        self.cursize = len(arr)
        self.data = list(arr)
        for i in range(self.cursize / 2, -1, -1):
            self.max_heapify(i)


    def get_max(self):
        if self.cursize >= 1:
            result = self.data[0]
            self.data[0], self.data[self.cursize - 1] = self.data[self.cursize - 1], self.data[0]
            self.cursize = self.cursize - 1
            self.max_heapify(0)
            return result
        return None

    def heap_sort(self):
        """
        the algorithm of heap sort
        """
        size = self.cursize
        while self.cursize >= 1:
            self.data[0], self.data[self.cursize - 1] = self.data[self.cursize - 1], self.data[0]
            self.cursize = self.cursize - 1
            self.max_heapify(0)
        self.cursize = size


    def insert(self, data):
        """
        insert function
            :param data: data information
        """
        self.data.append(data)
        cursize = self.cursize
        self.cursize = self.cursize + 1
        while self.data[cursize] > self.data[cursize / 2]:
            self.data[cursize], self.data[cursize / 2] = self.data[cursize / 2], self.data[cursize]
            cursize = cursize / 2


    def display(self):
        print(self.data)


class HeapTest(unittest.TestCase):

    def setUp(self):
        self.heap = Heap()
        self.heap.build_heap([3, 1, 2])

    def tearDown(self):
        pass

    def test_get_left(self):
        self.assertTrue(self.heap.left_child(0) == 1)

    def test_get_right(self):
        self.assertTrue(self.heap.right_child(0) == 2)

    def test_get_max(self):
        self.assertTrue(self.heap.get_max() == 3)

    def test_get_insert(self):
        self.heap.insert(4)
        self.assertTrue(self.heap.get_max() == 4)


if __name__ == '__main__':
    unittest.main(verbosity=2)
