import os
import environ
import csv, config
import datetime


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# main project directory adesua-api/
ROOT_PATH = environ.Path(__file__) -3

# public directory adesua-api/adesua
PUBLIC_PATH = ROOT_PATH.path('text')

env = environ.Env()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dr@@snbmujxx-=3#=+4qy2egf7prk2e(45ur=ovyr1f4(%5==2'

# Application definition
THIRD_PARTY_APPS = [
    'crispy_forms',  # Form layouts
    'allauth',  # registration
    'allauth.account',  # registration
    'allauth.socialaccount',
    'rest_framework',
    'rest_auth.registration',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_framework_jwt',
    'rest_framework_docs',
    'corsheaders',
    # 'django_twilio',
    # 'South',
]

MY_APPS = [
    'users',
    'lists',
    'sms',
    'wallet',
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + MY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(PUBLIC_PATH('templates'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

DATABASES = {
    'default': env.db('DATABASE_URL', default='postgres:///textinfinity'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# for cors header
CORS_ORIGIN_ALLOW_ALL = True

# CORS_ORIGIN_WHITELIST = [

# ]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LTIME_ZONE = 'UTC'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# REST FRAMEWORK CONFIGURATION
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    ),
    # 'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

# JWT CUSTOM DEFAULTS
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
}

# Activating the Custom Serializers
REST_AUTH_REGISTER_SERIALIZERS = {
        'REGISTER_SERIALIZER': 'users.custom_registration.CustomRegistrationSerializer',
        # 'LOGIN_SERIALIZER': 'adesua.apps.general.users.register_serializer.LoginSerializer'
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    str(PUBLIC_PATH('static')),
]

STATIC_ROOT = str(ROOT_PATH('staticfiles'))

MEDIA_URL = '/media/'
MEDIA_ROOT = str(PUBLIC_PATH('media'))

# some cool defaults
URL_PREFIX = 'http://app.textinfinity.com/#/'
DEPOSIT_PREFIX = 'TNF'


# authentication defaults
# Some really nice defaults
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = True
EMAIL_CONFIRMATION_SIGNUP = True

# use one at a time
ACCOUNT_EMAIL_VERIFICATION = 'optional'
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# all time defaults
ACCOUNT_ALLOW_REGISTRATION = True
ACCOUNT_ADAPTER = 'users.adapters.AccountAdapter'
LOGOUT_ON_PASSWORD_CHANGE = False
LOGIN_URL = 'account_login'
AUTH_USER_MODEL = 'users.User'
REST_USE_JWT = True
