from typing import Union, Optional

Number = Union[int, float]

class Calculator:
    """
    A calculator class that provides basic and advanced mathematical operations.
    All methods include type hints and docstrings for better code clarity.
    """
    
    def __init__(self):
        """Initialize the calculator."""
        self._last_result: Optional[Number] = None
    
    @property
    def last_result(self) -> Optional[Number]:
        """Return the last calculation result."""
        return self._last_result
    
    def add(self, a: Number, b: Number) -> Number:
        """
        Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of the two numbers
        """
        self._last_result = a + b
        return self._last_result
    
    def subtract(self, a: Number, b: Number) -> Number:
        """
        Subtract second number from first number.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Difference between the two numbers
        """
        self._last_result = a - b
        return self._last_result
    
    def multiply(self, a: Number, b: Number) -> Number:
        """
        Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Product of the two numbers
        """
        self._last_result = a * b
        return self._last_result
    
    def divide(self, a: Number, b: Number) -> float:
        """
        Divide first number by second number.
        
        Args:
            a: First number (dividend)
            b: Second number (divisor)
            
        Returns:
            Quotient of the division
            
        Raises:
            ZeroDivisionError: If the divisor is zero
        """
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        self._last_result = a / b
        return self._last_result
    
    def power(self, base: Number, exponent: Number) -> Number:
        """
        Raise a number to the power of another.
        
        Args:
            base: The base number
            exponent: The exponent
            
        Returns:
            The result of base raised to the exponent
        """
        self._last_result = base ** exponent
        return self._last_result
    
    def square_root(self, number: Number) -> float:
        """
        Calculate the square root of a number.
        
        Args:
            number: The number to find the square root of
            
        Returns:
            The square root of the number
            
        Raises:
            ValueError: If the input is negative
        """
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        self._last_result = number ** 0.5
        return self._last_result 