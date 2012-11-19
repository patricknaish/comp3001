# Unit test module
import unittest

import lib

class TestCourse(unittest.TestCase):

	# Prepare for running a test
	def setUp(self):
		self.course = lib.Course("Test Course")

	# Test the course name
	def test_CourseToStr(self):
		self.assertEqual(str(self.course), "Test Course")

	# Test that adding a module only accepts a Module object
	def test_CourseAddModule(self):
		with self.assertRaises(TypeError):
			self.course.addModule("Module String")

	# Test that the module list returns a list of modules
	def test_CourseListModules(self):
		self.assertTrue(isinstance(self.course.getModules(), list))
