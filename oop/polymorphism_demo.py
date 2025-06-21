import math

class Shape:
    """
    Base class representing a geometric shape.
    
    This class serves as an abstract base class that defines
    the interface for calculating area, which must be implemented
    by derived classes.
    """
    
    def area(self):
        """
        Calculate the area of the shape.
        
        This method raises NotImplementedError to indicate that
        derived classes must override this method.
        
        Raises:
            NotImplementedError: This method must be overridden by subclasses
        """
        raise NotImplementedError("Subclasses must override area() method")


class Rectangle(Shape):
    """
    Derived class representing a rectangle.
    
    Attributes:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    """
    
    def __init__(self, length, width):
        """
        Initialize a Rectangle instance.
        
        Args:
            length (float): The length of the rectangle
            width (float): The width of the rectangle
        """
        self.length = length
        self.width = width
    
    def area(self):
        """
        Calculate the area of the rectangle.
        
        Returns:
            float: The area of the rectangle (length × width)
        """
        return self.length * self.width


class Circle(Shape):
    """
    Derived class representing a circle.
    
    Attributes:
        radius (float): The radius of the circle
    """
    
    def __init__(self, radius):
        """
        Initialize a Circle instance.
        
        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """
        Calculate the area of the circle.
        
        Returns:
            float: The area of the circle (π × radius²)
        """
        return math.pi * self.radius ** 2