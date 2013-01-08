"""
This module handles being logged in and out of the TexTreader website
"""
import os
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import Context
import lib
from web import AuthManager
from web.TemplateWrapper import render_to_string

def render_login(request):
    """
    Handler for requests to /login
    """
    if AuthManager.is_logged_in(request):
        return redirect("web.account.render_account")
    if request.method == "POST":
        return render_login_action(request)
    else:
        return render_login_form(request)

def render_login_action(request):
    """
    Handle the login form submission
    """
    if not request.method == "POST" or \
       not "email" in request.POST.keys() or \
       not "password" in request.POST.keys():
        return render_login_form(request, "The form was not correctly sent to the web server. Please try again.")
    if request.POST["email"] == "":
        return render_login_form(request, "Email address is a required field")
    if request.POST["password"] == "":
        return render_login_form(request, "Password is a required field")
    if lib.USER.authenticate(request.POST["email"], request.POST["password"]):
        AuthManager.set_logged_in(request, request.POST["email"])
        if "from" in request.POST.keys():
            return redirect(request.POST["from"])
        else:
            return redirect("web.account.render_account")
    else:
        return render_login_form(request, "Invalid username or password")

def render_login_form(request, error = None):
    """
    Handle display of the login page
    """
    origin = None
    if "from" in request.GET.keys():
        origin = request.GET["from"]
    if "from" in request.POST.keys():
        origin = request.POST["from"]
    context = Context({"origin": origin, "error": error})
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'login.html')
    response = HttpResponse()
    response.write(render_to_string(request, tmpl, context))
    return response
