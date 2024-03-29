"""
This module handles the actual books.
This includes rendering the individual book pages, adding new books etc.
"""

import os
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.template import Context, loader
from django.core.exceptions import PermissionDenied
from web import AuthManager
from web.TemplateWrapper import render_to_string
import cgi
import json
import lib
import time

def render_create_book(request):
    "Show the create book form"
    # Check permissions
    if not AuthManager.has_permission(request, 'create_book'):
        raise PermissionDenied

    # Handle the request if we're allowed to
    if request.method == 'POST':
        return create_book_action(request)
    else:
        user = AuthManager.get_current_user(request)
        context = Context({"user":user})
        tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'create_book.html')
        response = HttpResponse()
        response.write(render_to_string(request, tmpl, context))
        return response

def render_create_listing(request, error = None):
    "Show the create book form"
    # Check permissions
    if not AuthManager.has_permission(request, 'list_book'):
        raise PermissionDenied

    # Handle the request if we're allowed to
    if request.method == 'POST' and error is None:
        return list_book_action(request)
    else:
        user = AuthManager.get_current_user(request)
        context = Context({
                            "error": error,
                            "user": user,
                            "books": lib.BOOK.list_all_books()
                            })
        tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'list_book.html')
        response = HttpResponse()
        response.write(render_to_string(request, tmpl, context))
        return response

def list_book_action(request):
    # Are we using a template or a new book?
    if not "template_isbn" in request.POST.keys():
        # Create new book
        create_book_action(request)
        isbn = cgi.escape(request.POST["isbn"])
    elif request.POST["template_isbn"]:
        isbn = cgi.escape(request.POST["template_isbn"])
    else:
        return render_create_listing(request, "Please select a book from the drop-down or enter details for a new book.")
    book = lib.BOOK.get_by_key_name(isbn)
    user = AuthManager.get_current_user(request)
    condition = int(request.POST['condition'])
    #Convert condition from ints into the appropriate strings
    if condition == 1:
        condition = "New"
    if condition == 2:
        condition = "As New"
    if condition == 3:
        condition = "Used"
    if condition == 4:
        condition = "Damaged"
    price = float(cgi.escape(request.POST['price']))
    price = int(price * 100) #convert P.pp to interger pence


    try:
        lib.USERBOOK(key_name = None,
                     user = user,
                     book = book,
                     price = price,
                     condition = condition,
                     listed_stamp = int(time.time()),
                     sold_stamp = 0,
                     sold_to_user = None ).put()
        tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'list_book_success.html')
        context = Context()
    except Exception as e:
        context = Context({"error": e})
        tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'list_book_failure.html')
    response = HttpResponse()
    response.write(render_to_string(request, tmpl, context))
    return response

def create_book_action(request):
    isbn = cgi.escape(request.POST['isbn'])
    title = cgi.escape(request.POST['title'])
    author = cgi.escape(request.POST['author'])
    year = int(cgi.escape(request.POST['year']))
    edition = cgi.escape(request.POST['edition'])
    publisher = cgi.escape(request.POST['publisher'])
    rrp = float(cgi.escape(request.POST['rrp']))
    picture = cgi.escape(request.POST['picture'])
    rrp = int(rrp * 100) #convert P.pp to interger pence

    context = Context()
    try:
        lib.BOOK.create_book(isbn, title, author, year, edition, publisher, rrp, picture)
        tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'create_book_success.html')
    except Exception as e:
        context = Context({"error": e})
        tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'create_book_failure.html')

    response = HttpResponse()
    response.write(render_to_string(request, tmpl, context))
    return response

def render_book_json(request):
    isbn = cgi.escape(request.GET['isbn'])
    book = lib.BOOK.get_by_key_name(isbn)
    response = HttpResponse()
    response.write(json.dumps(book.as_dict()))
    return response

def render_listing(request, listing_id):
    "Page to show a listing, as well as other listings of the same book"
    listing = lib.USERBOOK.get(listing_id)
    book = listing.book
    seller = listing.user
    copies = lib.BOOK.list_book_copies(book.isbn)
    context = Context({
                       "book":book,
                       "seller":seller,
                       "current_book":listing,
                       "same_books":copies, 
                       "user": AuthManager.get_current_user(request)
                       })
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'listing.html')
    response = HttpResponse()
    response.write(render_to_string(request, tmpl, context))
    return response

def render_book(request, book_isbn):
    "Page to show the details of a single book"
    copies = lib.BOOK.list_book_copies(book_isbn)
    context = Context({
                        "user": AuthManager.get_current_user(request),
                        "book": lib.BOOK.get_by_key_name(book_isbn),
                        "book_listings": copies
                        })
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'book.html')
    response = HttpResponse()
    response.write(render_to_string(request, tmpl, context))
    return response

def render_book_image(request, book_isbn):
    isbn = cgi.escape(book_isbn)
    book = lib.BOOK.get_by_key_name(isbn)
    if book == None:
       return HttpResponseNotFound("Book was not found")
    return redirect(book.picture)
