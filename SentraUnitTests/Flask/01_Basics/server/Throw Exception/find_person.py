import unittest
from unittest.mock import patch
from app import find_person

class TestFindPerson(unittest.TestCase):
    
    @patch('app.find_person')
    def test_find_person_with_argument(self, mock_find_person):
        # Arrange
        mock_find_person.return_value = {'name': 'John', 'age': 30}
        
        # Act
        response = find_person()
        
        # Assert
        mock_find_person.assert_called_once_with(request.args.get('q'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'name': 'John', 'age': 30})
    
    @patch('app.find_person')
    def test_find_person_without_argument(self, mock_find_person):
        # Arrange
        mock_find_person.side_effect = ValueError("Missing argument 'q'")
        
        # Act & Assert
        with self.assertRaises(ValueError) as context:
            find_person()
        self.assertIn("Missing argument 'q'", str(context.exception))
    
    @patch('app.find_person')
    def test_find_person_not_found(self, mock_find_person):
        # Arrange
        mock_find_person.return_value = None
        
        # Act
        response = find_person()
        
        # Assert
        mock_find_person.assert_called_once_with(request.args.get('q'))
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()