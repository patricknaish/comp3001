"""
Module containing classes for manipulating books
"""

class Book:
    "Class representing a book in the book trading system"

    def __init__(self, id, isbn, title, author, year, edition, publisher, rrp):
        "Create a new book with the specified parameters"
        self.id = id
		self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.edition = edition
        self.publisher = publisher
        self.rrp = rrp

    def __str__(self):
        "Convert a book to a string representation"
        return ", ".join( [self.title,
                            self.author,
                            self.year,
                            self.edition,
                            self.publisher,
                            self.isbn,
                            self.rrp
                            ])
