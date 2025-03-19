import unittest
from app import no_content

class TestNoContent(unittest.TestCase):
    def test_no_content_status_code(self):
        response = no_content()
        self.assertEqual(response.status_code, 204)

    def test_no_content_message(self):
        response = no_content()
        self.assertEqual(response.data.decode('utf-8'), "No conttent found")

if __name__ == '__main__':
    unittest.main()