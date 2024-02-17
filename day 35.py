'''
Write a simple unit test for a function that adds two numbers
'''
import unittest

def add_numbers(a, b):
    return a + b

class TestAddNumbers(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = add_numbers(3, 5)
        self.assertEqual(result, 8)

    def test_add_negative_numbers(self):
        result = add_numbers(-3, -5)
        self.assertEqual(result, -8)

    def test_add_mixed_numbers(self):
        result = add_numbers(3, -5)
        self.assertEqual(result, -2)

    def test_add_zero_to_number(self):
        result = add_numbers(0, 7)
        self.assertEqual(result, 7)

    def test_add_number_to_zero(self):
        result = add_numbers(7, 0)
        self.assertEqual(result, 7)

if __name__ == '__main__':
    unittest.main()
