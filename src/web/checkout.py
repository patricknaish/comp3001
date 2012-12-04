# Django magic
import os
from django.http import HttpResponse
from django.template import Context, loader


def render_basket(request):
    context = Context()
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'checkout.html')
    response = HttpResponse()
    response.write(loader.render_to_string(tmpl, context))
    return response
