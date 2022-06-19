<<<<<<< HEAD
"""
WSGI config for zcovid project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zcovid.settings')

application = get_wsgi_application()
=======
"""
WSGI config for zcovid project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zcovid.settings')

application = get_wsgi_application()
>>>>>>> b462ff9ba88ceb37fdfc4830eb6a7fe7c9623a9f
