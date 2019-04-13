from .base import *
from decouple import Csv, config
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': config('ENGINE', default='django.db.backends.postgresql'),
        'NAME': config('NAME', default='textinfinity'),
        'HOST': config('HOST', default='127.0.0.1'),
        'PORT': config('PORT', default='5432'),
        'USER': config('USER', default='postgres'),
        'PASSWORD': config('PASSWORD', default='postgres')
    }
}

# email configuration
EMAIL_SUBJECT_PREFIX = 'Text-Infinity'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = 'developer@forever#'
EMAIL_HOST_USER = 'metesteremail@gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = 'Text-Infinity <noreply@textinfinity.com>'
