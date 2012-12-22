# Django magic
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from lib import USER
from web import AuthManager

def render_login(request):
    if request.method == "POST":
        return render_login_action(request)
    else:
        return render_login_form(request)

def render_login_action(request):
    if not request.method == "POST" or
       not "email" in request.POST.keys() or
       not "password" in request.POSTkeys():
        return render_login_form(request, "The form was not correctly sent to the web server. Please try again.")
    if request.POST["email"] == "":
        return render_login_form(request, "Email address is a required field")
    if request.POST["password"] == "":
        return render_login_form(request, "Password is a required field")
    if USER.authenticate(request.POST["email"], request.POST["password"]):
        AuthManager.set_logged_in(request, request.POST["email"])
        if "from" in request.POST.keys():
            return redirect(request.POST["from"])
        else:
            return redirect("web.account.render_account")
    else:
        return render_login_form(request, "Invalid username or password")

def render_login_form(request, error = None)
    origin = None
    if "from" in request.GET.keys():
        origin = request.GET["from"]
    if "from" in request.POST.keys():
        origin = request.POST["from"]
    context = Context({"origin": origin, "error": error})
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'login.html')
    response = HttpResponse()
    response.write(loader.render_to_string(tmpl, context))
    return response
