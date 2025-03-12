import unittest
from mymath import basic, stats


class TestBasic(unittest.TestCase):
    def test_add(self):
        self.assertEqual(basic.add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(basic.square(2), 4)

unittest.main()