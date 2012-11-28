# Django magic
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context

def render_home(request):
    context = Context()
    response = HttpResponse();
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'pagebase.html')
    response.write(render(request, tmpl, context))
    return response
