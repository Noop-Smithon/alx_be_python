class Book:
    def __init__(self, title, author, year):
        # Initialize a Book Instance with the title, author and year of publication
        self.title = title
        self.author = author
        self.year = year

    def __del__(self): 
        # Destructur prints a message when a Book Instance is deleted
        print(f"Deleting {self.title}")

    def __str__(self):
        # Returns a string representation of the Book Instance in a certain format
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # Returns an official string representation that can recreate the Book Instance
        return f"Book('{self.title}', '{self.author}', {self.year})"
        