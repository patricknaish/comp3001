"""
Interim table between users and books
"""

from google.appengine.ext import db

from lib.User import User
from lib.Book import Book

import time
import logging

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
    sold_stamp = db.IntegerProperty()
    sold_to_user = db.StringProperty()

    @staticmethod
    def get_recent_listings():
        "Gets all listings created in the last 24 hours"
        books = []
        book_ref = UserBook.gql("WHERE listed_stamp > %d" % (time.time() - 86400, ))
        for book in book_ref.run():
            if not book.sold_to_user:
                books.append(book)
        return books

    def mark_as_sold(self, user):
        self.sold_to_user = user.email
        self.sold_stamp = int(time.time())
        self.put()
