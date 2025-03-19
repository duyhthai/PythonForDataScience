import unittest
from your_module import find_by_id

class TestFindById(unittest.TestCase):
    def setUp(self):
        self.data = [
            {"id": "1", "name": "Alice"},
            {"id": "2", "name": "Bob"}
        ]

    def test_find_by_id_valid_id(self):
        result = find_by_id("1")
        self.assertEqual(result, {"id": "1", "name": "Alice"})

    def test_find_by_id_invalid_id(self):
        result = find_by_id("3")
        self.assertEqual(result, {"message": "Person not found"}, 404)

    def test_find_by_id_non_string_id(self):
        result = find_by_id(3)
        self.assertEqual(result, {"message": "Person not found"}, 404)

if __name__ == '__main__':
    unittest.main()