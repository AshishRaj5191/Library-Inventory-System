# Task-1 Implementation book.py - Contains the definition for the Book class

class Book:
    """
    Represents a book in the library inventory.
    """
    def __init__(self, title, author, isbn):
        # Attributes
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True  # Default: Book is available

    def __str__(self):
        # String representation for easy printing
        availability = "Available" if self.available else "On Loan"
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {availability}"

    # Task 2: Method 1
    def borrow(self):
        # Marks the book as not available
        if self.available:
            self.available = False
            return True
        return False # Already borrowed

    # Task 2: Method 2
    def return_book(self):
        # Marks the book as available
        if not self.available:
            self.available = True
            return True
        return False # Already returned

# Helper method for saving/loading data (Task 4)
    def to_dict(self):
        """Returns book data as a dictionary for file saving."""
        return self.__dict__