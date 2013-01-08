# Django magic
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context

import AuthManager
import lib
from web.TemplateWrapper import render_to_string

def render_help(request):
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'help.html')
    response = HttpResponse()
    response.write(render_to_string(request, tmpl))
    return response
