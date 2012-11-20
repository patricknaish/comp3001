"""
Test class for datastore interactions
"""
import webapp2
import cgi

from google.appengine.ext import db

class Book(db.Model):
    """
    Defines the book schema
    """
    isbn = db.StringProperty()
    title = db.StringProperty()
    author = db.StringProperty()
    year = db.IntegerProperty()
    edition = db.StringProperty()
    publisher = db.StringProperty()
    rrp = db.IntegerProperty()

class User(db.Model):
    """
    Defines the user schema
    """
    email = db.EmailProperty()
    firstName = db.StringProperty()
    lastName = db.StringProperty()
    currentYear = db.IntegerProperty()
    reputation = db.IntegerProperty()

class Module(db.Model):
    """
    Defines the module schema
    """
    shortTitle = db.StringProperty()
    title = db.StringProperty()

class Course(db.Model):
    """
    Defines the course schema
    """
    name = db.StringProperty()

class University(db.Model):
    """
    Defines the university schema
    """
    name = db.StringProperty()

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
    condition = db.IntegerProperty()

class UserCourse(db.Model):
    """
    Defines the user-course schema
    """
    user = db.ReferenceProperty(User, 
                                required=True, 
                                collection_name = 'courses')
    course = db.ReferenceProperty(Course, 
                                  required=True, 
                                  collection_name = 'users')

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

class CourseModule(db.Model):
    """
    Defines the course-module schema
    """
    course = db.ReferenceProperty(Course, 
                                  required=True, 
                                  collection_name = 'modules')
    module = db.ReferenceProperty(Module, 
                                  required=True, 
                                  collection_name = 'courses')

class UniversityCourse(db.Model):
    """
    Defines the university-course schema
    """
    university = db.ReferenceProperty(University, 
                                      required=True, 
                                      collection_name = 'courses')
    course = db.ReferenceProperty(Course, 
                                  required=True, 
                                  collection_name = 'universities')

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

def create_book(book_isbn, 
                book_title,
                book_author,
                book_year,
                book_edition,
                book_publisher,
                book_rrp):
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
                    rrp=book_rrp)
    new_book.put()

def create_module(module_short_title,
                  module_title):
    """
    Add a new module to the datastore
    """
    new_module = Module(key_name=module_short_title,
                        shortTitle=module_short_title,
                        title=module_title)
    new_module.put()

def create_course(course_name):
    """
    Add a new course to the datastore
    """
    new_course = Course(key_name=course_name,
                        name=course_name)
    new_course.put()

def create_university(university_name):
    """
    Add a new university to the datastore
    """
    new_university = University(key_name=university_name,
                                name=university_name)
    new_university.put()

def create_user_book_copy(user_email, 
                          book_isbn, 
                          book_price, 
                          book_condition):
    """
    Link a user and a book
    """
    user_ref = User.get_by_key_name(user_email)
    book_ref = Book.get_by_key_name(book_isbn)
    user_book = UserBook(user=user_ref,
                         book=book_ref,
                         price=book_price,
                         condition=book_condition)
    user_book.put()

def create_user_course_registration(user_email,
                                    course_name):
    """
    Link a user and a course
    """
    user_ref = User.get_by_key_name(user_email)
    course_ref = Course.get_by_key_name(course_name)
    user_course = UserCourse(user=user_ref,
                             course=course_ref)
    user_course.put()

def create_module_book_assignation(module_short_title,
                                   book_isbn):
    """
    Link a module and a book
    """
    module_ref = Module.get_by_key_name(module_short_title)
    book_ref = Book.get_by_key_name(book_isbn)
    module_book = ModuleBook(module=module_ref,
                             book=book_ref)
    module_book.put()

def create_course_module_assignation(course_name,
                                     module_short_title):
    """
    Link a course and a module
    """
    course_ref = Course.get_by_key_name(course_name)
    module_ref = Module.get_by_key_name(module_short_title)
    course_module = CourseModule(course=course_ref,
                                 module=module_ref)
    course_module.put()

def create_university_course_assignation(university_name,
                                         course_name):
    """
    Link a university and a course
    """
    university_ref = University.get_by_key_name(university_name)
    course_ref = Course.get_by_key_name(course_name)
    university_course = UniversityCourse(university=university_ref,
                                         course=course_ref)
    university_course.put()

class MainPage(webapp2.RequestHandler) :
    """
    Page rendering
    """
    def get(self):
        """
        Handle GET requests
        """
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello')
        """create_user('patrick@pmnaish.co.uk',
                     'Patrick',
                     'Naish',
                     3)
        create_book('978-1840915013',
                    'Harumi\'s Japanese Cooking',
                    'Harumi Kurihara',
                    2008,
                    '1',
                    'Conran Octopus Ltd',
                    1499)
        create_user_book_copy('patrick@pmnaish.co.uk',
                              '978-1840915013',
                              1166,
                              5)"""

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
