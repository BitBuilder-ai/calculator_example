import math

from src.calculator import Calculator

class ScientificCalculator(Calculator):
    def __init__(self):
        super().__init__()

    def power(self, num):
        self.result = math.pow(self.result, num)
        return self.result

    def square_root(self):
        if self.result < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        self.result = math.sqrt(self.result)
        return self.result

    def sin(self):
        self.result = math.sin(self.result)
        return self.result

    def cos(self):
        self.result = math.cos(self.result)
        return self.result

    def tan(self):
        self.result = math.tan(self.result)
        return self.result

    def log(self, base=math.e):
        if self.result <= 0:
            raise ValueError("Cannot calculate logarithm of a non-positive number")
        self.result = math.log(self.result, base)
        return self.result

    def factorial(self):
        if self.result < 0:
            raise ValueError("Cannot calculate factorial of a negative number")
        self.result = math.factorial(self.result)
        return self.result

    def radians(self):
        self.result = math.radians(self.result)
        return self.result

    def degrees(self):
        self.result = math.degrees(self.result)
        return self.result
