import os
from django.http import HttpResponse
from django.templace import Context, loader

def render_create_book(request):
    context = Context()
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'create_book.html')
    response = HttpResponse()
    response.write(loader.render_to_string(tmpl, context))
    return response