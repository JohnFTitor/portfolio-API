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
    live_url = serializers.CharField(required=False, allow_blank=True)
    source_url = serializers.CharField(required=False, allow_blank=True)
    demo_url = serializers.CharField(required=False, allow_blank=True)

    tags = TagSerializer(many=True, read_only=True)

    # Write fields
    tag_names = serializers.ListField(
        child=serializers.CharField(allow_blank=True),
        write_only=True,
        required=False,
    )

    def _set_tags(
        self,
        project: models.Project,
        tag_names: list[str],
    ):
        existing_tags = models.Tag.objects.filter(
            name__in=tag_names,
        )

        existing_names = existing_tags.values_list(
            'name',
            flat=True,
        )

        new_tags = [
            models.Tag(
                name=tag,
            ) for tag in tag_names 
            if tag not in existing_names
        ]

        new_tags = models.Tag.objects.bulk_create(new_tags)

        tags_to_add = [
            *existing_tags,
            *new_tags,
        ]

        project.tags.set(tags_to_add)

        return project


    def create(self, validated_data):
        tag_names = validated_data.pop('tag_names', [])

        project = super().create(validated_data)

        return self._set_tags(project, tag_names)
    
    def update(self, instance, validated_data):
        tag_names = validated_data.pop('tag_names', [])

        project = super().update(instance, validated_data)

        return self._set_tags(project, tag_names)

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
            'tag_names',
        ]
