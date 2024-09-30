# import json
# from pathlib import Path
#
# from django.core.exceptions import ImproperlyConfigured
#
# from .jazzmin_settings import JAZZMIN_SETTINGS
#
# with open('secrets.json') as f:
#     secrets = json.loads(f.read())
#
# def get_secret(secret_name, secrets=secrets):
#     try:
#         return secrets[secret_name]
#     except:
#         msg = 'La variable %s no existe' % secret_name
#         raise ImproperlyConfigured(msg)
#
#
# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent.parent
#
# SECRET_KEY = get_secret('SECRET_KEY')
#
#
# DJANGO_APPS = [
#     'jazzmin',
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
# ]
#
# LOCAL_APPS = [
#     'applications.user',
#     'applications.assets',
#
# ]
#
# THIRD_PARTY_APPS = [
#     'rest_framework',
#     'django_ckeditor_5',
#     'django_extensions',
#     'corsheaders',
#
# ]
#
# INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS
#
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'corsheaders.middleware.CorsMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]
#
# ROOT_URLCONF = 'system_manager.urls'
#
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [ BASE_DIR / 'templates' ],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
#
# WSGI_APPLICATION = 'system_manager.wsgi.application'
#
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]
#
#
# # Internationalization
# # https://docs.djangoproject.com/en/4.2/topics/i18n/
#
# LANGUAGE_CODE = 'es'
#
# TIME_ZONE = 'America/Santiago'
#
# USE_I18N = True
#
# USE_TZ = True
#
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#
# AUTH_USER_MODEL = 'user.User'
#
# REST_FRAMEWORK = {
#     # Use Django's standard `django.contrib.auth` permissions,
#     # or allow read-only access for unauthenticated users.
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#     ]
# }
#
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#
# # EMAIL_HOST = os.environ.get('EMAIL_HOST')
# # EMAIL_PORT = os.environ.get('EMAIL_PORT')
# # EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
# # EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
# # EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
# # DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
# # EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL')
#
