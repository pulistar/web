from .settings import *
import os

WIBBLE2 = 'Wibble2'




CSRF_TRUSTED_ORIGINS = ['https://saludbienestar.azurewebsites.net/', '*']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',


    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
   'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')