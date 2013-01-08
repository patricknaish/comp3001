import os
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template import Context
from web.TemplateWrapper import render_to_string

def page_not_found(request):
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', '404.html')
    response = HttpResponse()
    response.write(render_to_string(request, tmpl))
    return response

def server_error(request):
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', '500.html')
    response = HttpResponse()
    response.write(render_to_string(request, tmpl))
    return response

def permission_denied(request):
    # If they are logged in, show access denied, else login form
    if "user" in request.session.keys():
        return redirect("django.views.defaults.permission_denied")
    else:
        return redirect("/login?from=%s" % request.path)

