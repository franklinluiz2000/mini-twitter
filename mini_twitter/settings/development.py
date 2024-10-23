from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Crie a secret key para seu ambiente de desenvolvimento
SECRET_KEY = 'django-insecure-y_h)^ly-q%cf90^3l3(af6cgb(w*9te8nq8sn3b2#3@o66dorm'

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}