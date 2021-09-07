"""
Django settings for webpage project.

Generated by 'django-admin startproject' using Django 3.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rmxq3lkq@nhlwgg)deu@q5e_nfmz8((qqe)v9s0vt*o5&i(ez%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['webpagedj19.herokuapp.com', 'localhost','127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'app_course_booking',
    'app_news',
    'app_food',
    'user',
    'g_pigeon_race',
    'a_social_network',
    'app_mail',
    'a_street_race',
    'a_index',
    'a_blog',
    'games',
    'application',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'embed_video',

]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
ROOT_URLCONF = 'webpage.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
)
WSGI_APPLICATION = 'webpage.wsgi.application'

import os
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'djdb',
#     }
# }
# #if secured 

# DATABASES = {
#     'default':{
#     'ENGINE': 'djongo',
#     'NAME': 's25',
#     'ENFORCE_SCHEMA':False,
#     'CLIENT': {
#         'host': 'mongodb+srv://dj19:aa09094553940@cluster0.hpgnf.mongodb.net/test'
#     }
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Manila'
TIME_INPUT_FORMATS = ('%I:%M %p',)
USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
import os
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'images')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
# Base url to serve media files
MEDIA_URL = '/images/'
# Path where media is stored
MEDIA_ROOT = os.path.join(BASE_DIR, 'images/')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

###### authenticate user from
AUTH_USER_MODEL = 'app_mail.User'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'application/static/'),

]