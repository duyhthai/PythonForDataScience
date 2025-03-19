import unittest
from unittest.mock import patch
from your_module import create_person

class TestCreatePerson(unittest.TestCase):
    @patch('your_module.data', None)
    def test_create_person_no_data_provided(self):
        response = create_person()
        self.assertEqual(response, ({'message': 'Invalid input, no data provided'}, 400))

    @patch('your_module.request.get_json')
    def test_create_person_data_not_dict(self, mock_get_json):
        mock_get_json.return_value = "not a dict"
        response = create_person()
        self.assertEqual(response, ({'message': 'Invalid input, no data provided'}, 400))

    @patch('your_module.request.get_json')
    def test_create_person_missing_id(self, mock_get_json):
        mock_get_json.return_value = {}
        response = create_person()
        self.assertEqual(response, ({'message': 'Invalid input, no data provided'}, 400))

if __name__ == '__main__':
    unittest.main()