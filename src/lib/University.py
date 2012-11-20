from lib import Course

class University:
    
    def __init__(self, university_id, name):
        self.university_id = university_id
        self.name = name
        self.course_list = list()
        
    def add_course(self, course):
        if not isinstance(course, Course):
            raise TypeError("course is not an instance of the Course object")
        self.course_list.append(course)

    def __str__(self):
        return self.name
