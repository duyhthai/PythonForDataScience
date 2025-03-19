import unittest
from unittest.mock import patch
from your_module import delete_by_id, data

class TestDeleteById(unittest.TestCase):

    @patch('your_module.data')
    def test_delete_by_id_person_found(self, mock_data):
        mock_data.return_value = [{"id": "1", "name": "John"}]
        response = delete_by_id("1")
        self.assertEqual(response, {"message": "Person deleted"}, 200)
        self.assertTrue(mock_data[0]["id"] not in [person["id"] for person in mock_data])

    @patch('your_module.data')
    def test_delete_by_id_person_not_found(self, mock_data):
        mock_data.return_value = [{"id": "1", "name": "John"}]
        response = delete_by_id("2")
        self.assertEqual(response, {"message": "Person not found"}, 404)

    @patch('your_module.data')
    def test_delete_by_id_invalid_input_type(self, mock_data):
        mock_data.return_value = [{"id": "1", "name": "John"}]
        with self.assertRaises(TypeError):
            delete_by_id(None)

if __name__ == '__main__':
    unittest.main()