from unittest import TestCase

from data_structures.trees.binaryHeap import MinHeap, MaxHeap


class TestBinaryMinHeap(TestCase):
    def setUp(self):
        pass

    def test_empty(self):
        test_heap = MinHeap()
        self.assertTrue(test_heap.empty())

        test_heap.insert(4)
        test_heap.get()
        self.assertTrue(test_heap.empty())

    def test_insert(self):
        test_heap = MinHeap()
        test_heap.insert(3)
        test_heap.insert(4)
        test_heap.insert(1)
        test_heap.insert(0)
        test_heap.insert(-1)
        test_heap.insert(5)

        self.assertEqual(test_heap.get(), -1)
        self.assertEqual(test_heap.get(), 0)

    def test_get(self):
        test_heap = MinHeap()
        test_heap.insert(3)
        test_heap.insert(5)
        test_heap.insert(4)
        test_heap.insert(11)
        test_heap.insert(8)
        test_heap.insert(15)
        self.assertEqual(test_heap.get(), 3)
        self.assertEqual(test_heap.get(), 4)
        self.assertEqual(test_heap.get(), 5)


class TestBinaryMaxHeap(TestCase):
    def setUp(self):
        pass

    def test_empty(self):
        test_heap = MaxHeap()
        self.assertTrue(test_heap.empty())

        test_heap.insert(4)
        test_heap.get()
        self.assertTrue(test_heap.empty())

    def test_insert(self):
        test_heap = MaxHeap()
        test_heap.insert(3)
        test_heap.insert(4)
        test_heap.insert(1)
        test_heap.insert(0)
        test_heap.insert(-1)
        test_heap.insert(5)

        self.assertEqual(test_heap.get(), 5)
        self.assertEqual(test_heap.get(), 4)

    def test_get(self):
        test_heap = MaxHeap()
        test_heap.insert(3)
        test_heap.insert(5)
        test_heap.insert(4)
        test_heap.insert(11)
        test_heap.insert(8)
        test_heap.insert(15)
        self.assertEqual(test_heap.get(), 15)
        self.assertEqual(test_heap.get(), 11)
        self.assertEqual(test_heap.get(), 8)
