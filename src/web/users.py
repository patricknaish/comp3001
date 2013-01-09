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
    	                "viewing_user": user
                      })
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'user.html')
    response = HttpResponse()
    response.write(render_to_string(request, tmpl, context))
    return response

def render_message(request, to_user, error = None):
    if request.method == 'POST':
        return send_message(request, to_user, request.POST['message'], request.POST['subject'])
    else:
        context = Context({ "send_user": lib.USER.get(to_user),
                            "user": AuthManager.get_current_user(request) })
        tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'message.html')
        response = HttpResponse()
        response.write(loader.render_to_string(tmpl, context))
        return response

def send_message(request, to_user, message, subject):
    send_to_user = lib.USER.get(to_user)
    send_from_user = AuthManager.get_current_user(request)
    try:
        lib.MESSAGE.create_message(send_from_user.email,send_to_user.email, subject, message)
        context = Context({})
        tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'send_message_success.html')
    except Exception as e:
        context = Context({"error": str(e)})
        tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'send_message_failure.html')

    response = HttpResponse()
    response.write(loader.render_to_string(tmpl, context))
    return response

def render_inbox(request):
    user = AuthManager.get_current_user(request)
    context = Context({"user_messages": lib.USER.list_received_messages(user.email),
                       "user": AuthManager.get_current_user(request)})  
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'inbox.html')
    response = HttpResponse()
    response.write(loader.render_to_string(tmpl, context))
    return response

def render_sentbox(request):
    user = AuthManager.get_current_user(request)
    context = Context({"user_messages": lib.USER.list_sent_messages(user.email),
                       "user": AuthManager.get_current_user(request)})
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'sentbox.html')
    response = HttpResponse()
    response.write(loader.render_to_string(tmpl, context))
    return response