import unittest

class TestMeanFunction(unittest.TestCase):

    def test_mean_with_empty_list(self):
        # Arrange
        numbers = []
        
        # Act & Assert
        with self.assertRaises(ZeroDivisionError):
            mean(numbers)

    def test_mean_with_non_numeric_values(self):
        # Arrange
        numbers = [1, 'a', 3]
        
        # Act & Assert
        with self.assertRaises(TypeError):
            mean(numbers)

    def test_mean_with_negative_numbers(self):
        # Arrange
        numbers = [-1, -2, -3]
        
        # Act
        result = mean(numbers)
        
        # Assert
        self.assertEqual(result, -2)

if __name__ == '__main__':
    unittest.main()