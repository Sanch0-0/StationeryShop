"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from dotenv import load_dotenv
from pathlib import Path
from django.urls import reverse_lazy

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-f7wmiv1t3ey!n#w48i2(ljypyvf%d)1)7&49jntz7%=wbmk0^b'

# Session settings
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Log out when the browser is closed
SESSION_COOKIE_AGE = 1209600  # Two weeks in seconds (only if "Remember me" is checked)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'django_recaptcha',
    'easy_thumbnails',
    'image_cropping',
    'shop',
    'users',
    'cart',
    'favourite',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart_info',
                'shop.context_processors.top_rated_products',
                'favourite.context_processors.favourite_info',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql',

        'NAME': os.getenv("DB_NAME"),

        'USER': os.getenv("DB_USER"),

        'PASSWORD': os.getenv("DB_PASSWORD"),

        'HOST': os.getenv("DB_HOST"),

        'PORT': os.getenv("DB_PORT"),

    }

}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + ('easy_thumbnails.processors.colorspace',
     'easy_thumbnails.processors.autocrop',
     'easy_thumbnails.processors.scale_and_crop',
     'easy_thumbnails.processors.filters',)

# Optionally, set up thumbnail aliases
THUMBNAIL_ALIASES = {
    '': {
        'product_thumbnail': {'size': (200, 200), 'crop': True},
    },
}



# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Bishkek'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


STATIC_URL = 'static/'
# STATIC_ROOT = 'static/'
STATICFILES_DIRS = [
    'static'
]


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'users.backends.EmailOrUsernameModelBackend'
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


AUTH_USER_MODEL = "users.User"
LOGIN_URL =  reverse_lazy("login")


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'fff.alex.er1317.fff@mail.ru'
EMAIL_HOST_PASSWORD = 'FiP9e1Ltx9mcR9PubcZC'


RECAPTCHA_PUBLIC_KEY = '6LemUzgqAAAAAGOcdb2DcLyThy8716EF3v7hpPw5'
RECAPTCHA_PRIVATE_KEY = '6LemUzgqAAAAAJfYSMT6YbpiHqnFnSYBeGNUi1Hw'
