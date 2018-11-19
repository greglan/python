from unittest import TestCase

from data_structures.trees.binarySearchTrees import BinarySearchTree


class TestBinarySearchTree(TestCase):
    def setUp(self):
        t0 = BinarySearchTree()

        t1 = BinarySearchTree(5)

        t2 = BinarySearchTree(5)

        t3 = BinarySearchTree(5)
        t3.insert(2)
        t3.insert(7)
        t3.insert(9)

        self.trees = [t0, t1, t2, t3]

    def test_search(self):
        self.assertEqual(self.trees[1].search(5), True)
        self.assertEqual(self.trees[1].search(1), False)
        self.assertEqual(self.trees[2].search(5), True)
        self.assertEqual(self.trees[2].search(1), False)
        self.assertEqual(self.trees[3].search(5), True)
        self.assertEqual(self.trees[3].search(2), True)
        self.assertEqual(self.trees[3].search(7), True)
        self.assertEqual(self.trees[3].search(10), False)
