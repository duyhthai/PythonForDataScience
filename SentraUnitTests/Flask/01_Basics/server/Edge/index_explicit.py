import unittest
from your_module import index_explicit  # Replace 'your_module' with the actual module name

class TestIndexExplicit(unittest.TestCase):

    def test_index_explicit_success(self):
        # Arrange
        expected_status_code = 200
        expected_message = {"message": "Using make_response"}

        # Act
        response = index_explicit()

        # Assert
        self.assertEqual(response.status_code, expected_status_code)
        self.assertDictEqual(response.get_json(), expected_message)

    def test_index_explicit_empty_response(self):
        # Arrange
        expected_status_code = 200
        expected_message = {}

        # Act
        response = index_explicit()
        response.data = b''  # Simulate an empty response body

        # Assert
        self.assertEqual(response.status_code, expected_status_code)
        self.assertDictEqual(response.get_json(), expected_message)

    def test_index_explicit_non_200_status(self):
        # Arrange
        expected_status_code = 200
        expected_message = {"message": "Using make_response"}
        response = make_response({"message": "Using make_response"})
        response.status_code = 500  # Simulate a non-200 status code

        # Act
        result = index_explicit()

        # Assert
        self.assertNotEqual(result.status_code, expected_status_code)
        self.assertNotEqual(result.get_json(), expected_message)

if __name__ == '__main__':
    unittest.main()