import os

from .base import *  # noqa: F401,F403

# Django Settings
# =============================================================

SECRET_KEY = 'django-insecure-+c+u1*-_k=^ix+wcn0s7b75bewn6ay3v1%t%=6^+v8&krz#3w+'
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('DB_HOST', 'postgres'),
        'NAME': os.environ.get('DB_NAME', 'data_provider'),
        'USER': os.environ.get('DB_USER', 'data_provider'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# Additional settings
# =============================================================
ENV = 'local'
