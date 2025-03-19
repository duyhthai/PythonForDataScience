import unittest
from unittest.mock import patch
from your_module import find_by_id, data

class TestFindById(unittest.TestCase):

    @patch('your_module.data')
    def test_find_by_id_found(self, mock_data):
        # Arrange
        mock_data.return_value = [{"id": "1", "name": "John Doe"}]
        expected_result = {"id": "1", "name": "John Doe"}
        
        # Act
        result = find_by_id("1")
        
        # Assert
        self.assertEqual(result, expected_result)

    @patch('your_module.data')
    def test_find_by_id_not_found(self, mock_data):
        # Arrange
        mock_data.return_value = [{"id": "1", "name": "John Doe"}]
        
        # Act
        result = find_by_id("2")
        
        # Assert
        self.assertEqual(result, {"message": "Person not found"}, 404)

    @patch('your_module.data')
    def test_find_by_id_empty_data(self, mock_data):
        # Arrange
        mock_data.return_value = []
        
        # Act
        result = find_by_id("1")
        
        # Assert
        self.assertEqual(result, {"message": "Person not found"}, 404)

if __name__ == '__main__':
    unittest.main()