from unittest import TestCase
import utilities


class TestData(TestCase):
    def test_generate_random_data(self):
        points = utilities.generate_random_data(10, 2)
        points = utilities.generate_random_data(10, 3)
