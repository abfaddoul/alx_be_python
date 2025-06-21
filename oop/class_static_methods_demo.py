class Calculator:
    """
    A Calculator class that demonstrates class methods and static methods.
    
    This class showcases the differences between @classmethod and @staticmethod
    decorators and their practical applications.
    """
    
    # Class attribute that can be accessed by class methods
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        
        Static methods don't receive any implicit first argument (self or cls).
        They behave like regular functions but are organized within the class.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        
        Class methods receive the class itself as the first argument (cls).
        They can access class attributes and other class methods.
        
        Args:
            cls: The class itself (automatically passed)
            a: First number
            b: Second number
            
        Returns:
            The product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
