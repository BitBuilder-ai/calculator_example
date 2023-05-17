class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def subtract(self, num):
        self.result -= num
        return self.result

    def multiply(self, num):
        self.result *= num
        return self.result

    def divide(self, num):
        if num == 0:
            raise ValueError("Cannot divide by zero")
        self.result /= num
        return self.result

    def reset(self):
        self.result = 0
        return self.result
