"""
WSGI config for Tercera_Pre_Entrega_Cristian_Pereyra project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tercera_Pre_Entrega_Cristian_Pereyra.settings')

application = get_wsgi_application()
