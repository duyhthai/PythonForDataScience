import unittest
from your_module import delete_by_id, data

class TestDeleteById(unittest.TestCase):
    def setUp(self):
        global data
        data = [
            {"id": "1", "name": "Alice"},
            {"id": "2", "name": "Bob"}
        ]

    def tearDown(self):
        global data
        data = []

    def test_delete_existing_person(self):
        response = delete_by_id("1")
        self.assertEqual(response, {"message": "Person deleted"}, 200)
        self.assertEqual(len(data), 1)

    def test_delete_non_existent_person(self):
        response = delete_by_id("3")
        self.assertEqual(response, {"message": "Person not found"}, 404)
        self.assertEqual(len(data), 2)

    def test_delete_person_with_invalid_id_type(self):
        with self.assertRaises(TypeError):
            delete_by_id({"id": "1"})

if __name__ == '__main__':
    unittest.main()