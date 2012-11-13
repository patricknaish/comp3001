#!/usr/bin/python

class University:
	courseList = []
	
	def __init__(self, id, name):
		self.id = id
		self.name = name
		
	def addCourse(self, course):
		self.courseList.append(course)

	def __str__(self):
		return name
