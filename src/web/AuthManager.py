"""
Authentication management for users
"""

import lib

def has_permission(request, perm_name):
    "Check if a user has a given permission"
    if is_logged_in(request):
        return True
    else:
        return False

def is_logged_in(request):
    "Is the user logged in?"
    if "user" in request.session.keys():
        return True
    else:
        return False

def set_logged_in(request, user):
    request.session["user"] = user

def set_logged_out(request):
    del request.session["user"]

def get_current_user(request):
    "Get the current user object"
    if not is_logged_in(request):
        return None
    return lib.USER.get_by_key_name(request.session["user"])
