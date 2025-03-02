from django.db import models
import uuid
from django.utils import timezone

class UUIDModel(models.Model):
  id = models.UUIDField(
    primary_key=True,
    default=uuid.uuid4,
  )

  class Meta:
    abstract = True

class TimeStampModel(models.Model):
  created_at=models.DateTimeField(default=timezone.now)
  updated_at=models.DateTimeField(default=timezone.now)

  def save(self, *args, **kwargs):
    self.updated_at = timezone.now()

    return super().save(*args, **kwargs)
  
  class Meta:
    abstract = True
