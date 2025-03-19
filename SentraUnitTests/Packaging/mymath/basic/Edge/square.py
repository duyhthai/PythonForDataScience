import unittest

class TestSquareFunction(unittest.TestCase):

    def test_square_positive_number(self):
        # Arrange
        number = 5
        
        # Act
        result = square(number)
        
        # Assert
        self.assertEqual(result, 25)

    def test_square_negative_number(self):
        # Arrange
        number = -3
        
        # Act
        result = square(number)
        
        # Assert
        self.assertEqual(result, 9)

    def test_square_zero(self):
        # Arrange
        number = 0
        
        # Act
        result = square(number)
        
        # Assert
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()