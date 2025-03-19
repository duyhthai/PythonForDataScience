import unittest

class TestMeanFunction(unittest.TestCase):
    
    def test_mean_with_positive_numbers(self):
        # Arrange
        numbers = [1, 2, 3, 4, 5]
        
        # Act
        result = mean(numbers)
        
        # Assert
        self.assertEqual(result, 3.0)
    
    def test_mean_with_negative_numbers(self):
        # Arrange
        numbers = [-1, -2, -3, -4, -5]
        
        # Act
        result = mean(numbers)
        
        # Assert
        self.assertEqual(result, -3.0)
    
    def test_mean_with_mixed_numbers(self):
        # Arrange
        numbers = [1, -2, 3, -4, 5]
        
        # Act
        result = mean(numbers)
        
        # Assert
        self.assertEqual(result, 0.0)

# Note: Ensure 'mean' function is defined in the same scope or imported before running this test case.

if __name__ == '__main__':
    unittest.main()