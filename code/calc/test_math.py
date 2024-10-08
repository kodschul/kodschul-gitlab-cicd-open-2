from unittest import TestCase
import math_calc

class Testmath_calc(TestCase):

    def test_add(self):
        self.assertEqual(math_calc.add(1, 2), 3)
        self.assertEqual(math_calc.add(-1, 1), 0)
        self.assertEqual(math_calc.add(-1, -1), -2)
        self.assertEqual(math_calc.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(math_calc.subtract(2, 1), 1)
        self.assertEqual(math_calc.subtract(-1, 1), -2)
        self.assertEqual(math_calc.subtract(-1, -1), 0)
        self.assertEqual(math_calc.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(math_calc.multiply(2, 3), 6)
        self.assertEqual(math_calc.multiply(-1, 1), -1)
        self.assertEqual(math_calc.multiply(-1, -1), 1)
        self.assertEqual(math_calc.multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(math_calc.divide(6, 2), 3)
        self.assertEqual(math_calc.divide(-6, 3), -2)
        self.assertEqual(math_calc.divide(0, 1), 0)

        with self.assertRaises(ValueError):
            math_calc.divide(2, 0)
