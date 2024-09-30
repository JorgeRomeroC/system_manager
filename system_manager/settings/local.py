import os

from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': get_secret('DB_ENGINE'),
#         'NAME': get_secret('DB_NAME'),
#         'HOST':get_secret('DB_HOST'),
#         'USER': get_secret('DB_USER'),
#         'PASSWORD': get_secret('DB_PASSWORD'),
#         'PORT': get_secret('DB_PORT')
#     }
# }

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

CKEDITOR_5_CUSTOM_CSS = {
    'default': 'css/custom.css',
}

CKEDITOR_5_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
CKEDITOR_5_UPLOAD_PATH = "upload/"
CK_EDITOR_5_UPLOAD_FILE_VIEW_NAME = "custom_upload_file"

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')