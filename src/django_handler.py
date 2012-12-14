# Set up our Django web environment.....
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")

# Get hold of a WSGI application to run
from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
