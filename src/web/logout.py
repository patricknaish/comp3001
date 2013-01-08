"""
This module handles being logged in and out of the TexTreader website
"""
import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import Context, loader
from web import AuthManager

def render_logout(request):
    """
    Handler for requests to /logout
    """
    if AuthManager.is_logged_in(request):
        AuthManager.set_logged_out(request)
        context = Context()
        tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'logout.html')
        response = HttpResponse()
        response.write(loader.render_to_string(tmpl, context))
        return response
