import unittest

class TestSquareFunction(unittest.TestCase):
    def test_negative_input(self):
        with self.assertRaises(TypeError):
            square(-1)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            square("test")

    def test_zero_input(self):
        self.assertEqual(square(0), 0)

if __name__ == '__main__':
    unittest.main()