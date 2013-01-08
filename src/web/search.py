import os
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from web import AuthManager
import cgi
import json
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
    if request.method == 'POST':
        return do_advanced_search(request)
    else:
        context = Context({"user": AuthManager.get_current_user(request)})
        tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'advanced.html')
        response = HttpResponse()
        response.write(loader.render_to_string(tmpl, context))
        return response

def do_advanced_search(request):
    matched_books = [] #Stores all the books that match the query

    #Get all the entered details
    title = cgi.escape(request.POST['title'].strip())
    isbn = cgi.escape(request.POST['isbn'].strip())
    author = cgi.escape(request.POST['author'].strip())
    all_books = lib.BOOK.list_all_books() #Grab all the books from the database

    if title:
        for book in all_books:
            if title.lower() in book.title.lower():
                matched_books.append(book)

    if isbn:
        for book in m1:
            if isbn.lower() in book.isbn.lower():
                matched_books.append(book)

    if author:
        for book in m2:
            if author.lower() in author.lower():
                matched_books.append(book)

    context = Context({ "book_list": matched_books,
                        "user": AuthManager.get_current_user(request)})
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'search.html')
    response = HttpResponse()
    response.write(loader.render_to_string(tmpl, context))
    return response

def search_predict(request):
    matched_books = []
    html = ""
    search = cgi.escape(request.GET['term'])
    book_list = lib.BOOK.list_all_books()
    for book in book_list:
        if search.lower() in book.title.lower():
            matched_books.append(book)
    matched_objects = list()
    for book in matched_books:
        matched_objects.append( { "label": book.title, "value": book.title } )
    response = HttpResponse()
    response.write(json.dumps(matched_objects))
    return response