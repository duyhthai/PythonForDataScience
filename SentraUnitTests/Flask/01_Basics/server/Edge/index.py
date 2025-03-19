import unittest
from unittest.mock import patch
from your_module import index  # Replace 'your_module' with the actual module name where index function is defined

class TestIndex(unittest.TestCase):
    @patch('flask.request')
    def test_index_empty_request(self, mock_request):
        mock_request.method = 'GET'
        mock_request.headers = {}
        response = index()
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, World!', response.data)

    @patch('flask.request')
    def test_index_with_query_params(self, mock_request):
        mock_request.method = 'GET'
        mock_request.args = {'name': 'Alice'}
        response = index()
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, Alice!', response.data)

    @patch('flask.request')
    def test_index_with_header(self, mock_request):
        mock_request.method = 'GET'
        mock_request.headers = {'User-Agent': 'Mozilla'}
        response = index()
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, Mozilla!', response.data)

if __name__ == '__main__':
    unittest.main()