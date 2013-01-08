# Django magic
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader

import AuthManager
import lib

def render_help(request):
    context = Context({"user": AuthManager.get_current_user(request)})
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'help.html')
    response = HttpResponse()
    response.write(loader.render_to_string(tmpl, context))
    return response
