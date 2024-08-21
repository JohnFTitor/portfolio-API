from django.db import models

class User(models.Model):
  id = models.UUIDField(primary_key=True)
  email = models.EmailField(unique=True, null=True)
  username = models.CharField(unique=True, null=True, max_length=150)
