# DJANGO WEB SETTINGS FILE

# from djangoappengine.settings_base import *

import os

SECRET_KEY = '' # Needs setting

INSTALLED_APPS = (
    'web', ## OUR web classes
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
)

LOGIN_REDIRECT_URL = '/'

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'images')
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'template'),)

ROOT_URLCONF = 'web.urls'
