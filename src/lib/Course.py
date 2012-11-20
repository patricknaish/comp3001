from lib import Module

"""
Course module with class to represent a single course at a University
"""
class Course:
    """
    Class representing a course
    """
    def __init__(self, course_id, name):
        """
        Initialise a new course object with a given name
        """
        self.name = name
        self.course_id = course_id
        self.module_list = list()
    
    def __str__(self):
        """
        Return the module's name as its string representation
        """
        return self.name

    def add_module(self, module):
        """
        Add a module to this course.
        """
        if not isinstance(module, Module):
            raise TypeError("module is not an instance of the Module object")
        self.module_list.append(module)
    
    def get_modules(self):
        """
        Return a list of the modules part of this course.
        """
        return self.module_list
