
import sys
import click
from src.calculator import add, subtract, multiply, divide, power, square_root



def main_function(args=None):
    """Main CLI function to execute operations."""
    if args is None:
        args = sys.argv[1:]

    if len(args) < 3:
        click.echo("Usage: <operation> <num1> <num2>")
        sys.exit(1)

    operation = args[0].lower()
    try:
        num1 = float(args[1])
        num2 = float(args[2])
    except ValueError:
        click.echo("Both numbers must be valid numeric values.")
        sys.exit(1)

    try:
        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)
    except ZeroDivisionError:
        click.echo("Error: Division by zero is not allowed.")
        sys.exit(1)
    except Exception as e:
        click.echo(f"Error: {str(e)}")
        sys.exit(1)

    # Format output: remove .0 if integer
    if isinstance(result, float) and result.is_integer():
        result = int(result)
    elif operation == "divide":
        result = round(result, 2)

    click.echo(f"{result}")
    return result


if __name__ == "__main__":
    main_function()
