# Django magic
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from web import AuthManager

import lib

def render_user(request, user_key):
	user = lib.USER.get(user_key)
    context = Context({ 
    	                "viewing_user": user,
    	                "user": AuthManager.get_current_user(request)
    	              })
    tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'user.html')
    response = HttpResponse()
    response.write(loader.render_to_string(tmpl, context))
    return response
