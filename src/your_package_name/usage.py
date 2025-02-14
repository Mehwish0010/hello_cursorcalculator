from your_package_name.calculator import Calculator

def basic_usage_example() -> None:
    """
    Demonstrates basic usage of the Calculator class.
    """
    # Create a calculator instance
    calc = Calculator()
    
    # Basic operations
    result = calc.add(5, 3)
    print(f"5 + 3 = {result}")  # Output: 5 + 3 = 8
    
    result = calc.subtract(10, 4)
    print(f"10 - 4 = {result}")  # Output: 10 - 4 = 6
    
    result = calc.multiply(6, 7)
    print(f"6 * 7 = {result}")  # Output: 6 * 7 = 42
    
    result = calc.divide(15, 3)
    print(f"15 / 3 = {result}")  # Output: 15 / 3 = 5.0

def advanced_usage_example() -> None:
    """
    Demonstrates advanced features of the Calculator class.
    """
    calc = Calculator()
    
    # Power and square root operations
    result = calc.power(2, 3)
    print(f"2^3 = {result}")  # Output: 2^3 = 8
    
    result = calc.square_root(16)
    print(f"√16 = {result}")  # Output: √16 = 4.0
    
    # Using last_result property
    calc.add(10, 5)
    print(f"Previous result: {calc.last_result}")  # Output: Previous result: 15
    
    # Chain calculations using last_result
    calc.multiply(calc.last_result, 2)
    print(f"Previous result * 2: {calc.last_result}")  # Output: Previous result * 2: 30

def error_handling_example() -> None:
    """
    Demonstrates error handling in the Calculator class.
    """
    calc = Calculator()
    
    try:
        calc.divide(10, 0)
    except ZeroDivisionError as e:
        print(f"Error: {e}")  # Output: Error: Division by zero is not allowed
    
    try:
        calc.square_root(-4)
    except ValueError as e:
        print(f"Error: {e}")  # Output: Error: Cannot calculate square root of negative number

def main() -> None:
    """
    Main function to run all examples.
    """
    print("Basic Calculator Usage:")
    print("-" * 20)
    basic_usage_example()
    
    print("\nAdvanced Calculator Usage:")
    print("-" * 20)
    advanced_usage_example()
    
    print("\nError Handling Examples:")
    print("-" * 20)
    error_handling_example()

if __name__ == "__main__":
    main() 