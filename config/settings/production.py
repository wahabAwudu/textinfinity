from .base import *
from decouple import config, Csv



DEBUG = False

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# django whitenoise for staticfiles in production
MIDDLEWARE += [
  'whitenoise.middleware.WhiteNoiseMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# redis caches
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            'IGNORE_EXCEPTIONS': True,
        }
    }
}

# email configuration
EMAIL_SUBJECT_PREFIX = 'Text-Infinity'
SERVER_EMAIL = 'Text-Infinity'

# Anymail with Mailgun
# INSTALLED_APPS += ['anymail', ]
# ANYMAIL = {
#     'MAILGUN_API_KEY': env('DJANGO_MAILGUN_API_KEY'),
#     'MAILGUN_SENDER_DOMAIN': env('MAILGUN_SENDER_DOMAIN')
# }

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_PASSWORD = config('SENDGRID_USERNAME')
EMAIL_HOST_USER = config('SENDGRID_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = 'Text-Infinity <noreply@textinfinity.com>'
