"""
Interim table between modules and books
"""

from google.appengine.ext import db

from lib.Module import Module
from lib.Book import Book

class ModuleBook(db.Model):
    """
    Defines the module-book schema
    """
    module = db.ReferenceProperty(Module, 
                                  required=True, 
                                  collection_name = 'books')
    book = db.ReferenceProperty(Book, 
                                required=True, 
                                collection_name = 'modules')
