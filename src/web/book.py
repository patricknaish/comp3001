# Django magic
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
import lib

def render_book(request, book_id):
    copies = lib.BOOK.list_book_copies(book_id)
    try:
        user = lib.USER.get_by_key_name(request.session["user"]),
    except:
        user = None
    context = Context({
                       "same_books":copies, 
                       "user": user
                       })
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'book.html')
    response = HttpResponse()
    response.write(loader.render_to_string(tmpl, context))
    return response
