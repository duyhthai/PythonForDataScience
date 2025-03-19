import unittest
from unittest.mock import patch
from your_module import index  # Replace 'your_module' with the actual module name

class TestIndex(unittest.TestCase):

    @patch('flask.request')
    def test_index_missing_header(self, mock_request):
        mock_request.headers = {}
        with self.assertRaises(KeyError) as context:
            response = index()
        self.assertIn('Header missing', str(context.exception))

    @patch('flask.request')
    def test_index_invalid_data_type(self, mock_request):
        mock_request.headers = {'Content-Type': 'application/json'}
        mock_request.data = b'invalid_json'
        with self.assertRaises(ValueError) as context:
            response = index()
        self.assertIn('Invalid data type', str(context.exception))

    @patch('flask.request')
    def test_index_empty_data(self, mock_request):
        mock_request.headers = {'Content-Type': 'application/json'}
        mock_request.data = b''
        with self.assertRaises(ValueError) as context:
            response = index()
        self.assertIn('Empty data', str(context.exception))

if __name__ == '__main__':
    unittest.main()