"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from split_settings.tools import include

load_dotenv() 
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.environ.get('SECRET_KEY') 
DEBUG = os.environ.get('DEBUG', True) == 'True'
ALLOWED_HOSTS = ['127.0.0.1']
STATIC_URL = "static/"
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOCALE_PATHS = ['movies/locale']
INTERNAL_IPS = ["127.0.0.1"]


include('components/installed_apps.py') 
include('components/middleware.py') 
include('components/templates.py')
include('components/database.py') 
include('components/auth_password_validators.py') 


