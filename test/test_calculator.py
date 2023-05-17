import unittest

from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(5), 5)
        self.assertEqual(self.calc.add(10), 15)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5), -5)
        self.assertEqual(self.calc.subtract(10), -15)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5), 0)
        self.calc.reset()
        self.calc.add(2)
        self.assertEqual(self.calc.multiply(3), 6)

    def test_divide(self):
        with self.assertRaises(ValueError):
            self.calc.divide(0)
        self.calc.reset()
        self.calc.add(10)
        self.assertEqual(self.calc.divide(2), 5)

    def test_reset(self):
        self.calc.add(5)
        self.calc.subtract(2)
        self.calc.multiply(3)
        self.assertEqual(self.calc.reset(), 0)

if __name__ == '__main__':
    unittest.main()