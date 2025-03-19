import unittest
from your_module import delete_by_id, data  # Replace 'your_module' with the actual module name where delete_by_id is defined

class TestDeleteById(unittest.TestCase):
    
    def setUp(self):
        global data
        data = [
            {"id": "1", "name": "John"},
            {"id": "2", "name": "Jane"}
        ]
    
    def test_delete_existing_person(self):
        response = delete_by_id("1")
        self.assertEqual(response, {"message": "Person deleted"}, 200)
        self.assertEqual(len(data), 1)
    
    def test_delete_nonexistent_person(self):
        response = delete_by_id("3")
        self.assertEqual(response, {"message": "Person not found"}, 404)
        self.assertEqual(len(data), 2)

if __name__ == '__main__':
    unittest.main()