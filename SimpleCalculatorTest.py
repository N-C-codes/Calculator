import unittest

from SimpleCalculator import Calculator

class CalculatorTest(unittest.TestCase):

    def test_add_two_numbers(self):
        calc = Calculator()
        res = calc.add(2,3)
        self.assertEqual(5, res)