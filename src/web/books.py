import os
from django.http import HttpResponse
from django.template import Context, loader
import cgi

def render_create_book(request):
    context = Context()
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'create_book.html')
    response = HttpResponse()
    response.write(loader.render_to_string(tmpl, context))
    return response
	
def create_book_action(request):
    isbn = cgi.escape(request.get('isbn'))
    title = cgi.escape(request.get('title'))
    author = cgi.escape(request.get('author'))
    year = int(cgi.escape(request.get('year')))
    edition = cgi.escape(request.get('edition'))
    publisher = cgi.escape(request.get('publisher'))
    rrp = double(cgi.escape(request.get('rrp')))
    picture = cgi.escape(request.get('picture'))
    rrp = int(rrp * 100) #convert P.pp to interger pence
	
    context = Context()
                            
    try:
        BOOK.create_book(isbn, title, author, year, edition, publisher, rrp, picture)
        tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'create_book_success.html')
    except:
        tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'create_book_failure.html')
		
    response = HttpResponse()
    response.write(loader.render_to_string(tmpl, context))
    return response