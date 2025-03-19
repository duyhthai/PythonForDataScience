import unittest
from your_module import basic, stats

class TestBasic(unittest.TestCase):
    def test_addition(self):
        result = basic.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtraction(self):
        result = basic.subtract(5, 3)
        self.assertEqual(result, 2)

class TestStats(unittest.TestCase):
    def test_mean(self):
        data = [1, 2, 3, 4, 5]
        result = stats.mean(data)
        self.assertEqual(result, 3)

    def test_median(self):
        data = [1, 2, 3, 4, 5]
        result = stats.median(data)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()