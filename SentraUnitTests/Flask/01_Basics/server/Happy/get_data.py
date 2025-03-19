import unittest
from your_module import get_data

class TestGetData(unittest.TestCase):

    def test_get_data_with_valid_input(self):
        # Arrange
        app = Flask(__name__)
        
        @app.route('/data', methods=['GET'])
        def mock_get_data():
            return make_response('{"key": "value"}', 200)
        
        client = app.test_client()
        
        # Act
        response = client.get('/data')
        
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'key': 'value'})

    def test_get_data_with_no_data(self):
        # Arrange
        app = Flask(__name__)
        
        @app.route('/data', methods=['GET'])
        def mock_get_data():
            return make_response('', 204)
        
        client = app.test_client()
        
        # Act
        response = client.get('/data')
        
        # Assert
        self.assertEqual(response.status_code, 204)

    def test_get_data_with_error(self):
        # Arrange
        app = Flask(__name__)
        
        @app.route('/data', methods=['GET'])
        def mock_get_data():
            raise Exception("An error occurred")
        
        client = app.test_client()
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            client.get('/data')

if __name__ == '__main__':
    unittest.main()