import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e00&@ismy&k9nn6a!(_i4(mwna315u9n(xd3_n+v#=pjc1ee3-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #Third-party apps
        'rest_framework',
        'corsheaders',
        
    #Local apps
        'accounts',
        'store',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
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
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'


DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
# Custom User Model
AUTH_USER_MODEL = 'accounts.CustomUser'

# CORS
CORS_ALLOW_ALL_ORIGINS = True 

# Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


JAZZMIN_SETTINGS = {
    "site_title": "iTechBox Admin",
    "site_header": "iTechBox Dashboard",
    "site_brand": "iTechBox",
    "welcome_sign": "Welcome to iTechBox Management",
    "copyright": "iTechBox Ltd",
    "search_model": ["store.Product", "accounts.CustomUser"],
    "topmenu_links": [
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},
        {"model": "accounts.CustomUser"},
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "order_with_respect_to": ["store", "accounts"],
    "icons": {
        "accounts.CustomUser": "fas fa-user",
        "store.Product": "fas fa-mobile-alt",
        "store.Category": "fas fa-list",
        "store.Brand": "fas fa-tag",
    },
}

# ড্যাশবোর্ডের কালার থিম কাস্টমাইজেশন
JAZZMIN_UI_TWEAKS = {
    "navbar_variant": "navbar-dark",
    "theme": "flatly", # মডার্ন থিম
    "accent": "accent-warning", # আপনার Orange কালারের কাছাকাছি
}