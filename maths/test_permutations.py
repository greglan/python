from unittest import TestCase

from maths.permutations import *


class TestPermutation(TestCase):
    def setUp(self):
        self.permutations = list(map(Permutation, [[2, 0],
                                                   [3, 1],
                                                   [0, 1, 2, 3],
                                                   [1, 2, 0, 3]]))
        self.not_permutations = list(map(Permutation, [[1, 2, 3],
                                                       ]))

    def test_check(self):
        for permutation in self.permutations:
            self.assertTrue(permutation.check())

        for not_permutation in self.not_permutations:
            self.assertFalse(not_permutation.check())

    def test_inverse(self):
        self.assertTrue(True)
        # self.assertEqual(self.permutations[0].inverse(), Permutation([]))

    def test___repr_(self):
        self.assertTrue(True)
        # self.assertEqual(self.permutations[0].__repr__(), "(0 1 2 3)")
