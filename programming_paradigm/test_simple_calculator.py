class SimpleCalculator:
    """
    A simple calculator class that provides basic arithmetic operations.
    
    This class implements addition, subtraction, multiplication, and division
    operations with proper error handling for division by zero.
    """
    
    def add(self, a, b):
        """
        Add two numbers.
        
        Args:
            a (float/int): First number
            b (float/int): Second number
            
        Returns:
            float/int: Sum of a and b
        """
        return a + b
    
    def subtract(self, a, b):
        """
        Subtract second number from first number.
        
        Args:
            a (float/int): First number (minuend)
            b (float/int): Second number (subtrahend)
            
        Returns:
            float/int: Difference of a and b
        """
        return a - b
    
    def multiply(self, a, b):
        """
        Multiply two numbers.
        
        Args:
            a (float/int): First number
            b (float/int): Second number
            
        Returns:
            float/int: Product of a and b
        """
        return a * b
    
    def divide(self, a, b):
        """
        Divide first number by second number.
        
        Args:
            a (float/int): Dividend
            b (float/int): Divisor
            
        Returns:
            float: Quotient of a divided by b
            
        Raises:
            ValueError: If b is zero (division by zero)
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


# Example usage (optional - for testing the class directly)
if __name__ == "__main__":
    calc = SimpleCalculator()
    
    # Test basic operations
    print("Testing SimpleCalculator:")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")
    
    # Test division by zero
    try:
        result = calc.divide(10, 0)
    except ValueError as e:
        print(f"Division by zero error: {e}")