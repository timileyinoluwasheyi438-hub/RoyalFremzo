import os
from pathlib import Path
import cloudinary
import cloudinary.api
import cloudinary.uploader
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'cloudinary',
    'cloudinary_storage',
    'core',
]

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

ROOT_URLCONF = 'hotel_website_engine.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'hotel_website_engine.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Cloudinary
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('dgvpwsxy0'),
    'API_KEY': os.getenv('564321755454527'),
    'API_SECRET': os.getenv('gscG8b7caHbSG2wnfiTHJx4gtVQ'),
}

cloudinary.config(
    cloud_name = os.getenv('dgvpwsxy0git'),
    api_key = os.getenv('564321755454527'),
    api_secret = os.getenv('gscG8b7caHbSG2wnfiTHJx4gtVQ')
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Static & Media
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'

# Render specific
if os.environ.get('RENDER'):
    MEDIA_ROOT = '/opt/render/project/src/media'

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'timileyinoluwasheyi1438@gmail.com'
EMAIL_HOST_PASSWORD = 'zczbezncwgalegwo'   # your current app password
EMAIL_TIMEOUT = 30

DEFAULT_FROM_EMAIL = 'Royal Frenzo <timileyinoluwasheyi1438@gmail.com>'
ADMIN_EMAIL = 'timileyinoluwasheyi1438@gmail.com'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Lagos'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'