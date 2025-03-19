import unittest
from your_module import index  # Replace 'your_module' with the actual module name

class TestIndex(unittest.TestCase):
    def test_index_without_query_params(self):
        app = Flask(__name__)
        app.add_url_rule('/', 'index', index)
        
        client = app.test_client()
        response = client.get('/')
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, World!', response.data)

    def test_index_with_query_params(self):
        app = Flask(__name__)
        app.add_url_rule('/', 'index', index)
        
        client = app.test_client()
        response = client.get('/?name=TestUser')
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, TestUser!', response.data)

    def test_index_with_empty_query_param(self):
        app = Flask(__name__)
        app.add_url_rule('/', 'index', index)
        
        client = app.test_client()
        response = client.get('/?name=')
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, !', response.data)

if __name__ == '__main__':
    unittest.main()