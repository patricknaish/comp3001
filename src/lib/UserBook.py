"""
Interim table between users and books
"""

from google.appengine.ext import db

from lib.User import User
from lib.Book import Book

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
