from google.appengine.ext import db

from lib.Book import Book

class User(db.Model):

    email = db.EmailProperty()
    firstName = db.StringProperty()
    lastName = db.StringProperty()
    currentYear = db.IntegerProperty()
    reputation = db.IntegerProperty()

    @staticmethod
    def create_user(user_email,
                    user_first_name, 
                    user_last_name, 
                    user_current_year):
        """
        Add a new user to the datastore
        """
        new_user = User(key_name=user_email,
                        email=user_email,
                        firstName=user_first_name,
                        lastName=user_last_name,
                        currentYear=user_current_year,
                        reputation=0)
        new_user.put()

    @staticmethod
    def increase_reputation(user_email):
        user_ref = User.get_by_key_name(user_email)
        user_ref.reputation += 1
        user_ref.put()

    @staticmethod
    def decrease_reputation(user_email):
        user_ref = User.get_by_key_name(user_email)
        user_ref.reputation -= 1
        user_ref.put()

    @staticmethod
    def add_book(user_email,
                book_isbn, 
                book_price, 
                book_condition):
        from lib.UserBook import UserBook
        user_ref = User.get_by_key_name(user_email)
        book_ref = Book.get_by_key_name(book_isbn)
        new_user_book = UserBook(user=user_ref,
                                 book=book_ref,
                                 price=book_price,
                                 condition=book_condition)
        new_user_book.put()

    @staticmethod
    def remove_book(user_email,
                   book_isbn, 
                   book_price, 
                   book_condition):
        user_ref = User.get_by_key_name(user_email)
        book_ref = Book.get_by_key_name(book_isbn)
        user_book_ref = db.GqlQuery("SELECT * FROM UserBook WHERE " +\
                                    "user = :1 AND " +\
                                    "book = :2 AND " +\
                                    "price = :3 AND " +\
                                    "condition = :4", 
                                    user_ref, 
                                    book_ref, 
                                    book_price, 
                                    book_condition)
        db.delete(user_book_ref)
