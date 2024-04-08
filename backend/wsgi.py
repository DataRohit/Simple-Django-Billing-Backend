# Imports
import os
from django.core.wsgi import get_wsgi_application


# Set the default Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings.prod")


# Initialize the WSGI application
app = application = get_wsgi_application()
