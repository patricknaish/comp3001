# Django magic
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader

def render_login(request, origin = None):
    context = Context({"from": origin})
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'login.html')
    response = HttpResponse()
    response.write(loader.render_to_string(tmpl, context))
    return response
