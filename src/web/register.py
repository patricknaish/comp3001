import os
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.template import Context
from google.appengine.api import mail
import cgi

# User functions
import lib

class EmailDoesntMatchError(Exception):
    def __init__(self):
        Exception.__init__(self, "The provided email addresses do not match.")

def render_register(request):
    if request.method == 'GET':
        return render_register_form(request)

    if request.method == 'POST':
        return render_register_action(request)

def render_register_action(request):
    try:
        email = cgi.escape(request.POST['email'])
        email2 = cgi.escape(request.POST['email2'])
        firstname = cgi.escape(request.POST['firstname'])
        lastname = cgi.escape(request.POST['lastname'])
        year = int(cgi.escape(request.POST['year']))
        # Check their email addresses match
        if email != email2:
            raise EmailDoesntMatchError()

        # Do the creation
        lib.USER.create_user(email, firstname, lastname, year)
        new_password = USER.reset_password(email)

        # Send the success email
        context = Context({
            "firstname": firstname,
            "lastname" : lastname,
            "email": email,
            "password": new_password
        })
        tmpl = os.path.join(os.path.dirname(__file__), 'template', 'registersuccess.eml')
        message = mail.EmailMessage(sender = "TexTrader Support <support@comp3001.net.cmalton.me.uk>", 
            subject = "TexTrader: Your account details")
        message.to = "%s %s <%s>" % (firstname, lastname, email)
        message.body = render_to_string(tmpl, context)
        message.send()

        tmpl = os.path.join(os.path.dirname(__file__), 'template', 'registersuccess.html')
        context = Context()
        response = HttpResponse()
        response.write(render_to_string(tmpl, context))
        return response

    except EmailDoesntMatchError as e:
        return render_register_form(request, str(e))

def render_register_form(request, error = None):
    tmpl = os.path.join(os.path.dirname(__file__), 'template', 'registerform.html')
    context = Context({"error": error})
    response = HttpResponse()
    response.write(render_to_string(tmpl, context))
    return response

def render_forgot_password(request):
    if request.method == 'GET':
        return render_forgotpw_form(request)

    if request.method == 'POST':
        return render_forgotpw_action(request)

def render_forgotpw_action(request):
    try:
        email = cgi.escape(request.POST['email'])
        lastname = cgi.escape(request.POST['lastname'])
        # Check their email addresses match
        user = lib.USER.get_by_key_name(email)
        if user == None:
             raise InvalidUserError()

        if user.lastName != lastname:
#            raise InvalidUserDataError()
             return None

        # Do the creation
        new_password = USER.reset_password(email)

        # Send the success email
        context = Context({
            "firstname": user.firstName,
            "lastname" : user.lastName,
            "email": email,
            "password": new_password
        })
        tmpl = os.path.join(os.path.dirname(__file__), 'template', 'forgotpw.eml')
        message = mail.EmailMessage(sender = "TexTrader Support <support@comp3001.net.cmalton.me.uk>", 
            subject = "TexTrader: Password reset")
        message.to = "%s %s <%s>" % (user.firstName, user.lastName, user.email)
        message.body = render_to_string(tmpl, context)
        message.send()

        tmpl = os.path.join(os.path.dirname(__file__), 'template', 'pwresetsuccess.html')
        context = Context()
        response = HttpResponse()
        response.write(render_to_string(tmpl, context))
        return response

    except EmailDoesntMatchError as e:
        return render_register_form(request, str(e))

def render_forgotpw_form(request, error = None):
    tmpl = os.path.join(os.path.dirname(__file__), 'template', 'pwreset.html')
    context = Context({"error": error})
    response = HttpResponse()
    response.write(render_to_string(tmpl, context))
    return response
