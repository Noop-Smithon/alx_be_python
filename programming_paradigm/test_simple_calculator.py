import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(25, -10), 15)
        self.assertEqual(self.calc.add(0, -10), -10)
        self.assertEqual(self.calc.add(0, 10), 10)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtraction(20, 10), 10)
        self.assertEqual(self.calc.subtraction(-5, -10), 5)
        self.assertEqual(self.calc.subtraction(-21, -9), -30)
        self.assertEqual(self.calc.subtraction(0, 0), 0)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(10, 2), 20)
        self.assertEqual(self.calc.multiply(-1, 6), -6)
        self.assertEqual(self.calc.multiply(0, 240), 0)
        self.assertEqual(self.calc.multiply(-10, -2), 20)

    def test_division(self):
        self.assertEqual(self.calc.divide(50, 25), 2)
        self.assertEqual(self.calc.divide(-50, 2), -25)
        self.assertEqual(self.calc.divide(115, 1), 115)
        self.assertEqual(self.calc.divide(0, 1), 0)
        self.assertEqual(self.calc.division(50, 0), "Error: Division by zero is not allowed.")
        
if __name__ == '__main__':
    unittest.main()