import unittest
from unittest.mock import patch
from your_module import no_content  # Replace 'your_module' with the actual module name

class TestNoContent(unittest.TestCase):

    @patch('flask.request')
    def test_no_content(self, mock_request):
        response = no_content()
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data.decode(), "No content found")

    @patch('flask.request', side_effect=Exception("Mock exception"))
    def test_no_content_exception(self, mock_request):
        with self.assertRaises(Exception) as context:
            no_content()
        self.assertTrue("Mock exception" in str(context.exception))

if __name__ == '__main__':
    unittest.main()