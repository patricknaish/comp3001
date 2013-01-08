# Django magic
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context
from web import AuthManager
from web.TemplateWrapper import render_to_string

import lib

def render_home(request):
    context = Context()
    context["book_list"] = lib.USERBOOK.get_recent_listings()
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'home.html')
    response = HttpResponse()
    response.write(render_to_string(request, tmpl, context))
    return response
