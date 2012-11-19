"""
Module to test the Course class.
"""
import unittest

import lib

class TestCourse(unittest.TestCase):

    def setUp(self):
        "Prepare for running a test"
        self.course = lib.COURSE("Test Course")

    def test_course_to_str(self):
        "Test the course name"
        self.assertEqual(str(self.course), "Test Course")

    def test_course_add_module(self):
        "Test that adding a module only accepts a module object"
        with self.assertRaises(TypeError):
            self.course.addModule("Module String")

    def test_course_list_modules(self):
        "Test that the module list returns a list of modules"
        self.assertTrue(isinstance(self.course.getModules(), list))
