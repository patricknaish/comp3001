# Django magic
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
import lib

def render_book(request, listing_id):
    listing = lib.USERBOOK.get_by_key_name(listing_id)
    book = listing.book
    seller = listing.user
    copies = lib.BOOK.list_book_copies(book.isbn)
    context = Context({
                       "seller":seller,
                       "current_book":book,
                       "same_books":copies, 
                       "user": lib.USER.get_by_key_name(request.session["user"])
                       })
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'book.html')
    response = HttpResponse()
    response.write(loader.render_to_string(tmpl, context))
    return response
