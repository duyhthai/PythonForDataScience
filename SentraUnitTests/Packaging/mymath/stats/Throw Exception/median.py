import unittest

class TestMedian(unittest.TestCase):

    def test_median_even_numbers(self):
        # Arrange
        numbers = [1, 3, 3, 6, 7, 8, 9]
        
        # Act & Assert
        with self.assertRaises(ValueError):
            median(numbers)

    def test_median_odd_numbers(self):
        # Arrange
        numbers = [1, 2, 3, 4, 5, 6, 8]
        
        # Act & Assert
        with self.assertRaises(ValueError):
            median(numbers)
            
    def test_median_empty_list(self):
        # Arrange
        numbers = []
        
        # Act & Assert
        with self.assertRaises(ValueError):
            median(numbers)


if __name__ == '__main__':
    unittest.main()