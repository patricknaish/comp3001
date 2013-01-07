"""
Authentication management for users
"""

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
