# Task-1 Implementation member.py - Contains the definition for the Member class

class Member:
    """
    Represents a registered member of the library.
    """
    def __init__(self, name, member_id):
        # Attributes
        self.name = name
        self.member_id = member_id
        # borrowed_books will store a list of ISBNs
        self.borrowed_books = [] 

    def __str__(self):
        # String representation for easy printing
        return f"Member: {self.name} (ID: {self.member_id}), Books Borrowed: {len(self.borrowed_books)}"

    # Task 2: Method 1 - Requires Book Object as Argument
    def borrow_book(self, book):
        """Adds book's ISBN to the member's borrowed_books list."""
        # Check if the book object has an ISBN and is not already borrowed
        if book.isbn not in self.borrowed_books: # <-- Accessing book.isbn for data
            self.borrowed_books.append(book.isbn)
            return True
        return False

    # Task 2: Method 2 - Requires Book Object as Argument
    def return_book(self, book):
        """Removes book's ISBN from the member's borrowed_books list."""
        if book.isbn in self.borrowed_books: # <-- Accessing book.isbn for data
            self.borrowed_books.remove(book.isbn)
            return True
        return False

    # Task 2: Method 3
    def list_books(self):
        """Prints the ISBNs of all books currently borrowed by the member."""
        if self.borrowed_books:
            print(f"--- Books borrowed by {self.name} ---")
            for isbn in self.borrowed_books:
                print(f"  - ISBN: {isbn}")
        else:
            print(f"{self.name} has no books currently borrowed.")

# Helper method for saving/loading data (Task 4)
    def to_dict(self):
        """Returns member data as a dictionary for file saving."""
        return self.__dict__