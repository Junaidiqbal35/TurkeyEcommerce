# pass ---12
# email --- adanzoabi207997@gmail.com
# username admin
from decouple import config
from django.utils.translation import gettext as _
from pathlib import Path
import os

# to secure the sensetive information we use the dot emv file to store them
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG')

ALLOWED_HOSTS = ['www.dianturkeyshop.com', '54.187.114.173', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'category',
    'accounts',
    'store',
    'carts',
    'orders',
    # 'admin_honeypot',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # for translation
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'web_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],  # we add these to tell the settings that we use folder name's templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.contrib.messages.context_processors.messages',
                # tell the templates that we using context_processors
                'category.context_processors.menu_links',  # we can use the def men_links in all the templates
                'carts.context_processors.counter',
            ],
        },
    },
]

WSGI_APPLICATION = 'web_project.wsgi.application'
# we will tell the settings the we use custome user model
AUTH_USER_MODEL = 'accounts.Account'
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('name'),
        'USER': config('user'),
        'PASSWORD': config('password'),
        "HOST": config('host'),
        "PORT": 5432
    }
}

# use this for development
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

MIDDLEWARE = [
                 'whitenoise.middleware.WhiteNoiseMiddleware',
             ] + MIDDLEWARE
INSTALLED_APPS = [
                     'whitenoise.runserver_nostatic',
                 ] + INSTALLED_APPS
# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'  # the primary language for the website

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale")
]
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/images/'

STATIC_ROOT = BASE_DIR / 'static'
PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# media files configuration 
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    # info is the name of bootstrap class we change this to error
    messages.ERROR: 'danger',
}
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# celery and redis setting
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER", "redis://localhost:6379/0")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_BROKER", "redis://localhost:6379/0")

# smtp configuration

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'imjuni.pythondev@gmail.com'
EMAIL_HOST_PASSWORD = 'onjvyvhlvfszbceo'
EMAIL_USE_TLS = True


