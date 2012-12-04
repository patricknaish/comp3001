"""
Module containing classes for manipulating books
"""

from google.appengine.ext import db

class Book(db.Model):
    "Class representing a book in the book trading system"

    isbn = db.StringProperty()
    title = db.StringProperty()
    author = db.StringProperty()
    year = db.IntegerProperty()
    edition = db.StringProperty()
    publisher = db.StringProperty()
    rrp = db.IntegerProperty()
    picture = db.StringProperty()

    @staticmethod
    def create_book(book_isbn, 
                    book_title,
                    book_author,
                    book_year,
                    book_edition,
                    book_publisher,
                    book_rrp,
                    book_picture):
        """
        Add a new book to the datastore
        """
        new_book = Book(key_name=book_isbn,
                        isbn=book_isbn,
                        title=book_title,
                        author=book_author,
                        year=book_year,
                        edition=book_edition,
                        publisher=book_publisher,
                        rrp=book_rrp,
                        picture=book_picture)
        new_book.put()
