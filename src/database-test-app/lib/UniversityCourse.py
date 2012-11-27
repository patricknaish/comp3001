from google.appengine.ext import db

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
