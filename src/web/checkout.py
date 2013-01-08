# Django magic
import os
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import redirect

import lib
from web import AuthManager
from web.TemplateWrapper import render_to_string

def render_basket_add(request):
    if not "items" in request.session.keys():
        request.session["items"] = set()
    if not request.POST["item"] in request.session["items"]:
        request.session["items"].append(request.POST["item"])
    return redirect(render_basket)

def render_basket(request):
    pp = lib.PAYPAL.Paypal();
    pp.sandbox = True
    pp.merchant_id = "comp30_1354642631_biz@lists.cmalton.me.uk"
    pp.pdt_auth_token = "lwcdLbpiHFwN8PJr08Rv6JVvYcmp90ivctfoJSWgBvANCrG-7iXJ59e8Qy4"
    pp.return_url = "http://%s/paypal_pdt" % request.get_host()
    pp.set_pdt_mode("enabled")
    user = AuthManager.get_current_user(request)
    context = Context({"user": user})
    if 'items' in request.session.keys():
        total_cost = 0
        for item in request.session['items']:
            userbook = lib.USERBOOK.get(item)
            total_cost += userbook.price
        item = lib.PAYPAL.Item("TT-BASKET", "TexTrader Basket", total_cost / 100)
        context["ppcheckout"] = pp.buy_now_button(item)
        tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'checkout.html')
    else:
        tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'emptybasket.html')
    response = HttpResponse()
    response.write(render_to_string(request, tmpl, context))
    return response

def render_pp_return(request):
    pp = lib.PAYPAL.Paypal()
    pp.sandbox = True
    pp.merchant_id = "comp30_1354642631_biz@lists.cmalton.me.uk"
    pp.pdt_auth_token = "lwcdLbpiHFwN8PJr08Rv6JVvYcmp90ivctfoJSWgBvANCrG-7iXJ59e8Qy4"
    pdt_data = pp.get_pdt_data(request.GET["tx"])
    import logging
    logging.info("PDT data is: %s" % dir(pdt_data))
    response = HttpResponse()
    return response
