import Course

class University:
    
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.course_list = list()
        
    def addCourse(self, course):
        if not isinstance(course, Course):
            raise TypeError("course is not an instance of the Course object")
        self.course_list.append(course)

    def __str__(self):
        return self.name
