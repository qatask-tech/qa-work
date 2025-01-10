# settings.py

from pathlib import Path
import os



# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Security and Debug Settings
SECRET_KEY = 'django-insecure-jge)8&t5moe4!8xaos!jp6qpn4gp2=4+hjxukxkauxn!wg1ww('
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Application Definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'system',  # Assuming 'system' is your main app
    'numbercheck', 
    'marksheet',
    'service',
    'tinymce',
    'static',
    'contact',
    'news',

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

ROOT_URLCONF = 'system.urls'
WSGI_APPLICATION = 'system.wsgi.application'

# Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Using Path object here
    }
}

# Templates Configuration

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates",  # General templates folder
            BASE_DIR / "system/templates"  # App-specific folder
        ],
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






# Password Validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static Files Configuration
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # Use Path object for static directory
]

# Media Files Configuration
MEDIA_ROOT = BASE_DIR / 'media'  # Use Path object for media directory
MEDIA_URL = '/media/'

# Default Auto Field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
