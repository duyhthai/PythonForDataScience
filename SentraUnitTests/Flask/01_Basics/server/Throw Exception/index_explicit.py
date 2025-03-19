import unittest
from app import index_explicit

class TestIndexExplicit(unittest.TestCase):
    def test_index_explicit(self):
        # Arrange
        # No setup required
        
        # Act
        response = index_explicit()
        
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Using make_response"})

if __name__ == '__main__':
    unittest.main()