from django.template import Context, loader
from web import AuthManager
import lib

def render_to_string(request, template, context = None):
    if context == None:
        context = Context()
    if not "items" in request.session.keys():
        request.session["items"] = list()
    context["user"] = AuthManager.get_current_user(request)
    context["basket"] = list();
    for item in request.session['items']:
        userbook = lib.USERBOOK.get(item)
        context["basket"].append(userbook)
    return loader.render_to_string(template, context)
