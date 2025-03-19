import unittest
from your_module_name import index_explicit  # Replace 'your_module_name' with the actual module name where index_explicit is defined

class TestIndexExplicit(unittest.TestCase):

    def test_index_explicit_status_code(self):
        # Arrange
        # No setup required
        
        # Act
        response = index_explicit()
        
        # Assert
        self.assertEqual(response.status_code, 200)
    
    def test_index_explicit_content_type(self):
        # Arrange
        # No setup required
        
        # Act
        response = index_explicit()
        
        # Assert
        self.assertEqual(response.content_type, 'application/json')
    
    def test_index_explicit_message(self):
        # Arrange
        # No setup required
        
        # Act
        response = index_explicit()
        
        # Assert
        data = response.get_json()
        self.assertEqual(data['message'], 'Using make_response')

if __name__ == '__main__':
    unittest.main()