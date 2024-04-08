# Import settings from base
from .base import *


# Set the debug status
DEBUG = True


# Set the allowed hosts
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]


# Database configuration
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "database" / "db.sqlite3",
    }
}
