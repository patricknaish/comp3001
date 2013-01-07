# Django magic
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader

from lib import BOOK

def render_book(request, book_id):
    copies = BOOK.list_book_copies(book_id)
    context = Context()
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'book.html')
    response = HttpResponse()
    response.write(loader.render_to_string(tmpl, context))
    return response
