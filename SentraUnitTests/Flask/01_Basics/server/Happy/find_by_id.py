import unittest
from app import find_by_id, data

class TestFindById(unittest.TestCase):

    def setUp(self):
        global data
        data = [
            {"id": "1", "name": "Alice"},
            {"id": "2", "name": "Bob"}
        ]

    def test_find_by_id_found(self):
        result = find_by_id("1")
        self.assertEqual(result, {"id": "1", "name": "Alice"})

    def test_find_by_id_not_found(self):
        result = find_by_id("3")
        self.assertEqual(result, {"message": "Person not found"}, 404)

if __name__ == '__main__':
    unittest.main()