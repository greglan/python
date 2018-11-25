from unittest import TestCase
from data_structures.trees.binarySearchTrees import BinarySearchTree


class TestBinarySearchTree(TestCase):
    def test_insert(self):
        t = BinarySearchTree(5)
        t.insert(2)
        t.insert(7)
        t.insert(9)
        t.insert(-1)
        t.insert(0)
        self.assertEqual(t.get_max(), 9)
        self.assertEqual(t.get_min(), -1)

        t = BinarySearchTree()
        t.insert(-1)
        t.insert(0)
        t.insert(1)
        self.assertEqual(t.get_max(), 1)
        self.assertEqual(t.get_min(), -1)

        t = BinarySearchTree()
        t.insert(0)
        t.insert(1)
        t.insert(0)
        self.assertEqual(t.get_max(), 1)
        self.assertEqual(t.get_min(), 0)

        t = BinarySearchTree(0)
        t.insert(0)
        self.assertEqual(t.get_max(), 0)
        self.assertEqual(t.get_min(), 0)

    def test_search(self):
        t = BinarySearchTree(5)
        t.insert(2)
        t.insert(7)
        t.insert(9)

        self.assertEqual(t.search(5), True)
        self.assertEqual(t.search(1), False)
        self.assertEqual(t.search(5), True)
        self.assertEqual(t.search(1), False)
        self.assertEqual(t.search(5), True)
        self.assertEqual(t.search(2), True)
        self.assertEqual(t.search(7), True)
        self.assertEqual(t.search(10), False)

    def test_delete(self):
        t = BinarySearchTree(5)
        t.insert(9)
        t.insert(-1)
        t.insert(0)

        t.delete(9)
        self.assertEqual(t.get_max(), 5)
        self.assertEqual(t.get_min(), -1)

        t.delete(-1)
        self.assertEqual(t.get_max(), 5)
        self.assertEqual(t.get_min(), 0)

        t = BinarySearchTree(5)
        t.insert(9)
        t.insert(-1)
        t.insert(5)
        t.delete(9)
        self.assertEqual(t.get_max(), 5)

        t.delete(5)
        self.assertEqual(t.get_max(), 5)

