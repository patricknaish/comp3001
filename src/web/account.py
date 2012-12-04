import os
from django.http import HttpResponse
from djagno.template.loader import render_to_string
from django.template import Context

def render_account(request):
    context = Context()
    response = HttpResponse()
    tmpl = os.path.join(os.path.dirname(__file__), 'template', 'account.html')
    response.write(render_to_string(tmpl, context))
    return response