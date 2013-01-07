"""
Interim table between users and books
"""

from google.appengine.ext import db

from lib.User import User
from lib.Book import Book

import time

class UserBook(db.Model):
    """
    Defines the user-book schema
    """
    user = db.ReferenceProperty(User, 
                                required=True, 
                                collection_name = 'books')
    book = db.ReferenceProperty(Book, 
                                required=True, 
                                collection_name = 'users')
    price = db.IntegerProperty()
    condition = db.StringProperty()
    listed_stamp = db.IntegerProperty()

    @staticmethod
    def get_recent_listings():
        "Gets all listings created in the last 24 hours"
        books = []
        book_ref = db.GqlQuery("SELECT * FROM UserBook WHERE listed_stamp > :1",
             time.time() - 86400)
        for book in book_ref.run():
            books.append(book)
        return books

