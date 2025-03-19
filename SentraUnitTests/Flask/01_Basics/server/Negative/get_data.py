import unittest
from unittest.mock import patch
from your_module import get_data

class TestGetData(unittest.TestCase):

    @patch('your_module.request')
    def test_get_data_invalid_request_method(self, mock_request):
        mock_request.method = 'POST'
        response = get_data()
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.data.decode(), 'Method Not Allowed')

    @patch('your_module.request')
    def test_get_data_missing_header(self, mock_request):
        mock_request.method = 'GET'
        mock_request.headers = {}
        response = get_data()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.decode(), 'Missing required header')

    @patch('your_module.request')
    def test_get_data_invalid_header_value(self, mock_request):
        mock_request.method = 'GET'
        mock_request.headers = {'Content-Type': 'application/json'}
        response = get_data()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.decode(), 'Invalid header value')

if __name__ == '__main__':
    unittest.main()