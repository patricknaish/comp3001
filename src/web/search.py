import os
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from web import AuthManager

import lib

def render_search(request):
    search_string = request.GET['s']
    matched_books = []
    all_books = lib.BOOK.list_all_books() #Grab all the books from the database
    for book in all_books:
        if search_string.lower() in book.title.lower():
        	matched_books.append(book)
    context = Context({ "book_list": matched_books,
    	                "user": AuthManager.get_current_user(request)})
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'search.html')
    response = HttpResponse()
    response.write(loader.render_to_string(tmpl, context))
    return response

def render_advanced_search(request):
    return response