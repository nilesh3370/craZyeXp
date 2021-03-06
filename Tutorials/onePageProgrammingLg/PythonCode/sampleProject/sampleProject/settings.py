"""
Django settings for sampleProject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#Dipankar: Define the path for all Directory 
here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)
#SITE_ROOT=here('../')
SITE_ROOT = os.path.abspath(os.path.join(here(''), os.pardir)) 



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q5#sg(^3fzdxb#!o1*!i=-+54iyz(%_qi#mw20(luzn_3yoo0y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_pdb',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_pdb.middleware.PdbMiddleware',
)

ROOT_URLCONF = 'sampleProject.urls'

WSGI_APPLICATION = 'sampleProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': here('Database/tickets.db'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# My Confugaration goes here .. 
STATIC_URL = '/static/'
MEDIA_ROOT =here('ProductData')
MEDIA_URL = '/pmedia/'
STATIC_ROOT = here('StaticFiles')
ROOT_URLCONF = 'sampleProject.urls'
TEMPLATE_DIRS = (
    here('templates'),
    )
# AutoDetect AppsEngines
ListHelperEngine=[ (d,os.path.join(SITE_ROOT,'AppsEngines',d)) for d in os.listdir(os.path.join(SITE_ROOT,'AppsEngines')) \
                   if os.path.isdir(os.path.join(SITE_ROOT,'AppsEngines',d))]
# Update Apps and Update Templates
for engine in ListHelperEngine:
    TEMPLATE_DIRS+=(os.path.join(engine[1],'templates'),)
    INSTALLED_APPS += ('AppsEngines.'+engine[0],)



