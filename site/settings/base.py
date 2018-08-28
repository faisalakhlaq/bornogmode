"""
Base settings for project. It is shared across all the settings.
"""

import os
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Initialize the root of the whole project
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '../..'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't_w4todgix36gw)vp=cjb&_2!-*(ge1b$deke7+t^gvippfxp)'

DEBUG = False

LANGUAGE_CODE = 'en-us'
LANGUAGES = (
    ('da', 'Dansk'),
    ('en', 'English')
)
LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, 'site/locale'),
)

ALLOWED_HOSTS = []


BASE_PROJECT_APPS = [
    'apps.clothes',
    'apps.pages',
    'apps.utils',
    'apps.brands',
    'apps.products',
    'apps.cart',
    'apps.childcarts'
]
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

] + BASE_PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'base.urls'

# template files directory
TEMP_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMP_DIR,
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'base.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME', 'bornogmode'),
        'USER': os.environ.get('DB_USER', 'bornogmode'),
        'PASSWORD': os.environ.get('DB_PASS', 'bornogmodeDBpassword'),
        'HOST': os.environ.get('DB_SERVICE', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, "site/static"),
)

STATIC_ROOT = os.path.join(PROJECT_ROOT, "static_root")
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media")
MEDIA_URL = '/media/'
CART_SESSION_ID = 'cart'
