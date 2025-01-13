# settings.py

import os
from pathlib import Path

# BASE_DIR is the directory containing the 'manage.py' file
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# For local development, you can set it directly here, but in production, store it in an environment variable
SECRET_KEY = '#nhm+t@(***^k)+97*mu(xupy73(6q#=ev!eyr)0271a+s36sp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []  # Add your domain or IP address in production (e.g., ['example.com'])

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'agriculture', 
    'smart_agriculture', # Your custom app (if you have one)
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

ROOT_URLCONF = 'smart_agriculture.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # You can set up your templates folder here
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

WSGI_APPLICATION = 'smart_agriculture.wsgi.application'

# Database settings (use SQLite for development, PostgreSQL or MySQL for production)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
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

# Localization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Optional settings for managing media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Optional: If you're using an environment variable for the secret key in production
# SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
# CSRF settings
CSRF_COOKIE_NAME = 'csrftoken'  # Default name for the CSRF cookie
CSRF_COOKIE_HTTPONLY = False    # Allow JavaScript to access CSRF token
CSRF_COOKIE_SECURE = False      # Set to True if you're using HTTPS
CSRF_HEADER_NAME = 'X-CSRFToken'  # Header to be used in AJAX requests

# Additional CSRF settings if needed
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]
