# Project Summary: Object-Oriented Library Inventory System

1. Introduction and Core Foundation

This project is a Python application built upon Object-Oriented Programming (OOP) principles. Its primary goal is to create an efficient, automated inventory management system for a library, eliminating the confusion and delays associated with manual record-keeping. The system's stability relies on Modular Design and robust Data Persistence.

2. Modular Design and OOP Architecture

The project is divided across four key Python files, showcasing modular design and the application of OOP concepts:

book.py & member.py: Define the core real-world objects (Book and Member) along with their attributes (e.g., isbn, available, borrowed_books) and behavior (e.g., borrow(), return_book()).

library.py: Defines the Library Class, which acts as the central management logic, storing and coordinating all Book and Member objects.

main.py: Serves as the program's entry point, hosting the interactive User Menu.

3. Core Functionalities

Management Operations (CRUD): The system handles adding new books and registering new members. Crucially, it manages the exchange process using lend_book() and take_return() methods, updating the status of both the book and the member simultaneously.

Data Persistence (Task 4): All object data is permanently stored in books.json and members.json files using the built-in json library, ensuring data integrity across program sessions.

Error Handling: Implemented try-except blocks are used to handle file-related issues, such as missing files (FileNotFoundError) or corrupted data (JSONDecodeError), allowing the system to start safely.

Class-Level Analytics (Task 5): A quick Library Report displays important operational statistics, including the Total number of books currently borrowed and the total number of books available for loan.

User Interface (Bonus): An interactive command-line menu allows users to easily execute all functions from a single interface.

4. Python Concepts Used

The project demonstrates proficiency in: OOP (Classes, Objects, Methods), Modularity (File imports), File I/O (JSON serialization/deserialization), and Exception Handling.