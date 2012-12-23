# DJANGO WEB SETTINGS FILE

# from djangoappengine.settings_base import *

import os

SECRET_KEY = '074953e23c03a689c90188843557c309bff231dc' # Needs setting

INSTALLED_APPS = (
    'web', ## OUR web classes
)

MIDDLEWARE_CLASSES = (
#    'web.middleware.sessions.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
)

LOGIN_REDIRECT_URL = '/'

# Some folders we use
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'images')
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'template'),)

# web.urls contains the url mapping to functions
ROOT_URLCONF = 'web.urls'

