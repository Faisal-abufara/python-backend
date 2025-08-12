class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book.title}")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print(f"Books in {self.name}:")
        for book in self.books:
            print(book)

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f"You have borrowed '{book.title}'.")
                    return
                else:
                    print(f"Sorry, '{book.title}' is already borrowed.")
                    return
        print("Book not found.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f"You have returned '{book.title}'.")
                    return
                else:
                    print(f"'{book.title}' was not borrowed.")
                    return
        print("Book not found.")


# Example usage:

library = Library("City Library")

# Add some books
library.add_book(Book("Programing in C++", "Benjamin", "12345"))
library.add_book(Book("Programming in java", "Gosling", "67890"))

library.display_books()

# Borrow and return
library.borrow_book("12345")
library.borrow_book("12345")  # Trying to borrow again

library.return_book("12345")
library.return_book("12345")  # Trying to return again

library.display_books()
