import os
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.template import Context
import AuthManager

def page_not_found(request):
    context = Context({"user": AuthManager.get_current_user(request)})
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', '500.html')
    response = HttpResponse()
    response.write(render_to_string(tmpl, context))
    return response

def server_error(request):
    context = Context({"user": AuthManager.get_current_user(request)})
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', '500.html')
    response = HttpResponse()
    response.write(render_to_string(tmpl, context))
    return response

def permission_denied(request):
    # If they are logged in, show access denied, else login form
    if "user" in request.session.keys():
        return redirect("django.views.defaults.permission_denied")
    else:
        return redirect("/login?from=%s" % request.path)

