import unittest

class TestMedian(unittest.TestCase):

    def test_median_odd_numbers(self):
        # Arrange
        numbers = [3, 1, 2, 4, 5]
        
        # Act
        result = median(numbers)
        
        # Assert
        self.assertEqual(result, 3)

    def test_median_even_numbers(self):
        # Arrange
        numbers = [-10, 4, 6, 1000, 10, 20]
        
        # Act
        result = median(numbers)
        
        # Assert
        self.assertEqual(result, 15.0)

    def test_median_empty_list(self):
        # Arrange
        numbers = []
        
        # Act & Assert
        with self.assertRaises(ValueError):
            median(numbers)

if __name__ == '__main__':
    unittest.main()