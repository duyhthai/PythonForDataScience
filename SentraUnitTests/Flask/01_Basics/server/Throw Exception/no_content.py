import unittest
from your_module_name import no_content  # Replace 'your_module_name' with the actual module name

class TestNoContent(unittest.TestCase):
    def test_no_content_status_code(self):
        response = no_content()
        self.assertEqual(response[1], 204)

    def test_no_content_message(self):
        response = no_content()
        self.assertEqual(response[0], "No conttent found")

if __name__ == '__main__':
    unittest.main()