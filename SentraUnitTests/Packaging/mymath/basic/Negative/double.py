import unittest

class TestDoubleFunction(unittest.TestCase):

    def test_double_with_negative_number(self):
        # Arrange
        number = -5
        
        # Act
        result = double(number)
        
        # Assert
        self.assertEqual(result, -10)

    def test_double_with_zero(self):
        # Arrange
        number = 0
        
        # Act
        result = double(number)
        
        # Assert
        self.assertEqual(result, 0)

    def test_double_with_large_positive_number(self):
        # Arrange
        number = 10**10
        
        # Act
        result = double(number)
        
        # Assert
        self.assertEqual(result, 2 * 10**10)

if __name__ == '__main__':
    unittest.main()