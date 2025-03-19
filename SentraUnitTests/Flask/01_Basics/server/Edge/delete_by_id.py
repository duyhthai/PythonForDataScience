import unittest
from your_module import delete_by_id, data

class TestDeleteById(unittest.TestCase):
    def setUp(self):
        # Arrange
        global data
        data = [
            {"id": "1", "name": "Alice"},
            {"id": "2", "name": "Bob"}
        ]

    def test_delete_existing_person(self):
        # Act
        response = delete_by_id("1")
        
        # Assert
        self.assertEqual(response, {"message": "Person deleted"}, 200)
        self.assertNotIn({"id": "1", "name": "Alice"}, data)

    def test_delete_nonexistent_person(self):
        # Act
        response = delete_by_id("3")
        
        # Assert
        self.assertEqual(response, {"message": "Person not found"}, 404)
        self.assertIn({"id": "1", "name": "Alice"}, data)
        self.assertIn({"id": "2", "name": "Bob"}, data)

    def test_delete_with_empty_data(self):
        # Arrange
        global data
        data = []

        # Act
        response = delete_by_id("1")
        
        # Assert
        self.assertEqual(response, {"message": "Person not found"}, 404)

if __name__ == '__main__':
    unittest.main()