import os
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.template import Context

def render_register(request):
    if request.method == 'GET':
        tmpl = os.path.join(os.path.dirname(__file__), 'template', 'registerform.html')
        
    if request.method == 'POST':
        tmpl = os.path.join(os.path.dirname(__file__), 'template', 'registerpost.html')     

    context = Context()
    response = HttpResponse()
    
    response.write(render_to_string(tmpl, context))
    return response