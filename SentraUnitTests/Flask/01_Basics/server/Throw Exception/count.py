import unittest
from unittest.mock import patch
from your_module import count  # Replace 'your_module' with the actual module name

class TestCountFunction(unittest.TestCase):
    
    @patch('your_module.data', None)
    def test_count_with_empty_data(self):
        response = count()
        self.assertEqual(response[0], {"data_count": 0})
        self.assertEqual(response[1], 200)

    @patch('your_module.data', [1, 2, 3])
    def test_count_with_non_empty_data(self):
        response = count()
        self.assertEqual(response[0], {"data_count": 3})
        self.assertEqual(response[1], 200)

if __name__ == '__main__':
    unittest.main()