# Set up our Django web environment.....
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")

# Get hold of a WSGI application to run
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Get the Google App Engine Utilities
from google.appengine.ext.webapp import util

# Run Django via GAE
util.run_wsgi_app(application)
