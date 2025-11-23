# Task-3 Implementation library.py - Contains the Library Management Logic

# Imports classes
from book import Book
from member import Member
import json
import os
import datetime

class Library:
    """
    Manages the collection of books and registered members.
    """
    # File paths for persistence (Task 4)
    BOOK_FILE = 'books.json'
    MEMBER_FILE = 'members.json'
    
    # -------------------------------------------------------------
    # --- Initialization and Persistence (Task 4 Setup) ---
    # -------------------------------------------------------------
    
    def __init__(self):
        # Attributes (Task 3: Maintains lists of books and members)
        # self.books = {ISBN: Book_object}
        self.books = {}     
        # self.members = {Member ID: Member_object}
        self.members = {}   
        
        # Task 4: Load existing data from files on startup 
        self._load_data() 
        
    def _save_data(self):
        """Task 4: Saves current state of books and members to JSON files."""
        # Convert objects to dictionary format before saving
        book_data = {isbn: book.to_dict() for isbn, book in self.books.items()}
        member_data = {member_id: member.to_dict() for member_id, member in self.members.items()}
        
        try:
            with open(self.BOOK_FILE, 'w') as f:
                json.dump(book_data, f, indent=4)
            with open(self.MEMBER_FILE, 'w') as f:
                json.dump(member_data, f, indent=4)
            print("\n✅ Data successfully saved.")
        except IOError:
            print("❌ Error: Could not save data to files.")

    def _load_data(self):
        """Task 4: Loads data from JSON files on startup."""
        print("ℹ️ Loading data on startup...")
        try:
            # Load Books
            with open(self.BOOK_FILE, 'r') as f:
                book_data = json.load(f)
                for isbn, data in book_data.items():
                    # Recreate Book objects from dictionary data
                    book = Book(data['title'], data['author'], data['isbn'])
                    book.available = data['available']
                    self.books[isbn] = book
            
            # Load Members
            with open(self.MEMBER_FILE, 'r') as f:
                member_data = json.load(f)
                for member_id, data in member_data.items():
                    # Recreate Member objects
                    member = Member(data['name'], data['member_id'])
                    member.borrowed_books = data['borrowed_books'] # Borrowed ISBNs load here
                    self.members[member_id] = member
            
            print(f"☑️ Loaded {len(self.books)} books and {len(self.members)} members.")
            
        except FileNotFoundError:
            print("⚠️ Warning: Data files not found. Starting with empty inventory.")
        except json.JSONDecodeError:
            print("❌ Error: Corrupted data files. Starting with empty inventory.")
        except Exception as e:
            print(f"❌ An unexpected error occurred during loading: {e}")

    # -------------------------------------------------------------
    # --- Task 3: Library Management Logic ---
    # -------------------------------------------------------------
    
    def add_book(self, title, author, isbn):
        """Adds a new book object to the library's collection."""
        if isbn in self.books:
            print(f"❌ Error: Book with ISBN {isbn} already exists.")
            return False
            
        new_book = Book(title, author, isbn)
        self.books[isbn] = new_book
        self._save_data() # Save data immediately after adding
        print(f"✅ Book '{title}' added successfully.")
        return True

    def register_member(self, name, member_id):
        """Registers a new member object."""
        if member_id in self.members:
            print(f"❌ Error: Member with ID {member_id} already registered.")
            return False
            
        new_member = Member(name, member_id)
        self.members[member_id] = new_member
        self._save_data() # Save data immediately after registering
        print(f"✅ Member '{name}' registered successfully with ID {member_id}.")
        return True
    
    def _is_valid_transaction(self, member_id, isbn):
        """Checks if both member and book exist."""
        if isbn not in self.books:
            print(f"❌ Error: Book with ISBN {isbn} not found.")
            return None, None
        if member_id not in self.members:
            print(f"❌ Error: Member with ID {member_id} not found.")
            return None, None
        return self.members[member_id], self.books[isbn]

    def lend_book(self, member_id, isbn):
        """Handles the borrowing process."""
        member, book = self._is_valid_transaction(member_id, isbn)
        if not member:
            return False

        if not book.available:
            print(f"❌ Error: Book '{book.title}' is currently unavailable (already on loan).")
            return False

        # 1. Mark the Book object as borrowed
        book.borrow() 
        # 2. Mark the Member object as having borrowed the book
        member.borrow_book(book)

        self._save_data() # Save changes
        print(f"✅ Success: Member {member_id} borrowed '{book.title}'.")
        return True

    def take_return(self, member_id, isbn):
        """Handles the book return process."""
        member, book = self._is_valid_transaction(member_id, isbn)
        if not member:
            return False
            
        if book.available:
            print(f"❌ Error: Book '{book.title}' was never checked out.")
            return False

        if book.isbn not in member.borrowed_books:
            print(f"❌ Error: Book '{book.title}' was not borrowed by member {member_id}.")
            return False
            
        # 1. Mark the Book object as returned
        book.return_book()
        # 2. Remove the book from Member's borrowed list
        member.return_book(book)
        
        self._save_data() # Save changes
        print(f"✅ Success: Member {member_id} returned '{book.title}'.")
        return True

    # -------------------------------------------------------------
    # --- Task 5: Analytics Report Implementation ---
    # -------------------------------------------------------------
    def display_report(self):
        """
        Task 5: Displays class-level analytics (Total books, borrowed books, members).
        """
        total_books = len(self.books)
        total_members = len(self.members)
        
        # Calculate currently borrowed books by checking the 'available' attribute
        borrowed_count = 0
        for book in self.books.values():
            if not book.available:
                borrowed_count += 1
                
        available_count = total_books - borrowed_count
        
        print("\n==============================================")
        print("          LIBRARY ANALYTICS REPORT            ")
        print("==============================================")
        print(f"Total Books in Inventory: {total_books:<15}")
        print(f"Total Registered Members: {total_members:<15}")
        print("-" * 46)
        # Required Analytic: Number of books currently borrowed
        print(f"Books Currently Borrowed: {borrowed_count:<15}")
        print(f"Books Available for Loan: {available_count:<15}")
        print("==============================================")


    def list_all_books(self):
        """Prints details of all books in the library."""
        print("\n--- Current Library Inventory ---")
        if not self.books:
            print("ℹ️ No books in the inventory.")
            return
        
        for isbn, book in self.books.items():
            print(book)
            
    def list_all_members(self):
        """Prints details of all registered members."""
        print("\n--- Registered Members ---")
        if not self.members:
            print("ℹ️ No members registered.")
            return
        
        for member_id, member in self.members.items():
            print(member)
            member.list_books()
            print("-" * 20)




