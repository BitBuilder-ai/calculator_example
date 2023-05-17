import sys

from src.calculator import Calculator

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <operation> <number>")
        return

    operation = sys.argv[1]
    number = float(sys.argv[2])

    calc = Calculator()

    if operation == "add":
        result = calc.add(number)
    elif operation == "subtract":
        result = calc.subtract(number)
    elif operation == "multiply":
        result = calc.multiply(number)
    elif operation == "divide":
        result = calc.divide(number)
    else:
        print("Invalid operation. Supported operations: add, subtract, multiply, divide")
        return

    print(f"Result: {result}")

if __name__ == "__main__":
    main()