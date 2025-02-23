from django.contrib.auth import models as auth_models
from django.db import models
from ..abstract import UUIDModel

class User(UUIDModel, auth_models.AbstractUser):
    is_admin = models.BooleanField(null=True, default=False)
