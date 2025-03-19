import unittest
from unittest.mock import patch, MagicMock
from your_module import create_person  # Replace 'your_module' with the actual module name

class TestCreatePerson(unittest.TestCase):

    @patch('your_module.request')
    def test_create_person_no_data_provided(self, mock_request):
        mock_request.get_json.return_value = None
        response = create_person()
        self.assertEqual(response, ({'message': 'Invalid input, no data provided'}, 400))

    @patch('your_module.request')
    @patch('your_module.data', new_callable=MagicMock)
    def test_create_person_name_error(self, mock_data, mock_request):
        mock_request.get_json.return_value = {'id': 1}
        with self.assertRaises(NameError):
            create_person()

    @patch('your_module.request')
    def test_create_person_success(self, mock_request):
        mock_request.get_json.return_value = {'id': 1}
        global data
        data = []
        response = create_person()
        self.assertEqual(response, ({'message': '1'}, 201))
        self.assertIn({'id': 1}, data)

if __name__ == '__main__':
    unittest.main()