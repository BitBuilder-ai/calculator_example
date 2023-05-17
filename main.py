import sys

from src.scientific_calculator import ScientificCalculator

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <operation> <number>")
        return

    operation = sys.argv[1]
    number = float(sys.argv[2])

    calc = ScientificCalculator()

    if operation == "add":
        result = calc.add(number)
    elif operation == "subtract":
        result = calc.subtract(number)
    elif operation == "multiply":
        result = calc.multiply(number)
    elif operation == "divide":
        result = calc.divide(number)
    elif operation == "power":
        result = calc.power(number)
    elif operation == "square_root":
        result = calc.square_root()
    elif operation == "sin":
        result = calc.sin()
    elif operation == "cos":
        result = calc.cos()
    elif operation == "tan":
        result = calc.tan()
    elif operation == "log":
        result = calc.log()
    elif operation == "factorial":
        result = calc.factorial()
    elif operation == "radians":
        result = calc.radians()
    elif operation == "degrees":
        result = calc.degrees()
    else:
        print("Invalid operation. Supported operations: add, subtract, multiply, divide, power, square_root, sin, cos, tan, log, factorial, radians, degrees")
        return

    print(f"Result: {result}")

if __name__ == "__main__":
    main()