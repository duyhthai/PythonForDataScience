import unittest
from your_module import find_by_id

class TestFindById(unittest.TestCase):
    def setUp(self):
        self.data = [
            {"id": "1", "name": "Alice"},
            {"id": "2", "name": "Bob"}
        ]

    def test_find_by_id_found(self):
        result = find_by_id("1", self.data)
        self.assertEqual(result, {"id": "1", "name": "Alice"})

    def test_find_by_id_not_found(self):
        with self.assertRaises(Exception) as context:
            find_by_id("3", self.data)
        self.assertIn("Person not found", str(context.exception))

if __name__ == '__main__':
    unittest.main()