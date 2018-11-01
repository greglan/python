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

    def test_is_leaf(self):
        self.assertFalse(self.trees[0].is_leaf())
        self.assertTrue(self.trees[1].is_leaf())
        self.assertTrue(self.trees[2].is_leaf())
        self.assertFalse(self.trees[3].is_leaf())

    def test_search(self):
        self.assertEqual(self.trees[1].search(5), 5)
        self.assertEqual(self.trees[1].search(1), None)
        self.assertEqual(self.trees[2].search(5), 5)
        self.assertEqual(self.trees[2].search(1), None)
        self.assertEqual(self.trees[3].search(5), 5)
        self.assertEqual(self.trees[3].search(2), 2)
        self.assertEqual(self.trees[3].search(7), 7)
        self.assertEqual(self.trees[3].search(10), None)

    def test_insert(self):
        self.fail()

    def test_get_min(self):
        self.fail()

    def test_get_max(self):
        self.fail()

    def test_delete(self):
        self.fail()
