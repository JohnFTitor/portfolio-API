from rest_framework import serializers
from project import models

class TagSerializer(serializers.ModelSerializer):
  id = serializers.UUIDField(read_only=True)
  name = serializers.CharField()

  class Meta:
    model = models.Tag
    fields = [
      'id',
      'name',
    ]
