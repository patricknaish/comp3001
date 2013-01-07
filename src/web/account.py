import os
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.template import Context

import lib
from web import AuthManager

def render_account(request):
    if not AuthManager.is_logged_in(request):
        return redirect("/login")
    try:
        user = lib.USER.get_by_key_name(request.session["user"])
    except:
        user = None
    context = Context({ "user": user})
    response = HttpResponse()
    tmpl = os.path.join(os.path.dirname(__file__), 'template', 'account.html')
    response.write(render_to_string(tmpl, context))
    return response

def render_account_test(request):
    if not users.get_current_user():
        return redirect("/login") #TODO: Pass account as a return-to page
    purchase_hist = [
    {"book": 
        {"image": "url",
        "title": "Title",
        "price": "10.00",
        "author": "Bob"}},
    {"book": 
        {"image": "url",
        "title": "Another Title",
        "price": "15.00",
        "author": "Bill"}}
    ]
    
    seller_list = [
    {"book": 
        {"image": "url",
        "title": "Title",
        "price": "10.00",
        "author": "Bob"}},
    {"book": 
        {"image": "url",
        "title": "Another Title",
        "price": "15.00",
        "author": "Bill"}}
    ]
    try:
        user = lib.USER.get_by_key_name(request.session["user"])
    except:
        user = None
    context = Context({
                       "purchase_history": purchase_hist, 
                       "user": user)
                       })
    response = HttpResponse()
    tmpl = os.path.join(os.path.dirname(__file__), 'template', 'account.html')
    response.write(render_to_string(tmpl, context))
    return response
