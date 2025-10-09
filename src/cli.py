import sys
from calculator import add, subtract, multiply, divide, power, square_root


def main():
    """Command-line interface for calculator operations."""
    if len(sys.argv) < 2:
        print("Usage: python -m src.cli <operation> <num1> <num2>")
        sys.exit(1)

    operation = sys.argv[1]
    try:
        if operation in {"add", "subtract", "multiply", "divide", "power"}:
            if len(sys.argv) < 4:
                print(f"Error: {operation} requires two operands.")
                sys.exit(1)
            num1 = float(sys.argv[2])
            num2 = float(sys.argv[3])

            if operation == "add":
                result = add(num1, num2)
            elif operation == "subtract":
                result = subtract(num1, num2)
            elif operation == "multiply":
                result = multiply(num1, num2)
            elif operation == "divide":
                result = divide(num1, num2)
            else:  # power
                result = power(num1, num2)

        elif operation == "sqrt":
            if len(sys.argv) < 3:
                print("Error: sqrt requires one operand.")
                sys.exit(1)
            num = float(sys.argv[2])
            result = square_root(num)

        else:
            print(f"Unknown operation: {operation}")
            sys.exit(1)

        print(result)

    except ValueError:
        print("Invalid input. Please provide numeric values.")
        sys.exit(1)
    except ZeroDivisionError:
        print("Error: Division by zero.")
        sys.exit(1)


if __name__ == "__main__":
    main()
