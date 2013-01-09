"""
This module handles being logged in and out of the TexTreader website
"""
import os
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import Context
from web import AuthManager
from web.TemplateWrapper import render_to_string

def render_logout(request):
    """
    Handler for requests to /logout
    """
    if AuthManager.is_logged_in(request):
        AuthManager.set_logged_out(request)
        tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'logout.html')
        response = HttpResponse()
        response.write(render_to_string(request, tmpl))
        return response
    else:
        return redirect("/login")
