import unittest
from your_module import no_content

class TestNoContent(unittest.TestCase):
    def test_no_content(self):
        # Arrange
        expected_status_code = 204
        
        # Act
        response = no_content()
        
        # Assert
        self.assertEqual(response[1], expected_status_code)
        self.assertEqual(response[0], "No content found")

if __name__ == '__main__':
    unittest.main()