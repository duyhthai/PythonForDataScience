import unittest
from unittest.mock import patch
from your_module import get_data  # Replace 'your_module' with the actual module name

class TestDataRetrieval(unittest.TestCase):
    
    @patch('flask.request')
    def test_get_data_with_valid_request(self, mock_request):
        # Arrange
        mock_request.args = {'key': 'value'}
        
        # Act
        response = get_data()
        
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertIn('key', response.json)

    @patch('flask.request')
    def test_get_data_with_empty_request(self, mock_request):
        # Arrange
        mock_request.args = {}
        
        # Act
        response = get_data()
        
        # Assert
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

    @patch('flask.request')
    def test_get_data_with_invalid_request(self, mock_request):
        # Arrange
        mock_request.args = {'invalid_key': None}
        
        # Act
        response = get_data()
        
        # Assert
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

if __name__ == '__main__':
    unittest.main()