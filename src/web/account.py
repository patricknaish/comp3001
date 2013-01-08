import os
import cgi
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template import Context

import lib
from web import AuthManager
from web.TemplateWrapper import render_to_string

class PasswordDoesntMatchError(Exception):
    def __init__(self):
        Exception.__init__(self, "The provided passwords do not match.")

def render_account(request, message = None):
    if request.method == 'GET':
        if not AuthManager.is_logged_in(request):
            return redirect("/login")
        user = AuthManager.get_current_user(request)
        context = Context({ "message": message })
        response = HttpResponse()
        tmpl = os.path.join(os.path.dirname(__file__), 'template', 'account.html')
        response.write(render_to_string(request, tmpl, context))
        return response
    if request.method == 'POST': 
        if not AuthManager.is_logged_in(request):
            return redirect("/login")
        user = AuthManager.get_current_user(request)
        try :
            password = cgi.escape(request.POST['password'])
            password2 = cgi.escape(request.POST['password_confirm'])
            if password != password2:
                raise PasswordDoesntMatchError()
            lib.USER.change_password(user.email, password)
            message = "Successfully updated password."
            context = Context({ "user": user,
                                "message": message})
            response = HttpResponse()
            tmpl = os.path.join(os.path.dirname(__file__), 'template', 'account.html')
            response.write(render_to_string(tmpl, context))
            return response
        except PasswordDoesntMatchError as e:
            request.method = 'GET'
            return render_account(request, str(e))
    

def render_account_test(request):
    if not users.get_current_user():
        return redirect("/login") #TODO: Pass account as a return-to page
    purchase_hist = [
    {"book": 
        {"image": "url",
        "title": "Title",
        "price": "10.00",
        "author": "Bob"}},
    {"book": 
        {"image": "url",
        "title": "Another Title",
        "price": "15.00",
        "author": "Bill"}}
    ]
    
    seller_list = [
    {"book": 
        {"image": "url",
        "title": "Title",
        "price": "10.00",
        "author": "Bob"}},
    {"book": 
        {"image": "url",
        "title": "Another Title",
        "price": "15.00",
        "author": "Bill"}}
    ]
    try:
        user = lib.USER.get_by_key_name(request.session["user"])
    except:
        user = None
    context = Context({
                       "purchase_history": purchase_hist, 
                       "user": user
                       })
    response = HttpResponse()
    tmpl = os.path.join(os.path.dirname(__file__), 'template', 'account.html')
    response.write(render_to_string(tmpl, context))
    return response
