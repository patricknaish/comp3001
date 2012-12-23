# Set up our Django web environment.....
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")

# Get hold of a WSGI application to run
import django.core.handlers.wsgi
app = django.core.handlers.wsgi.WSGIHandler()
