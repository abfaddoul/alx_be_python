class Book:
    """
    A Book class that demonstrates Python magic methods.
    
    Attributes:
        title (str): The title of the book
        author (str): The author of the book
        year (int): The publication year of the book
    """
    
    def __init__(self, title, author, year):
        """
        Constructor method to initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """
        Destructor method that prints a message when the object is deleted.
        """
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """
        String representation method for user-friendly output.
        
        Returns:
            str: A formatted string representation of the book
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """
        Official representation method that shows how to recreate the object.
        
        Returns:
            str: A string that would recreate the Book instance
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
