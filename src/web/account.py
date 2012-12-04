import os
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.template import Context

def render_account(request):
    context = Context()
    response = HttpResponse()
    tmpl = os.path.join(os.path.dirname(__file__), 'template', 'account.html')
    response.write(render_to_string(tmpl, context))
    return response

def render_account_test(request):
    purchase_hist = [{"book": 
        {"image": "url",
        "title": "Title",
        "price": "10.00",
        "author": "Bob"}}]
    context = Context("purchase_history": purchase_hist)
    response = HttpResponse()
    tmpl = os.path.join(os.path.dirname(__file__), 'template', 'account.html')
    response.write(render_to_string(tmpl, context))
    return response