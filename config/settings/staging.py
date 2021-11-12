from .base import *

DEBUG = True

ALLOWED_HOSTS = []
CORS_ORIGIN_ALLOW_ALL = True

DATABASES = {
    'default': {
        'NAME': 'email_verifier',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',
        'PORT': 5432,
    },
}

SITE_ID = 1

INSTALLED_APPS += [
    'drf_yasg',
]

# REDIS related settings

REDIS_HOST = 'localhost'
REDIS_PORT = '6379'
CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': ROOT_DIR.parent / 'cache' / 'default',
        'TIMEOUT': 60 * 60 * 24 * 6,
    },
}

