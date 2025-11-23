'''
    Name: {--Ashish Raj--}
    Date: {--23-11-2025--}
    Assignment Title: {--Python Object-Oriented Library Inventory System--}
'''


#  (Task 6) Implementation - main.py - Main program entry point and User Menu

from library import Library

def display_welcome():
    """Prints the welcome message."""
    # Task 1 Implementation:- Welcome Message

    print("\n==================================================================")
    print("        Welcome to Python Object-Oriented Library System          ")
    print("This system manages book inventory, members, and borrow/return operations.")
    print("==================================================================")

# Task 6 Implementation:- Interactive User Menu
def main():
    """Handles the main application loop."""
    
    # Library object Creation
    lib = Library()
    display_welcome()

    while True:
        print("\n--- LIBRARY MAIN MENU ---")
        print("1. Add New Book")
        print("2. Register New Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Library Report (Analytics)")
        print("6. View All Books and Members (Helper)")
        print("7. Exit") # Added a helper option

        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            # Task 3/6 logic: Add Book
            title = input("Enter Book Title: ").strip()
            author = input("Enter Author Name: ").strip()
            isbn = input("Enter ISBN (Unique ID): ").strip()
            if title and author and isbn:
                lib.add_book(title, author, isbn)
            else:
                print("❌ All fields are required.")
                
        elif choice == '2':
            # Task 3/6 logic: Register Member
            name = input("Enter Member Name: ").strip()
            member_id = input("Enter Member ID (Unique): ").strip()
            if name and member_id:
                lib.register_member(name, member_id)
            else:
                print("❌ All fields are required.")
                
        elif choice == '3':
            # Task 3/6 logic: Borrow Book
            member_id = input("Enter Member ID to borrow: ").strip()
            isbn = input("Enter ISBN of the book to borrow: ").strip()
            if member_id and isbn:
                lib.lend_book(member_id, isbn)
            else:
                print("❌ Member ID and ISBN are required.")
                
        elif choice == '4':
            # Task 3/6 logic: Return Book
            member_id = input("Enter Member ID returning: ").strip()
            isbn = input("Enter ISBN of the book being returned: ").strip()
            if member_id and isbn:
                lib.take_return(member_id, isbn)
            else:
                print("❌ Member ID and ISBN are required.")
                
        elif choice == '5':
            # Task 5 logic
            lib.display_report()
            
        elif choice == '6':
            # Helper to quickly check the data
            lib.list_all_books()
            lib.list_all_members()
            
        elif choice == '7':
            # Task 4: Save data before exit
            print("Exiting Library System. Saving data...")
            lib._save_data() 
            print("Data saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 7.")


if __name__ == '__main__':
    main()