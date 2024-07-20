""" Settings file to run the project locally on the local OS using a virtual environment."""

from .development import *

DEBUG = True
ALLOWED_HOSTS = ['*']  # To be changed

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

