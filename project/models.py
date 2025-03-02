from portfolio.abstract import UUIDModel, TimeStampModel
from django.db import models
from portfolio.user.models import User


class Tag(UUIDModel, TimeStampModel):
    name = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        unique=True,
    )


class Project(UUIDModel, TimeStampModel):
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='projects',
    )
    name = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    live_url = models.CharField(
        null=True,
        blank=True,
    )
    source_url = models.CharField(
        null=True,
        blank=True,
    )
    demo_url = models.CharField(
        null=True,
        blank=True,
    )
