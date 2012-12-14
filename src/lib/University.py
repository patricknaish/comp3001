"""
Module containing methods for manipulating universities
"""

from google.appengine.ext import db

from lib.Course import Course

class University(db.Model):
    """
    Defines the university schema
    """
    name = db.StringProperty()

    @staticmethod
    def create_university(university_name):
        """
        Add a new university to the datastore
        """
        new_university = University(key_name=university_name,
                                    name=university_name)
        new_university.put()

    @staticmethod
    def add_course(university_name,
                   course_name):
        """
        Link a university and a course
        """
        from lib.UniversityCourse import UniversityCourse
        university_ref = University.get_by_key_name(university_name)
        course_ref = Course.get_by_key_name(course_name)
        new_university_course = UniversityCourse(university=university_ref,
                                                 course=course_ref)
        new_university_course.put()

    @staticmethod
    def remove_course(university_name,
                      course_name):
        """
        Unlink a university and a course
        """
        university_ref = University.get_by_key_name(university_name)
        course_ref = Course.get_by_key_name(course_name)
        uni_course_ref = db.GqlQuery("SELECT * FROM UniversityCourse WHERE " +\
                                     "university = :1 AND " +\
                                     "course = :2", 
                                     university_ref, 
                                     course_ref)
        db.delete(uni_course_ref)      

    @staticmethod
    def list_all_universities():
        """
        List all universities in the datastore
        """
        universities = []
        university_ref = db.GqlQuery("SELECT * FROM University")
        for book in book_ref.run()

    @staticmethod
    def list_courses(university_name):
        """
        List all courses associated with a university
        """
        courses = []
        university_ref = University.get_by_key_name(university_name)
        university_course_ref = db.GqlQuery("SELECT * FROM UniversityCourse WHERE " +\
                                            "university = :1",                                      
                                            university_ref)
        for course_ref in university_course_ref.run():
            course_key = UniversityCourse.course.get_value_for_datastore(course_ref)
            course_res = Course.get(course_key)
            courses.append(course_res)
        return courses
