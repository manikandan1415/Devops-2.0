# test_calculator.py
import unittest
from calculator import add, subtract, multiply, divide, calculate

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(-6, 3), -2)
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_calculate(self):
        self.assertEqual(calculate("1", 2, 3), 5)
        self.assertEqual(calculate("2", 5, 3), 2)
        self.assertEqual(calculate("3", 2, 4), 8)
        self.assertEqual(calculate("4", 8, 2), 4)
        with self.assertRaises(ZeroDivisionError):
            calculate("4", 1, 0)
        with self.assertRaises(ValueError):
            calculate("6", 1, 1)

if __name__ == "__main__":
    unittest.main()
