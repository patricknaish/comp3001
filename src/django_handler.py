# Set up our Django web environment.....
import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")
# Add the GAEUtilites magic
sys.path.append(os.path.sep.join([ os.path.dirname( os.path.realpath( __file__ ) ), "gaeutilities" ]))
sys.path.append(os.path.sep.join([ os.path.dirname( os.path.realpath( __file__ ) ), "gaeutilities", "appengine_utilities" ]))

# Get hold of a WSGI application to run
import django.core.handlers.wsgi
app = django.core.handlers.wsgi.WSGIHandler()
