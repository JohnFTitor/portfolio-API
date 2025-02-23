from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "test_portfolio",
        "USER": "johnftitor",
        "PASSWORD": "localDev**",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
