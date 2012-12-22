import os
from django.http import HttpResponse
from django.template import Context, loader
from django.core.exceptions import PermissionDenied
import cgi
from lib import BOOK
from web import AuthManager

def render_create_book(request):
    # Check permissions
    if not AuthManager.is_authenticated(request):
        raise PermissionDenied

    if not AuthManager.has_permission(request, 'check_book'):
        raise PermissionDenied

    # Handle the request if we're allowed to
    if request.method == 'POST':
        return create_book_action(request)
    else:
        context = Context()
        tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'create_book.html')
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
