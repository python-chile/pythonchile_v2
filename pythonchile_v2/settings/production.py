import os
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['pythonchile.cl', '165.227.61.182']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', "")  # Blank to ensure it being set

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME', "pythonchile_web"),
        'USER': os.environ.get('DB_USER', "postgres"),
        'PASSWORD': os.environ.get('DB_PASS', ""),
        'HOST': os.environ.get('DB_SERVICE', "localhost"),
        'PORT': os.environ.get('DB_PORT', 5432),
    }
}
