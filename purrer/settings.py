"""
Django settings for purrer project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# LOGIN REDIRECT URL
LOGIN_URL = 'accounts/login'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

#import secrets
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'purrer'
#SECRET_KEY = secrets.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'meows',
    'storages',
    'bootstrap3',
    'rest_framework',
    
)

MIDDLEWARE_CLASSES = (
    #'html5_appcache.middleware.appcache_middleware.AppCacheAssetsFromResponse',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# REST_FRAMEWORK = {
#     # Use Django's standard `django.contrib.auth` permissions,
#     # or allow read-only access for unauthenticated users.
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#     ]
# }

ROOT_URLCONF = 'purrer.urls'

WSGI_APPLICATION = 'purrer.wsgi.application'

def get_cache():
  import os
  try:
    os.environ['MEMCACHE_SERVERS'] = os.environ['MEMCACHIER_SERVERS'].replace(',', ';')
    os.environ['MEMCACHE_USERNAME'] = os.environ['MEMCACHIER_USERNAME']
    os.environ['MEMCACHE_PASSWORD'] = os.environ['MEMCACHIER_PASSWORD']
    return {
      'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
        'TIMEOUT': 500,
        'BINARY': True,
        'OPTIONS': { 'tcp_nodelay': True }
      }
    }
  except:
    return {
      'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
      }
    }

CACHES = get_cache()

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',)
}


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


import dj_database_url
DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

AUTH_USER_MODEL = 'meows.User'


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Media Files (User images, and Post Images)
# Suggestion from Tyler Lubeck on Piazza
#MEDIA_ROOT = os.path.join(BASE_DIR, "static")

#########################################
#    AMAZON S3 WEB SERVICES SETTINGS    #
#########################################

#This makes sure that wehn files are uploaded to S3, browsers are given
#an HTTP header in the response. The headers in turn will tell
#browsers that they can cache these files for a very long time

# AWS_HEADERS = {
#     'Expires': 'Thu, 31 Dec 2099 20:00:00 EST',
#     'Cache-Control': 'max-age=94608000',
# }



#AWS_STORAGE_BUCKET_NAME = secrets.BUCKET_NAME
#AWS_ACCESS_KEY_ID = secrets.KEY_ID
#AWS_SECRET_ACCESS_KEY = secrets.ACCESS_KEY

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# Tell the staticfiles app to use S3Boto storage when writing the
# collected static files (when you run `collectstatic`).
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_LOCATION = 'static'

# This is used by the `static` template tag from `static`, if you're using
# that. Or if anything else refers directly to STATIC_URL. So it's safest
# to always set it.
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

# CONFIGURATIONS FOR MEDIA FILES (FILES USERS UPLOAD)
MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)

DEFAULT_FILE_STORAGE = 'purrer.custom_storages.MediaStorage'

#CUSTOM USER
CUSTOM_USER_MODEL = 'meows.User'
