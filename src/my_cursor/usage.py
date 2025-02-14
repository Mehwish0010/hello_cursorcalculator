from my_cursor.calculator import Calculator

def interactive_calculator() -> None:
    """
    Interactive calculator with simple operation flow.
    """
    calc = Calculator()
    print("Welcome to Calculator!")
    
    operations = {
        '1': ('+', 'Addition'),
        '2': ('-', 'Subtraction'),
        '3': ('*', 'Multiplication'),
        '4': ('/', 'Division'),
        '5': ('^', 'Power'),
        '6': ('sqrt', 'Square Root'),
        'q': ('q', 'Quit')
    }
    
    while True:
        # Display menu
        print("\nAvailable operations:")
        for key, (symbol, name) in operations.items():
            print(f"  {key}. {name} ({symbol})")
        
        choice = input("\nSelect operation (or 'q' to quit): ").strip().lower()
        
        if choice == 'q':
            print("Goodbye!")
            break
            
        if choice not in operations:
            print("Invalid choice! Please select a valid operation.")
            continue
            
        operation = operations[choice][0]
            
        try:
            if operation == 'sqrt':
                num = float(input("Enter number: "))
                result = calc.square_root(num)
                print(f"√{num} = {result}")
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if operation == '+':
                    result = calc.add(num1, num2)
                elif operation == '-':
                    result = calc.subtract(num1, num2)
                elif operation == '*':
                    result = calc.multiply(num1, num2)
                elif operation == '/':
                    result = calc.divide(num1, num2)
                elif operation == '^':
                    result = calc.power(num1, num2)
                    
                print(f"{num1} {operation} {num2} = {result}")
            
            print(f"\nYour answer is: {result}")
            
            continue_calc = input("\nDo you want to continue? (y/n): ").strip().lower()
            if continue_calc != 'y':
                print("Goodbye!")
                break
                
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")

def main() -> None:
    """
    Main function to run the interactive calculator.
    """
    interactive_calculator()

if __name__ == "__main__":
    main() 