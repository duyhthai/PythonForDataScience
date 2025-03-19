import unittest
from your_module import find_person  # Replace 'your_module' with the actual module name

class TestFindPerson(unittest.TestCase):
    def setUp(self):
        app = Flask(__name__)
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_find_person_found(self):
        # Arrange
        query = {'q': 'John Doe'}
        
        # Act
        response = find_person(query)
        
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertIn('John Doe', response.get_data(as_text=True))

    def test_find_person_not_found(self):
        # Arrange
        query = {'q': 'Jane Smith'}
        
        # Act
        response = find_person(query)
        
        # Assert
        self.assertEqual(response.status_code, 404)

    def test_find_person_missing_argument(self):
        # Arrange
        query = {}
        
        # Act
        response = find_person(query)
        
        # Assert
        self.assertEqual(response.status_code, 422)

if __name__ == '__main__':
    unittest.main()