"""
WSGI config for pls project.

It exposes the WSGI callable as a module-level variable named ``application``.
c
For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pls.settings')

application = get_wsgi_application()
