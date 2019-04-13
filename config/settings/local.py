from .base import *

DEBUG = True

ALLOWED_HOSTS = []

# email configuration
EMAIL_SUBJECT_PREFIX = 'Text-Infinity'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = 'developer@forever#'
EMAIL_HOST_USER = 'metesteremail@gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = 'Text-Infinity <noreply@textinfinity.com>'
