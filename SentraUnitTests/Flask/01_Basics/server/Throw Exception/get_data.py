import unittest
from flask import Flask, request, jsonify
from your_module import get_data  # Replace 'your_module' with the actual module name

class TestGetData(unittest.TestCase):

    def test_get_data_exception(self):
        app = Flask(__name__)

        @app.route('/data', methods=['GET'])
        def data_route():
            return get_data()

        with app.test_request_context('/data'):
            with self.assertRaises(Exception) as context:
                response = data_route()
            self.assertIn('Exception message', str(context.exception))

if __name__ == '__main__':
    unittest.main()