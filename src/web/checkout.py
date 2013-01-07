# Django magic
import os
from lib import Paypal
from django.http import HttpResponse
from django.template import Context, loader

import lib

def render_basket(request):
    pp = Paypal.Paypal();
    pp.sandbox = True
    pp.merchant_id = "comp30_1354642631_biz@lists.cmalton.me.uk"
    pp.pdt_auth_token = "lwcdLbpiHFwN8PJr08Rv6JVvYcmp90ivctfoJSWgBvANCrG-7iXJ59e8Qy4"
    item = Paypal.Item("TEST", "Test item", 10.00)
    try:
        user = lib.USER.get_by_key_name(request.session["user"]),
    except:
        user = None
    context = Context({"user": user})
    if 'items' in request.session.keys():
        context["basket"] = request.session['items']
        context["ppcheckout"] = pp.buy_now_button(item)
        tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'checkout.html')
    else:
        tmpl =  os.path.join(os.path.dirname(__file__), 'template', 'emptybasket.html')
    response = HttpResponse()
    response.write(loader.render_to_string(tmpl, context))
    return response
