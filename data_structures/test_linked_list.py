from unittest import TestCase
from data_structures.linked_list import *


class TestSinglyLinkedListNode(TestCase):
    def test_append(self):
        test_list = SinglyLinkedListNode(0)
        test_list.append(1)
        test_list.append(1)
        test_list.append(2)

        self.assertEqual("0 -> 1 -> 1 -> 2", str(test_list))

    def test_size(self):
        test_list = SinglyLinkedListNode(0)
        test_list.append(1)
        test_list.append(1)
        test_list.append(2)

        self.assertEqual(4, test_list.size())


class TestLinkedListNode(TestCase):
    def test_append(self):
        test_list = SinglyLinkedList()
        test_list.append(1)
        test_list.append(1)
        test_list.append(2)

        self.assertEqual("1 -> 1 -> 2", str(test_list))

    def test_size(self):
        test_list = SinglyLinkedList()
        test_list.append(1)
        test_list.append(1)
        test_list.append(2)

        self.assertEqual(3, test_list.size())

    def test_delete(self):
        test_list = SinglyLinkedList()
        test_list.append(0)
        test_list.append(1)
        test_list.append(2)
        test_list.delete(0)
        self.assertEqual("1 -> 2", str(test_list))
        test_list.delete(2)
        self.assertEqual("1", str(test_list))
