"""
Test class for datastore interactions
"""
import webapp2
import cgi

from lib import USER

from google.appengine.ext import db

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
