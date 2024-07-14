class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False


class Library:

    """Library class with a private list _books to store instances of Book"""

    def __init__(self):
        self._books = []

    # Method to add books
    def add_book(self, book):
        self._books.append(book)

    # Method to checkout book(s)
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out: {book.title} by {book.author}")
                else:
                    print(f"{book.title} is already checked out.")
                return
        print(f"Book not found: {title}")

    # Method to return book(s)
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned: {book.title} by {book.author}")
                else:
                    print(f"{book.title} is already available.")
                return
        print(f"Book not found: {title}")

    # Method to list book(s) available in the Library
    def list_available_books(self):
        if not self._books:
            print("No books available.")
        else:
            print("Available books:")
            for book in self._books:
                if not book._is_checked_out:
                    print(f"{book.title} by {book.author}")