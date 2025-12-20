"""
WSGI config for samaj_site project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
import sys

# add your project directory to the sys.path
project_home = '/home/Kantha27MevadaSuthar/samaj_site'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# add virtualenv site-packages to sys.path
venv_path = '/home/Kantha27MevadaSuthar/venv/lib/python3.13/site-packages'
if venv_path not in sys.path:
    sys.path.insert(0, venv_path)

# set Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'samaj_site.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
