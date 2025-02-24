"""
ASGI config for adeep_attentive_multimodal_learning_aApproach

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adeep_attentive_multimodal_learning_aApproach.settings')

application = get_asgi_application()
