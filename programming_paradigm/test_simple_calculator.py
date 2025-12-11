#test_simple_calculator.py
import unittest 
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.Testcase):
    def setUp(self):
        self.calculator = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(3, 5), 8)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 4), 6)
        self.assertEqual(self.calculator.subtract(-1, -1), 0)
        self.assertEqual(self.calculator.subtract(-1, 1), -2)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3, 7), 21)
        self.assertEqual(self.calculator.multiply(-1, 1), -1)
        self.assertEqual(self.calculator.multiply(-2, -3), 6)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(8, 2), 4)
        self.assertEqual(self.calculator.divide(5, 0), None)
        self.assertEqual(self.calculator.divide(-6, -2), 3)