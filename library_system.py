

# Import necessary libraries for typing and date management
from typing import List

# Book class to represent each book in the library
class Book:
    def __init__(self, title, author, genre, year):
        # Encapsulated book attributes
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__year = year
        self.is_borrowed = False  # Track borrowing status

    # Method to display book details
    def get_details(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.__title} by {self.__author} ({self.__genre}, {self.__year}) - {status}"

    # Check if book matches a keyword (used in search)
    def matches(self, keyword):
        return keyword.lower() in self.__title.lower()

    # Borrow the book if it's not already borrowed
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    # Return the book if it's currently borrowed
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False

# EBook class inherits from Book and adds file size
class EBook(Book):
    def __init__(self, title, author, genre, year, file_size):
        super().__init__(title, author, genre, year)
        self.file_size = file_size

    # Override get_details to include file size
    def get_details(self):
        base_details = super().get_details()
        return f"{base_details} [E-Book: {self.file_size}MB]"

# Member class to store user details
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

    def __str__(self):
        return f"Member {self.member_id}: {self.name}"

# Library class manages all books and members
class Library:
    def __init__(self):
        self.books = []      # List to store Book objects
        self.members = []    # List to store Member objects
        self.next_member_id = 1  # To auto-assign IDs

    # Add a new book to the library
    def add_book(self, book):
        self.books.append(book)

    # Display all books
    def list_books(self):
        for book in self.books:
            print(book.get_details())

    # Search for a book by keyword
    def search_books(self, keyword):
        found = False
        for book in self.books:
            if book.matches(keyword):
                print(book.get_details())
                found = True
        if not found:
            print("No matching books found.")

    # Delete a book from the list
    def delete_book(self, keyword):
        for i, book in enumerate(self.books):
            if book.matches(keyword):
                del self.books[i]
                print("Book deleted.")
                return
        print("Book not found.")

    # Register a new member
    def register_member(self, name):
        member = Member(name, self.next_member_id)
        self.members.append(member)
        self.next_member_id += 1
        print(f"Registered: {member}")

    # List all registered members
    def list_members(self):
        for member in self.members:
            print(member)

    # Borrow a book
    def borrow_book(self, keyword):
        for book in self.books:
            if book.matches(keyword):
                if book.borrow():
                    print("Book borrowed.")
                else:
                    print("Book already borrowed.")
                return
        print("Book not found.")

    # Return a borrowed book
    def return_book(self, keyword):
        for book in self.books:
            if book.matches(keyword):
                if book.return_book():
                    print("Book returned.")
                else:
                    print("Book wasn't borrowed.")
                return
        print("Book not found.")

# Example interaction using a simple menu
if __name__ == "__main__":
    lib = Library()
    lib.add_book(Book("The Power of Faith", "John Maxwell", "Spiritual", 2019))
    lib.add_book(EBook("AI for Beginners", "Sam Tech", "Technology", 2023, 2.5))
    lib.register_member("Blossom Dopamu")

    # Command-line interface loop
    while True:
        print("\n1. Add Book\n2. List Books\n3. Search Book\n4. Delete Book\n5. Register Member\n6. List Members\n7. Borrow Book\n8. Return Book\n9. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            genre = input("Genre: ")
            year = int(input("Year: "))
            lib.add_book(Book(title, author, genre, year))

        elif choice == "2":
            lib.list_books()

        elif choice == "3":
            keyword = input("Enter keyword to search: ")
            lib.search_books(keyword)

        elif choice == "4":
            keyword = input("Enter book title to delete: ")
            lib.delete_book(keyword)

        elif choice == "5":
            name = input("Enter member name: ")
            lib.register_member(name)

        elif choice == "6":
            lib.list_members()

        elif choice == "7":
            keyword = input("Enter book title to borrow: ")
            lib.borrow_book(keyword)

        elif choice == "8":
            keyword = input("Enter book title to return: ")
            lib.return_book(keyword)

        elif choice == "9":
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")
