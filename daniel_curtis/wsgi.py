"""
WSGI config for daniel_curtis project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "daniel_curtis.settings")

application = get_wsgi_application()
