from unittest import TestCase

from utils.string_utils import compress


class TestCompress(TestCase):
    def test_compress(self):
        self.assertEqual("a2b1c5a3", compress("aabcccccaaa"))
        self.assertEqual("a3b3c3a3", compress("aaabbbcccaaa"))
        self.assertEqual("a1b1c1d1e1", compress("abcde"))
