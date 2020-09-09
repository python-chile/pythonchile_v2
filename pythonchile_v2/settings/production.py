import os
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['www.pythonchile.cl', 'pythonchile.cl', ]

ADMINS = [('Site admins', 'serverlogs@pythonchile.cl')]

SERVER_EMAIL = 'server@pythonchile.cl'

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

# Email Sendgrid config
DEFAULT_FROM_EMAIL = "web@pythonchile.cl"
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY', "")
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'  # this is exactly the value 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True


LOGGING = {
    'version': 1,
    'disable_existing_logger': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        }
    }
}
