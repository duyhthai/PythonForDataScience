import unittest
from your_module import count, data  # Replace 'your_module' with the actual module name

class TestCountFunction(unittest.TestCase):

    def setUp(self):
        global data
        data = []  # Reset data before each test

    def test_empty_data(self):
        result, status_code = count()
        self.assertEqual(status_code, 200)
        self.assertEqual(result, {"data_count": 0})

    def test_single_item_data(self):
        data.append("item")
        result, status_code = count()
        self.assertEqual(status_code, 200)
        self.assertEqual(result, {"data_count": 1})

    def test_multiple_items_data(self):
        data.extend(["item1", "item2", "item3"])
        result, status_code = count()
        self.assertEqual(status_code, 200)
        self.assertEqual(result, {"data_count": 3})

if __name__ == '__main__':
    unittest.main()