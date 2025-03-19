import unittest

class TestMedian(unittest.TestCase):
    def test_median_with_empty_list(self):
        with self.assertRaises(ValueError):
            median([])

    def test_median_with_single_element(self):
        result = median([5])
        self.assertEqual(result, 5)

    def test_median_with_odd_number_of_elements(self):
        result = median([1, 3, 2])
        self.assertEqual(result, 2)

    def test_median_with_even_number_of_elements(self):
        result = median([1, 2, 3, 4])
        self.assertEqual(result, 2.5)

    def test_median_with_negative_numbers(self):
        result = median([-3, -1, -2])
        self.assertEqual(result, -2)

    def test_median_with_duplicate_values(self):
        result = median([2, 2, 2, 2])
        self.assertEqual(result, 2)

    def test_median_with_large_numbers(self):
        result = median([1000000, 2000000, 3000000])
        self.assertEqual(result, 2000000)

    def test_median_with_mixed_types(self):
        with self.assertRaises(TypeError):
            median([1, 'a', 3])

if __name__ == '__main__':
    unittest.main()