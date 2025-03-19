import unittest
from flask import Flask, make_response, request

class TestIndex(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.app = app.test_client()
    
    def test_index_invalid_request_method(self):
        response = self.app.get('/index', follow_redirects=True)
        self.assertEqual(response.status_code, 405)

    def test_index_missing_route(self):
        response = self.app.get('/nonexistent', follow_redirects=True)
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()