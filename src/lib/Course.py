"""
Course module with class to represent a single course at a University
"""
from google.appengine.ext import db

from lib.Module import Module

class Course(db.Model):
    """
    Defines the course schema
    """
    name = db.StringProperty()

    @staticmethod
    def create_course(course_name):
        """
        Add a new course to the datastore
        """
        new_course = Course(key_name=course_name,
                            name=course_name)
        new_course.put()

    @staticmethod
    def add_module(course_name,
                   module_short_title):
        """
        Link a course and a module
        """
        from lib.CourseModule import CourseModule
        course_ref = Course.get_by_key_name(course_name)
        module_ref = Module.get_by_key_name(module_short_title)
        new_course_module = CourseModule(course=course_ref,
                                         module=module_ref)
        new_course_module.put()

    @staticmethod
    def remove_module(course_name,
                      module_short_title):  
        course_ref = Course.get_by_key_name(course_name)
        module_ref = Module.get_by_key_name(module_short_title)
        course_module_ref = db.GqlQuery("SELECT * FROM CourseModule WHERE " +\
                                        "course = :1 AND " +\
                                        "module = :2", 
                                        course_ref, 
                                        module_ref)
        db.delete(course_module_ref)

