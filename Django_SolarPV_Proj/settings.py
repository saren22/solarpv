"""
Django settings for Django_SolarPV_Proj project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$+0ebc18v0h$zzqwog#q^iiy=pryf(*@rz_u!d1frs(5dw37^_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
##pythonanwhere database settings
#ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'solarpv',
    'backend',
    'rest_framework',
    'accounts',
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

ROOT_URLCONF = 'Django_SolarPV_Proj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'solarpv/templates/solarpv')],
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

WSGI_APPLICATION = 'Django_SolarPV_Proj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

##localhost database settings
DATABASES = {
    'default': {
        # MySQL database engine class.
        'ENGINE': 'django.db.backends.mysql',
        # MySQL database host ip.
        'HOST': 'localhost',
        # port number.
        'PORT': '3306',
        # database name.
        'NAME': 'solarpv_db',
        # user name.
        'USER': 'root',
        # password
        'PASSWORD': 'password',
    }
}

##pythonanwhere database settings
""" DATABASES = {
    'default': {
        # MySQL database engine class.
        'ENGINE': 'django.db.backends.mysql',
        # MySQL database host ip.
        'HOST': 'skuma143.mysql.pythonanywhere-services.com',
        # database name.
        'NAME': 'skuma143$solarpv_db',
        # user name.
        'USER': 'skuma143',
        # password
        'PASSWORD': 'pythonanywhere',
    }
} """


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'solarpv/static/solarpv/')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'solarpv/assets/')

##$ python manage.py collectstatic
##This will copy all files from your static folders(STATICFILES_DIRS) into the STATIC_ROOT directory.
##Finally uses files on STATIC_ROOT path
##STATIC_URL = '/static/' -- This is to tell browser to create folder for static files with this name 'static' 
