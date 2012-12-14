"""
Interim table between universities and courses
"""

from google.appengine.ext import db

from lib.University import University
from lib.Course import Course

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
