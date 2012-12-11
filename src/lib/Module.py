from google.appengine.ext import db

from lib.Book import Book

class Module(db.Model):
    """
    Defines the module schema
    """
    shortTitle = db.StringProperty()
    title = db.StringProperty()

    @staticmethod
    def create_module(module_short_title,
                      module_title):
        """
        Add a new module to the datastore
        """
        new_module = Module(key_name=module_short_title,
                            shortTitle=module_short_title,
                            title=module_title)
        new_module.put()

    @staticmethod
    def add_book(module_short_title,
                 book_isbn):
        """
        Link a module and a book
        """
        from lib.ModuleBook import ModuleBook
        module_ref = Module.get_by_key_name(module_short_title)
        book_ref = Book.get_by_key_name(book_isbn)
        new_module_book = ModuleBook(module=module_ref,
                                     book=book_ref)
        new_module_book.put()

    @staticmethod
    def remove_book(module_short_title,
                    book_isbn):
        module_ref = Module.get_by_key_name(module_short_title)
        book_ref = Book.get_by_key_name(book_isbn)
        module_book_ref = db.GqlQuery("SELECT * FROM ModuleBook WHERE " +\
                                      "module = :1 AND " +\
                                      "book = :2", 
                                      module_ref, 
                                      book_ref)
        db.delete(module_book_ref)
