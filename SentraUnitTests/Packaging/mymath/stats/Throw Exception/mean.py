import unittest

class TestMeanFunction(unittest.TestCase):

    def test_mean_with_empty_list(self):
        # Arrange
        numbers = []
        
        # Act & Assert
        with self.assertRaises(ZeroDivisionError):
            mean(numbers)

    def test_mean_with_negative_numbers(self):
        # Arrange
        numbers = [-1, -2, -3]
        
        # Act & Assert
        with self.assertRaises(ZeroDivisionError):
            mean(numbers)
            
    def test_mean_with_positive_and_negative_numbers(self):
        # Arrange
        numbers = [1, -2, 3]
        
        # Act & Assert
        with self.assertRaises(ZeroDivisionError):
            mean(numbers)

if __name__ == '__main__':
    unittest.main()