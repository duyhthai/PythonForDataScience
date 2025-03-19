import unittest
from unittest.mock import patch
from your_module_name import basic, stats  # Replace 'your_module_name' with actual module name

class TestThrowExceptionScenarios(unittest.TestCase):

    @patch('your_module_name.basic.some_function', side_effect=Exception("Mocked exception"))
    def test_basic_function_exception(self, mock_function):
        with self.assertRaises(Exception) as context:
            basic.some_function()
        self.assertEqual(str(context.exception), "Mocked exception")

    @patch('your_module_name.stats.calculate_stats', side_effect=ZeroDivisionError("Mocked division by zero"))
    def test_stats_calculate_stats_exception(self, mock_function):
        with self.assertRaises(ZeroDivisionError) as context:
            stats.calculate_stats([1, 2, 3])
        self.assertEqual(str(context.exception), "Mocked division by zero")

    @patch('your_module_name.basic.another_function', side_effect=TypeError("Invalid input type"))
    def test_another_function_type_error(self, mock_function):
        with self.assertRaises(TypeError) as context:
            basic.another_function(None)
        self.assertEqual(str(context.exception), "Invalid input type")

if __name__ == '__main__':
    unittest.main()