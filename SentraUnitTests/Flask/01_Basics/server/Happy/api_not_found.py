import unittest
from unittest.mock import patch
from your_module import api_not_found  # Replace 'your_module' with the actual module name

class TestApiNotFound(unittest.TestCase):

    @patch('flask.jsonify')
    def test_api_not_found(self, mock_jsonify):
        error = Exception("Not Found")
        response = api_not_found(error)
        
        mock_jsonify.assert_called_once_with({"message": "API not found"})
        self.assertEqual(response[1], 404)

if __name__ == '__main__':
    unittest.main()