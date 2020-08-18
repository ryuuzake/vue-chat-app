from .base import *

from os import environ

if environ['DJANGO_SETTINGS_MODULE'] == 'django_vue_chat_app.settings':
    from .development import *