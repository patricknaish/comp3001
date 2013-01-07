"""
Module containing methods for manipulating books
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

    @staticmethod
    def list_all_books():
        """
        List all books in the datastore
        """
        books = []
        book_ref = db.GqlQuery("SELECT * FROM Book")
        for book in book_ref.run():
            books.append(book)
        return books

    @staticmethod
    def list_book_copies(book_isbn):
        """
        Get all the copies of a book
        """
        from lib.UserBook import UserBook
        books = []
        book_ref = Book.get_by_key_name(book_isbn)
        if book_ref == None:
            return None
        user_book_ref = db.GqlQuery("SELECT * FROM UserBook WHERE " +\
                                    "book = :1",                                      
                                    book_ref)
        for book_ref in user_book_ref.run():
            book_key = UserBook.book.get_value_for_datastore(book_ref)
            book_res = Book.get(Book_key)
            books.append(book_res)
        return books

    def as_dict(self):
        return { 
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "edition": self.edition,
            "publisher": self.publisher,
            "rrp": self.rrp,
            "picture": self.picture
           }
