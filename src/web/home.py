# Django magic
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from web import AuthManager

import lib

def render_home(request):
	if AuthManager.is_logged_in:
    	context = Context({"user": AuthManager.get_current_user})
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'home.html')
    response = HttpResponse()
    response.write(loader.render_to_string(tmpl, context))
    return response
