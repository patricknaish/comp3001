"""
Interim table between courses and modules
"""

from google.appengine.ext import db

from lib.Course import Course
from lib.Module import Module

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
