import unittest

class TestDoubleFunction(unittest.TestCase):
    def test_double_positive_number(self):
        # Arrange
        number = 5
        
        # Act
        result = double(number)
        
        # Assert
        self.assertEqual(result, 10)

    def test_double_negative_number(self):
        # Arrange
        number = -3
        
        # Act
        result = double(number)
        
        # Assert
        self.assertEqual(result, -6)

    def test_double_zero(self):
        # Arrange
        number = 0
        
        # Act
        result = double(number)
        
        # Assert
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()