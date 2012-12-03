from google.appengine.ext import db

from lib.User import User
from lib.Course import Course

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
