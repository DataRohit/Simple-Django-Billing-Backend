# Import settings from base
from .base import *


# Set the debug status
DEBUG = False


# Set the allowed hosts
ALLOWED_HOSTS = [".vercel.app"]


# PostgreSQL database settings
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "billing_db",
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": "5432",
        "OPTIONS": {
            "sslmode": "require",
        },
    }
}
