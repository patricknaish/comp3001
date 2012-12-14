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
        """
        Remove a module from a course
        """
        course_ref = Course.get_by_key_name(course_name)
        module_ref = Module.get_by_key_name(module_short_title)
        course_module_ref = db.GqlQuery("SELECT * FROM CourseModule WHERE " +\
                                        "course = :1 AND " +\
                                        "module = :2", 
                                        course_ref, 
                                        module_ref)
        db.delete(course_module_ref)

    @staticmethod
    def list_modules(course_name):
        """
        List all modules associated with a course
        """
        modules = []
        course_ref = Course.get_by_key_name(course_name)
        course_module_ref = db.GqlQuery("SELECT * FROM CourseModule WHERE " +\
                                        "course = :1",                                      
                                        course_ref)
        for module_ref in course_module_ref.run():
            module_key = CourseModule.module.get_value_for_datastore(module_ref)
            module_res = Module.get(module_key)
            modules.append(module_res)
        return modules
