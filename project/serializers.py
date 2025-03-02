from rest_framework import serializers
from project import models


class TagSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    name = serializers.CharField(required=True)

    class Meta:
        model = models.Tag
        fields = [
            'id',
            'name',
        ]


class ProjectSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex', read_only=True)

    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    live_url = serializers.CharField(required=True)
    source_url = serializers.CharField(required=True)
    demo_url = serializers.CharField(required=True)

    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = models.Project
        fields = [
            'id',
            'name',
            'description',
            'live_url',
            'source_url',
            'demo_url',
            'tags',
        ]
