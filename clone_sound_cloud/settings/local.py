
import os
from .base import *


SECRET_KEY = '$cwa(@@5qvs^6fb6@^x%fs%ed5x6_j4!os#6%d3t(hj85soimy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition




# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'soundcloud_db',
        'USER': 'soundcloud',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
STATICFILES_DIRS = [os.path.join(os.getcwd(), 'static')]

