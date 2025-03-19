import unittest
from your_module import api_not_found  # Replace 'your_module' with the actual module name

class TestApiNotFound(unittest.TestCase):
    def test_api_not_found(self):
        response = api_not_found(None)
        self.assertEqual(response[0], {"message": "API not found"})
        self.assertEqual(response[1], 404)

if __name__ == '__main__':
    unittest.main()