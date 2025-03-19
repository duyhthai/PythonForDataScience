import unittest
from flask import Flask, make_response, request
from your_module import find_person  # Replace 'your_module' with the actual module name

class TestFindPerson(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()

    def test_find_person_with_query(self):
        with self.app.app_context():
            response = self.client.get('/find_person?q=John')
            self.assertEqual(response.status_code, 200)
            data = response.json
            self.assertIn('person', data)

    def test_find_person_without_query(self):
        with self.app.app_context():
            response = self.client.get('/find_person')
            self.assertEqual(response.status_code, 422)
            data = response.json
            self.assertIn('error', data)

    def test_find_person_not_found(self):
        with self.app.app_context():
            response = self.client.get('/find_person?q=Unknown')
            self.assertEqual(response.status_code, 404)
            data = response.json
            self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()