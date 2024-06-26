# Imports
import os
import dotenv
import datetime
from pathlib import Path


# Load the environment variables
dotenv.load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")


# Set the auth user model
AUTH_USER_MODEL = "home.User"


# Installed apps list
INSTALLED_APPS = [
    # Admin theme
    "jazzmin",
    # Default apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third party apps
    "corsheaders",
    "django_extensions",
    "rest_framework",
    "drf_yasg",
    # Installed apps
    "backend.apps.home.apps.HomeConfig",
    "backend.apps.customers.apps.CustomersConfig",
    "backend.apps.employees.apps.EmployeesConfig",
    "backend.apps.orders.apps.OrdersConfig",
    "backend.apps.jwtauth.apps.JwtauthConfig",
]


# Set the CORS origin whitelist
CORS_ALLOWED_ORIGINS = ["https://*"]


# Middleware list
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# Root URL configuration
ROOT_URLCONF = "backend.urls"


# Set templates config
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# WSGI application
WSGI_APPLICATION = "backend.wsgi.application"


# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Default auto field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Set the static files URL
STATIC_URL = "/static/"


# Set the static files root
STATIC_ROOT = BASE_DIR.parent / "staticfiles_build" / "static"


# # Set the static files directories
# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]


# Set the static files storage
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Django REST Framework Settings
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly"
    ],
    # "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    # "PAGE_SIZE": 10,
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    # "DEFAULT_THROTTLE_RATES": {"anon": "10/hour", "user": "100/hour"},
}


# Simple JWT Settings
SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": [
        "Bearer",
    ],
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(days=7),
}
