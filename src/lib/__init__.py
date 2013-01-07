"""
Root of the libraries behind the web UI for the book trader system.

All classes that are the same name as their modules are brought into the global
namespace
"""
import lib.Course as Course
import lib.Paypal as Paypal
import lib.University as University
import lib.User as User
import lib.UserBook as UserBook
import lib.Book as Book
import lib.Module as Module
import lib.Session as Session
import logging
# Now make the classes available readily
logging.info("dir(lib.Paypal) = %s" % dir(Paypal))
Paypal = Paypal.Paypal
COURSE = Course.Course
UNIVERSITY = University.University
USER = User.User
BOOK = Book.Book
MODULE = Module.Module
USERBOOK = UserBook.UserBook
SESSION = Session.Session
