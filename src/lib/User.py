"""
Module containing methods for manuipulating users
"""

import random
import hashlib
import uuid

from google.appengine.ext import db

from lib.Book import Book
from lib.Course import Course

class User(db.Model):
    """
    Defines the user schema
    """
    email = db.EmailProperty()
    password = db.StringProperty()
    salt = db.StringProperty()
    firstName = db.StringProperty()
    lastName = db.StringProperty()
    currentYear = db.IntegerProperty()
    reputation = db.IntegerProperty()
    password = db.StringProperty()

    @staticmethod
    def create_user(user_email,
                    user_first_name,
                    user_last_name,
                    user_current_year):
        """
        Add a new user to the datastore
        """
        salt = uuid.uuid4().hex
        new_user = User(key_name=user_email,
                        email=user_email,
                        salt=salt,
                        firstName=user_first_name,
                        lastName=user_last_name,
                        currentYear=user_current_year,
                        reputation=0,
                        password="")
        new_user.put()

    @staticmethod
    def reset_password(user_email):
        password = User.create_password()
        user_ref = User.get_by_key_name(user_email)
        user_ref.password = User.hash_password(password, user_ref.salt)
        user_ref.put()
        return password

    @staticmethod
    def authenticate(user_email,
                     user_password):
        """
        Authenticate a user with the hashed password
        """
        user_ref = User.get_by_key_name(user_email)
        salt = user_ref.salt
        hash_pwd = User.hash_password(user_password, salt)
        if hash_pwd == user_ref.password:
            return true
        else:
            return false

    @staticmethod
    def increase_reputation(user_email):
        """
        Increment a user's reputation by 1
        """
        user_ref = User.get_by_key_name(user_email)
        user_ref.reputation += 1
        user_ref.put()

    @staticmethod
    def decrease_reputation(user_email):
        """
        Decrement a user's reputation by 1
        """
        user_ref = User.get_by_key_name(user_email)
        user_ref.reputation -= 1
        user_ref.put()

    @staticmethod
    def reset_reputation(user_email):
        """
        Set a user's reputation back to 0
        """
        user_ref = User.get_by_key_name(user_email)
        user_ref.reputation = 0
        user_ref.put()

    @staticmethod
    def add_book(user_email,
                 book_isbn, 
                 book_price, 
                 book_condition):
        """
        Add a book to the datastore
        """
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
        """
        Remove a book from the datastore
        """
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

    @staticmethod
    def add_course(user_email,
                   course_name):
        """
        Link a user and a course
        """
        from lib.UserCourse import UserCourse
        user_ref = User.get_by_key_name(user_email)
        course_ref = Course.get_by_key_name(course_name)
        new_user_course = UserCourse(user=user_ref,
                                     course=course_ref)
        new_user_course.put()

    @staticmethod
    def remove_course(user_email,
                      course_name):
        """
        Unlink a user and a course
        """
        user_ref = User.get_by_key_name(user_email)
        course_ref = Course.get_by_key_name(course_name)
        user_course_ref = db.GqlQuery("SELECT * FROM UserCourse WHERE " +\
                                      "user = :1 AND " +\
                                      "course = :2",
                                      user_ref,
                                      course_ref)
        db.delete(user_course_ref)

    @staticmethod
    def hash_password(user_password, salt):
        return hashlib.sha512(user_password + salt).hexdigest()

    @staticmethod
    def create_password():
        DICTIONARY = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#~@-_+="
        newPW = ""
        for x in range(8):
            newPW += random.choice(DICTIONARY)
        return newPW

    @staticmethod
    def list_books(user_email):
        """
        List all books associated with a user
        """
        books = []
        user_ref = User.get_by_key_name(user_email)
        user_book_ref = db.GqlQuery("SELECT * FROM UserBook WHERE " +\
                                    "user = :1",                                      
                                    user_ref)
        for book_ref in user_book_ref.run():
            book_key = UserBook.book.get_value_for_datastore(book_ref)
            book_res = Book.get(Book_key)
            books.append(book_res)
        return books

    @staticmethod
    def list_courses(user_email):
        """
        List all courses associated with a user
        """
        courses = []
        user_ref = User.get_by_key_name(user_email)
        user_course_ref = db.GqlQuery("SELECT * FROM UserCourse WHERE " +\
                                      "user = :1",                                      
                                      user_ref)
        for course_ref in user_course_ref.run():
            course_key = UserCourse.course.get_value_for_datastore(course_ref)
            course_res = Course.get(Course_key)
            courses.append(course_res)
        return courses

