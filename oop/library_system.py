class Book:
    def __init__(self, title, author):
        # Initializes a Book Instance with the titl and aauthor
        self.title = title
        self.author = author

    def __str__(self):
        # Returns a string representation of the Book instance
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        # Initializes an EBook instance with the given title, author, and file size.
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        # Returns a string representation of the EBook instance.
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # Initializes a PrintBook instance with the given title, author, and page count.
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        # Returns a string representation of the PrintBook instance.
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        # Initializes a Library instance with an empty list of books.
        self.books = []

    def add_book(self, book):
        # Adds a book (Book, EBook, or PrintBook) to the library.
        self.books.append(book)

    def list_books(self):
        # Prints details of each book in the library.
        for book in self.books:
            print(book)