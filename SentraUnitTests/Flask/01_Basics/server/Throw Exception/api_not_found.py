import unittest
from flask import Flask, request
from your_module import api_not_found  # Replace 'your_module' with the actual module name

class TestApiNotFound(unittest.TestCase):
    def test_api_not_found(self):
        # Arrange
        app = Flask(__name__)
        
        @app.route('/nonexistent', methods=['GET'])
        def nonexistent_route():
            raise Exception("This route does not exist")
        
        client = app.test_client()
        
        # Act
        response = client.get('/nonexistent')
        
        # Assert
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"message": "API not found"})

if __name__ == '__main__':
    unittest.main()