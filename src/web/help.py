# Django magic
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader

from lib import User

def render_help(request):
    context = Context({"user": User.get_by_key_name(request.session["user"])})
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'help.html')
    response = HttpResponse()
    response.write(loader.render_to_string(tmpl, context))
    return response
