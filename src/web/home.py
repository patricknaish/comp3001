# Django magic
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context

def render_home(request):
    context = Context()
    response = HttpResponse();
    tmpl =  '/home/cmalton/Documents/University/Part3/comp3001_cw2/src/web/template/pagebase.html'
    response.write(render(request, tmpl, context))
    return response
