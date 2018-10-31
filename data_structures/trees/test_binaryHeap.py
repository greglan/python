from unittest import TestCase

from data_structures.trees.binaryHeap import MinHeap


class TestBinaryMinHeap(TestCase):
    def setUp(self):
        self.test_heap = MinHeap()
        self.test_heap.insert(3)
        self.test_heap.insert(5)
        self.test_heap.insert(4)
        self.test_heap.insert(11)
        self.test_heap.insert(8)

    def test_empty(self):
        self.fail()

    def test_insert(self):
        self.test_heap.insert(15)
        self.fail()

    def test_get(self):
        self.fail()
