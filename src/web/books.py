"""
This module handles the actual books.
This includes rendering the individual book pages, adding new books etc.
"""

import os
from django.http import HttpResponse
from django.template import Context, loader
from django.core.exceptions import PermissionDenied
import cgi
import json
from lib import BOOK
from lib import USER
from web import AuthManager

def render_create_book(request):
    "Show the create book form"
    # Check permissions
    if not AuthManager.has_permission(request, 'create_book'):
        raise PermissionDenied

    # Handle the request if we're allowed to
    if request.method == 'POST':
        return create_book_action(request)
    else:
        context = Context({"user": USER.get_by_key_name(request.session["user"])})
        tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'create_book.html')
        response = HttpResponse()
        response.write(loader.render_to_string(tmpl, context))
        return response

def render_create_listing(request):
    "Show the create book form"
    # Check permissions
    if not AuthManager.has_permission(request, 'list_book'):
        raise PermissionDenied

    # Handle the request if we're allowed to
    if request.method == 'POST':
        return list_book_action(request)
    else:
        context = Context({
                           "user": USER.get_by_key_name(request.session["user"]),
                           "books": BOOK.list_all_books()
                           })
        tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'list_book.html')
        response = HttpResponse()
        response.write(loader.render_to_string(tmpl, context))
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
        BOOK.create_book(isbn, title, author, year, edition, publisher, rrp, picture)
        tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'create_book_success.html')
    except Exception as e:
        context = Context({"error": e})
        tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'create_book_failure.html')

    response = HttpResponse()
    response.write(loader.render_to_string(tmpl, context))
    return response

def render_book_json(request):
    isbn = cgi.escape(request.GET['isbn'])
    book = BOOK.get_by_key_name(isbn)
    response = HttpResponse()
    response.write(json.dumps(book.as_dict()))
    return response
