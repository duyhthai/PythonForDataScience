import unittest

class TestMeanFunction(unittest.TestCase):

    def test_mean_with_empty_list(self):
        # Arrange
        numbers = []

        # Act & Assert
        with self.assertRaises(ZeroDivisionError):
            mean(numbers)

    def test_mean_with_single_element(self):
        # Arrange
        numbers = [5]

        # Act
        result = mean(numbers)

        # Assert
        self.assertEqual(result, 5)

    def test_mean_with_multiple_elements(self):
        # Arrange
        numbers = [1, 2, 3, 4, 5]

        # Act
        result = mean(numbers)

        # Assert
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()