# Django magic
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader

from lib import Book
from lib import User

def render_book(request, book_id):
    copies = Book.list_book_copies(book_id)
    context = Context({
                       "same_books":copies, 
                       "user": User.get_by_key_name(request.session["user"])
                       })
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'book.html')
    response = HttpResponse()
    response.write(loader.render_to_string(tmpl, context))
    return response
