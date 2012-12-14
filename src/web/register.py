import os
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.template import Context
import cgi

def render_register(request):
    if request.method == 'GET':
        return render_register_form(request)
        
    if request.method == 'POST':
        return render_register_post(request)  

def render_register_form(request):
    tmpl = os.path.join(os.path.dirname(__file__), 'template', 'registerform.html')
    
    context = Context()
    response = HttpResponse()
    
    response.write(render_to_string(tmpl, context))
    return response

def render_register_post(request):
    tmpl = os.path.join(os.path.dirname(__file__), 'template', 'requestpost.html')
    
    context = Context() #TODO: fill with request details
    response = HttpResponse()
    
    response.write(render_to_string(tmpl, context))
    return response