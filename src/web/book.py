# Django magic
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
import lib

def render_book(request, listing_id):
    listing_id = int(listing_id)
    listing = lib.USERBOOK.get_by_id(listing_id)
    book = listing.book
    seller = listing.user
    copies = lib.BOOK.list_book_copies(book.isbn)
    context = Context({
                       "seller":seller,
                       "current_book":listing,
                       "same_books":copies, 
                       "user": AuthManager.get_current_user(request))
                       })
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'book.html')
    response = HttpResponse()
    response.write(loader.render_to_string(tmpl, context))
    return response
