
import os
import sys
from dotenv import load_dotenv
#----------------------------------------------------

# base_dir config
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
STATIC_DIR=os.path.join(BASE_DIR,'/static/')

# Adicionar essa tag para que nosso projeto encontre o .env
load_dotenv(os.path.join(BASE_DIR, ".env"))
#----------------------------------------------------

# Diz para Django onde estão nossos aplicativos
APPS_DIR = str(os.path.join(BASE_DIR,'apps'))
sys.path.insert(0, APPS_DIR)
#----------------------------------------------------

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#----------------------------------------------------

ALLOWED_HOSTS = ['.vercel.app','now.sh','127.0.0.1','localhost']


# Application definition
DJANGO_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_APPS = [
    # Outros aplicativos de terceiros aqui
]

PROJECT_APPS = [
    'apps.base',
    'apps.pages',
    # Seus aplicativos personalizados aqui
]

INSTALLED_APPS = DJANGO_APPS + THIRD_APPS + PROJECT_APPS
#----------------------------------------------------


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'


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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
DATABASES = {
	'default': {
	'ENGINE': 'django.db.backends.sqlite3',
	'NAME': os.path.join(BASE_DIR, os.getenv('NAME_DB')),
		#'USER':os.getenv('USER_DB')
		#'PASSWORD': os.getenv('PASSWORD_DB')
		#'HOST':os.getenv('HOST_DB')
		#'PORT':os.getenv('PORT_DB')
	}
}
#----------------------------------------------------


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# Se quiser deixar em PT BR
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Manaus'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles', 'static')

# used to specify additional directories from which to load static files


MEDIA_ROOT=os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'
#----------------------------------------------------


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Se tiver configuração de email
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
SERVER_EMAIL = DEFAULT_FROM_EMAIL
#----------------------------------------------------
