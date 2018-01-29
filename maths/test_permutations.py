from unittest import TestCase
from maths.permutations import *


class TestPermutation(TestCase):
    def __init__(self):
        self.permutations = []

    def test_check(self):
        self.assertTrue(Permutation([0,1,2,3]).check())
        self.assertTrue(Permutation([1,2,0,3]).check())
        self.assertFalse(Permutation([1,2,3]).check())
        #self.fail()

    def test_inverse(self):
        self.assertTrue()