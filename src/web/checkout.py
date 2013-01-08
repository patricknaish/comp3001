# Django magic
import os
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import redirect

import lib
from web import AuthManager

def render_basket_add(request):
    if not "items" in request.session.keys():
        request.session["items"] = list()
    request.session["items"].append(request.POST["item"])
    return redirect(render_basket)

def render_basket(request):
    pp = lib.PAYPAL.Paypal();
    pp.sandbox = True
    pp.merchant_id = "comp30_1354642631_biz@lists.cmalton.me.uk"
    pp.pdt_auth_token = "lwcdLbpiHFwN8PJr08Rv6JVvYcmp90ivctfoJSWgBvANCrG-7iXJ59e8Qy4"
    user = AuthManager.get_current_user(request)
    context = Context({"user": user})
    if 'items' in request.session.keys():
        context["basket"] = list();
        for item in request.session['items']:
            userbook = lib.USERBOOK.get(item)
            context["basket"].append(userbook)
            total_cost = userbook.price
        item = lib.PAYPAL.Item("TT-BASKET", "TexTrader Basket", total_cost / 100)
        context["ppcheckout"] = pp.buy_now_button(item)
        tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'checkout.html')
    else:
        tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'emptybasket.html')
    response = HttpResponse()
    response.write(loader.render_to_string(tmpl, context))
    return response
