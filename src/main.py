import webapp2
from lib import USER
import cgi

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Yo")

class Registration(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("""
            <html>
                <body>
                    <h1>Registration</h1><br />
                    <form action="/register" method="post">
                        <div>First name: <input type="text" name="firstname"</div>
                        <div>Last name:  <input type="text" name="lastname"</div>
                        <div>Email:      <input type="text" name="email"</div>
                        <div>Year of study: <input type="radio" name="year" value="1">1<br />
                                            <input type="radio" name="year" value="2">2<br />
                                            <input type="radio" name="year" value="3">3<br />
                                            <input type="radio" name="year" value="4">4<br />
                                            <input type="radio" name="year" value="5">5<br />
                                            <input type="radio" name="year" value="6">Postgrad<br />
                        </div>
                        <div><input type="submit" value="Register"></div>
                    </form>
                </body>
            </html>""")

    def post(self):
        firstname = cgi.escape(self.request.get('firstname'))
        lastname = cgi.escape(self.request.get('lastname'))
        email = cgi.escape(self.request.get('email'))
        year = int(cgi.escape(self.request.get('year'))) 
        self.response.out.write("""
            <html>
                <body>
                    <h1>Registration</h1><br />
                    Registering user {first} {last} with email {mail} in year {yy} of study
                </body>
            </html>""".format(first=firstname, last=lastname, mail=email, yy=year))
        USER.create_user(email, firstname, lastname, year)

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/register', Registration)])
