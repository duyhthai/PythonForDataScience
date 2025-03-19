import unittest
from your_module import count  # Replace 'your_module' with the actual module name where the 'count' function is defined

class TestCountFunction(unittest.TestCase):
    def setUp(self):
        global data
        data = []  # Reset the global variable before each test

    def test_empty_data(self):
        response = count()
        self.assertEqual(response[0], {"data_count": 0})
        self.assertEqual(response[1], 200)

    def test_non_empty_data(self):
        global data
        data = [1, 2, 3]
        response = count()
        self.assertEqual(response[0], {"data_count": 3})
        self.assertEqual(response[1], 200)

if __name__ == '__main__':
    unittest.main()