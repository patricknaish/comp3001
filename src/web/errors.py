import os
from django.shortcuts import redirect

def permission_denied(request):
    # If they are logged in, show access denied, else login form
    if "user" in request.session.keys():
        redirect("django.views.defaults.permission_denied")
    else:
        redirect("/login?origin=%s" % request.path)

