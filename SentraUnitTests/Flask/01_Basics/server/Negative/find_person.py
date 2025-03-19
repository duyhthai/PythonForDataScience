import unittest
from your_module import find_person  # Replace 'your_module' with the actual module name

class TestFindPerson(unittest.TestCase):

    def test_missing_argument(self):
        # Arrange
        request.args = {}

        # Act
        response = find_person()

        # Assert
        self.assertEqual(response.status_code, 422)
        self.assertIn('Missing argument \'q\'', str(response.get_data(as_text=True)))

    def test_person_not_found(self):
        # Arrange
        request.args = {'q': 'nonexistent'}

        # Act
        response = find_person()

        # Assert
        self.assertEqual(response.status_code, 404)
        self.assertIn('Person not found', str(response.get_data(as_text=True)))

    def test_invalid_argument_type(self):
        # Arrange
        request.args = {'q': 123}

        # Act
        response = find_person()

        # Assert
        self.assertEqual(response.status_code, 422)
        self.assertIn('Invalid argument type', str(response.get_data(as_text=True)))

if __name__ == '__main__':
    unittest.main()