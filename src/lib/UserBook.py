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

    @staticmethod
    def get_recent_listings():
        "Gets all listings created in the last 24 hours"
        books = []
        book_ref = UserBook.gql("WHERE listed_stamp > %d" % (time.time() - 86400, ))
        logging.info("Running GQL for get_recent_listings")
        for book in book_ref.run():
            logging.info(book)
            books.append(book)
        return books

