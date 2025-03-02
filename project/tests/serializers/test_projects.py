from project.serializers import ProjectSerializer
from project.tests import factory
from django.test import TestCase
from project.tests.serializers.mock_serializers import serialize_project
from project.models import Tag

class ProjectRenderSerializer(TestCase):

  def test_project_serializes_correctly(self):
    project = factory.project(
      name='Testing project',
      save=True,
    )

    tags = Tag.objects.bulk_create([
      factory.tag(
        name=f"{index} Tag",
      ) for index in range(5)
    ])
    
    project.tags.set(tags)

    serialized_project = ProjectSerializer(
      instance=project,
    )

    self.assertEqual(
      serialize_project(project),
      serialized_project.data,
    )
