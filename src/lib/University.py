import Course

class University:
	courseList = []
	
	def __init__(self, id, name):
		self.id = id
		self.name = name
		
	def addCourse(self, course):
		if not isinstance(course, Course):
			raise TypeError("course is not an instance of the Course object")
		self.courseList.append(course)

	def __str__(self):
		return name
