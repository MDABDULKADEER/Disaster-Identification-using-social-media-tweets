"""
WSGI config for adeep_attentive_multimodal_learning_aApproach

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adeep_attentive_multimodal_learning_aApproach.settings')
application = get_wsgi_application()
