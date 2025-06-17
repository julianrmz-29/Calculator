import unittest
from FunctionCalculator.CalculatorOperations import add, sub, mul, div

class TestCalculatorOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 5), 8)

    def test_sub(self):
        self.assertEqual(sub(10, 7), 3)

    def test_mul(self):
        self.assertEqual(mul(4, 6), 24)

    def test_div(self):
        self.assertEqual(div(8, 2), 4.0)

    def test_div_by_zero(self):
        with self.assertRaises(ValueError):
            div(8, 0)


if __name__ == "__main__":
    unittest.main()
