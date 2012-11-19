# Unit test module
import unittest

import lib

class TestUniversity(unittest.TestCase):

	# Prepare for running a test
	def setUp(self):
		self.university = lib.University(0, "Test")

	# Test the course name
	def test_UniversityToStr(self):
		self.assertEqual(str(self.course), "Test")

	# Test that adding a module only accepts a Module object
	def test_UniversityAddCourse(self):
		with self.assertRaises(TypeError):
			self.course.addCourse("Module String")

	# Test that the module list returns a list of modules
	def test_UniversityListCourses(self):
		self.assertTrue(isinstance(self.course.getCourses(), list))
