import os
import sys

from src.calculator import Calculator

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <operation> <number>")
        return

    operation = sys.argv[1]

    if operation == "clear":
        os.environ["CALCULATOR_PREV_RESULT"] = "0"
        print("Previous result cleared.")
        return

    if len(sys.argv) < 3:
        print("Usage: python main.py <operation> <number>")
        return

    number = float(sys.argv[2])

    prev_result = float(os.environ.get("CALCULATOR_PREV_RESULT", 0))
    calc = Calculator(result=prev_result)

    if operation == "add":
        result = calc.add(number)
    elif operation == "subtract":
        result = calc.subtract(number)
    elif operation == "multiply":
        result = calc.multiply(number)
    elif operation == "divide":
        result = calc.divide(number)
    else:
        print("Invalid operation. Supported operations: add, subtract, multiply, divide, clear")
        return

    os.environ["CALCULATOR_PREV_RESULT"] = str(result)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()