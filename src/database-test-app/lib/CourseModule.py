from google.appengine.ext import db

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
