from google.appengine.ext import db

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
