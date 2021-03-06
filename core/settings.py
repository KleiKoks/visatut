import os
import posixpath
from decouple import config
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = [
    '*',
]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'project',
    'project.blog',
    'project.service',
    'project.vacancy',
    'project.feedback',
    'tinymce',
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

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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


if DEBUG == True:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
if DEBUG == False:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('NAME'),
        'USER': config('USER'),
        'PASSWORD': config('PASSWORD'),
        'HOST': config('HOST'),
        'PORT': '5432'
        }
    }
    
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


LANGUAGE_CODE = 'uk'
LANGUAGES = (
    ("uk","uk"),
    ("ru","ru"),
    ("en","en"),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR,  "media")
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')




EMAIL_USE_TLS          = True
EMAIL_USE_SSL          = False
EMAIL_PORT             = 587
EMAIL_HOST             = "mail.starwayua.com"
EMAIL_HOST_USER        = "dev@starwayua.com"
EMAIL_HOST_PASSWORD    = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL     = EMAIL_HOST_USER




STATIC_SITEMAP_PAGES = [
    'index',
    'franchise',
    'partner_europe',
    'partner_potential',
    'partner_usa',
    'search_service',
    'blog_all'
]



TINYMCE_DEFAULT_CONFIG = {
  'height': 360,
  # 'width': 920,
  'width': 'auto',
  # 'cleanup_on_startup': True,
  'cleanup_on_startup': False,
  'custom_undo_redo_levels': 20,
  'selector': 'textarea',
  'theme': 'modern',
  'plugins': '''
    textcolor save link image media preview codesample contextmenu
    table code lists fullscreen  insertdatetime  nonbreaking
    contextmenu directionality searchreplace wordcount visualblocks
    visualchars code fullscreen autolink lists  charmap print  hr
    anchor pagebreak
    ''',
  'toolbar1': '''
    fullscreen preview bold italic underline | formatselect fontselect,
    fontsizeselect  | forecolor backcolor | alignleft alignright |
    aligncenter alignjustify | indent outdent | bullist numlist table |
    | link image media | codesample |
    ''',
  'toolbar2': '''
    visualblocks visualchars |
    charmap hr pagebreak nonbreaking anchor |  code |
    ''',
  'contextmenu': 'formats | link image',
  'menubar': True,
  'statusbar': True,
  'inline': False,

}
SITE_ID = 1 
#django-toolbar


