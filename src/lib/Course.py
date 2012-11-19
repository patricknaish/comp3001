"""
Course module with class to represent a single course at a University
"""
class Course:
    """
    Class representing a course
    """
    def __init__(self, name):
        """
        Initialise a new course object with a given name
        """
        self.name = name
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
        self.module_list.append(module)
    
    def list_modules(self):
        """
        Return a list of the modules part of this course.
        """
        return '\n'.join(str(module) for module in self.module_list)
