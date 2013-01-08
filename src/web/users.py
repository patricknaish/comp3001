# Django magic
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from web import AuthManager

import lib

class MessageSendError(Exception):
    def __init__(self):
        Exception.__init__(self, "There was an error sending this message.")

def render_user(request, user_key):
    user = lib.USER.get(user_key)
    user_listings = lib.USER.list_books(user.email)
    context = Context({ "user_listings": user_listings,
    	                "viewing_user": user,
    	                "user": AuthManager.get_current_user(request)
                      })
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'user.html')
    response = HttpResponse()
    response.write(loader.render_to_string(tmpl, context))
    return response

def render_message(request, to_user, error = None):
    if request.POST['message'] and request.POST['subject']:
        return send_message(request, to_user, request.POST['message'], request.POST['subject'])
    else :
        context = Context({ "send_user": to_user })
        tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'message.html')
        response = HttpResponse()
        response.write(loader.render_to_string(tmpl, context))

def send_message(request, to_user, message, subject):
    try:
        lib.MESSAGE.create_message(AuthManager.get_current_user(request),to_user, subject, message)
        tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'send_message_success.html')
    except Exception:
        context = Context({"error": e})
        tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'send_message_failure.html')

    response = HttpResponse()
    response.write(loader.render_to_string(tmpl, context))
    return response

def render_inbox(request):
    user = AuthManager.get_current_user(request)
    context = Context({"user_messages": lib.USER.list_messages(user.email)})
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'inbox.html')
    response = HttpResponse()
    response.write(loader.render_to_string(tmpl, context))
    return response