"""
ASGI config for daniel_curtis project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "daniel_curtis.settings")

application = get_asgi_application()
