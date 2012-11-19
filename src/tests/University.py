"""
Module to test the University class
"""
# Unit test module
import unittest

import lib

class TestUniversity(unittest.TestCase):
    """
    Class that handles the testing of the University class
    """
    def setUp(self):
        "Prepare for running a test"
        self.university = lib.UNIVERSITY(0, "Test")

    def test_university_to_str(self):
        "Test the course's __str__ function"
        self.assertEqual(str(self.university), "Test")

    def test_university_add_course(self):
        "Test that adding a module only accepts a Module object"
        with self.assertRaises(TypeError):
            self.university.addCourse("Module String")

    def test_university_list_courses(self):
        "Test that the module list returns a list of modules"
        self.assertTrue(isinstance(self.university.getCourses(), list))
