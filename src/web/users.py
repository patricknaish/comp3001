# Django magic
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from web import AuthManager

import lib

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
