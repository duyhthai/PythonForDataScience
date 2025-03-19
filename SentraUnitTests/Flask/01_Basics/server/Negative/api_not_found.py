import unittest
from unittest.mock import patch
from your_module import api_not_found  # Replace 'your_module' with the actual module name

class TestApiNotFound(unittest.TestCase):
    
    def test_api_not_found_with_string(self):
        with self.assertRaises(TypeError) as context:
            api_not_found("Invalid input")
        self.assertIn("'error' must be an instance of Exception", str(context.exception))

    @patch('flask.jsonify')
    def test_api_not_found_with_exception(self, mock_jsonify):
        error = Exception("Mock exception")
        response = api_not_found(error)
        self.assertEqual(response, {"message": "API not found"})
        mock_jsonify.assert_called_once_with({"message": "API not found"})

    @patch('flask.Response')
    def test_api_not_found_with_custom_status_code(self, mock_Response):
        error = Exception("Custom status code")
        response = api_not_found(error)
        self.assertEqual(response, {"message": "API not found"})
        mock_Response.assert_called_once_with(json={"message": "API not found"}, status=404)

if __name__ == '__main__':
    unittest.main()