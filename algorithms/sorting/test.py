from unittest import TestCase

from algorithms.sorting.bubble_sort import bubble_sort
from algorithms.sorting.insertion_sort import insertion_sort
from algorithms.sorting.merge_sort import merge_sort
from algorithms.sorting.selection_sort import selection_sort


tests = [
    (
        [0, 3, 1],
        [0, 1, 3]
    ),
    (
        [0, 5, 1, 2, -1],
        [-1, 0, 1, 2, 5]
    )
]


class TestSort(TestCase):
    def test_bubble_sort(self):
        pass
        for test in tests:
            result, complexity = bubble_sort(test[0])
            self.assertEqual(test[1], result)

    def test_insertion_sort(self):
        pass
        for test in tests:
            result, complexity = insertion_sort(test[0])
            self.assertEqual(test[1], result)

    def test_selection_sort(self):
        pass
        for test in tests:
            result, complexity = selection_sort(test[0])
            self.assertEqual(test[1], result)

    def test_quick_sort(self):
        pass
        for test in tests:
            result, complexity = selection_sort(test[0])
            self.assertEqual(test[1], result)

    def test_merge_sort(self):
        for test in tests:
            result, complexity = merge_sort(test[0])
            self.assertEqual(test[1], result)
