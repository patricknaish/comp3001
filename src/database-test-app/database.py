import webapp2
import cgi

from google.appengine.ext import db

class Book(db.Model):
    isbn = db.StringProperty()
    title = db.StringProperty()
    author = db.StringProperty()
    year = db.IntegerProperty()
    edition = db.StringProperty()
    publisher = db.StringProperty()
    rrp = db.IntegerProperty()

class User(db.Model):
    email = db.EmailProperty()
    firstName = db.StringProperty()
    lastName = db.StringProperty()
    currentYear = db.IntegerProperty()
    reputation = db.IntegerProperty()

class Module(db.Model):
    shortTitle = db.StringProperty()
    title = db.StringProperty()

class Course(db.Model):
    name = db.StringProperty()

class University(db.Model):
    name = db.StringProperty()

class UserBook(db.Model):
    user = db.ReferenceProperty(User, 
                                required=True, 
                                collection_name = 'books')
    book = db.ReferenceProperty(Book, 
                                required=True, 
                                collection_name = 'users')
    price = db.IntegerProperty()
    condition = db.IntegerProperty()

class UserCourse(db.Model):
    user = db.ReferenceProperty(User, 
                                required=True, 
                                collection_name = 'courses')
    course = db.ReferenceProperty(Course, 
                                  required=True, 
                                  collection_name = 'users')

class ModuleBook(db.Model):
    module = db.ReferenceProperty(Module, 
                                  required=True, 
                                  collection_name = 'books')
    book = db.ReferenceProperty(Book, 
                                required=True, 
                                collection_name = 'modules')

class CourseModule(db.Model):
    course = db.ReferenceProperty(Course, 
                                  required=True, 
                                  collection_name = 'modules')
    module = db.ReferenceProperty(Module, 
                                  required=True, 
                                  collection_name = 'courses')

class UniversityCourses(db.Model):
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
    new_book = Book(key_name=book_isbn,
                    isbn=book_isbn,
                    title=book_title,
                    author=book_author,
                    year=book_year,
                    edition=book_edition,
                    publisher=book_publisher,
                    rrp=book_rrp)
    new_book.put()

def create_user_book_copy(user_email, 
                          book_isbn, 
                          book_price, 
                          book_condition):
    user_ref = User.get_by_key_name(user_email)
    book_ref = Book.get_by_key_name(book_isbn)
    user_book = UserBook(user=user_ref,
                         book=book_ref,
                         price=book_price,
                         condition=book_condition)
    user_book.put()

class MainPage(webapp2.RequestHandler) :
    def get(self):
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