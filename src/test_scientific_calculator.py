import unittest
from src.scientific_calculator import ScientificCalculator

class TestScientificCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = ScientificCalculator()

    def test_power(self):
        self.calc.add(2)
        self.assertEqual(self.calc.power(3), 8)

    def test_square_root(self):
        self.calc.add(9)
        self.assertEqual(self.calc.square_root(), 3)

    def test_sin(self):
        self.calc.add(90)
        self.calc.radians()
        self.assertAlmostEqual(self.calc.sin(), 1, places=5)

    def test_cos(self):
        self.calc.add(180)
        self.calc.radians()
        self.assertAlmostEqual(self.calc.cos(), -1, places=5)

    def test_tan(self):
        self.calc.add(45)
        self.calc.radians()
        self.assertAlmostEqual(self.calc.tan(), 1, places=5)

    def test_log(self):
        self.calc.add(100)
        self.assertAlmostEqual(self.calc.log(10), 2, places=5)

    def test_factorial(self):
        self.calc.add(5)
        self.assertEqual(self.calc.factorial(), 120)

    def test_radians(self):
        self.calc.add(180)
        self.assertAlmostEqual(self.calc.radians(), 3.141592653589793, places=5)

    def test_degrees(self):
        self.calc.add(3.141592653589793)
        self.assertAlmostEqual(self.calc.degrees(), 180, places=5)

    def test_invalid_square_root(self):
        self.calc.add(-9)
        with self.assertRaises(ValueError):
            self.calc.square_root()

    def test_invalid_log(self):
        self.calc.add(-1)
        with self.assertRaises(ValueError):
            self.calc.log()

    def test_invalid_factorial(self):
        self.calc.add(-5)
        with self.assertRaises(ValueError):
            self.calc.factorial()

if __name__ == '__main__':
    unittest.main()