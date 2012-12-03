"""
Test class for datastore interactions
"""
import webapp2
import cgi

from lib import USER

from google.appengine.ext import db

def create_university_course_assignation(university_name,
                                         course_name):
    """
    Link a university and a course
    """
    university_ref = University.get_by_key_name(university_name)
    course_ref = Course.get_by_key_name(course_name)
    university_course = UniversityCourse(university=university_ref,
                                         course=course_ref)
    university_course.put()

class MainPage(webapp2.RequestHandler) :
    """
    Page rendering
    """
    def get(self):
        """
        Handle GET requests
        """
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello')
        #USER.create_user("alan@test.com", "Alan", "Jones", 2)
        #USER.add_book("alan@test.com", "978-1840915013", 1499, 3)
        #USER.remove_book("alan@test.com", "978-1840915013", 1499, 3)

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
