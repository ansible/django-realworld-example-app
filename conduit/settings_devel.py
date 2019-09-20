import os

from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT'),
    }
}
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
MEDIA_ROOT = os.getenv('MEDIA_ROOT')
STATIC_ROOT = os.getenv('STATIC_ROOT')
