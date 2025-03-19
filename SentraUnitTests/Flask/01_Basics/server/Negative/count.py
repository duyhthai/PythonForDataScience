import unittest
from your_module import count

class TestCount(unittest.TestCase):

    def test_empty_data(self):
        global data
        data = []
        response = count()
        self.assertEqual(response[0], {"data_count": 0})
        self.assertEqual(response[1], 200)

    def test_non_list_data(self):
        global data
        data = "not a list"
        response = count()
        self.assertEqual(response[0], {"data_count": 0})
        self.assertEqual(response[1], 200)

    def test_none_data(self):
        global data
        data = None
        response = count()
        self.assertEqual(response[0], {"data_count": 0})
        self.assertEqual(response[1], 200)

if __name__ == '__main__':
    unittest.main()