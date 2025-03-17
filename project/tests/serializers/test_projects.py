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

class ProjectCreateSerializer(TestCase):

  def test_project_creates_correctly(self):
    serialized_project = ProjectSerializer(
      data={
        'name': 'My new project',
        'description': 'Description',
        'live_url': '',
        'source_url': 'test',
        'demo_url': 'Test'
      }
    )

    assert serialized_project.is_valid(raise_exception=True)

    project = serialized_project.save()

    assert project.name == 'My new project'
    assert project.description == 'Description'
    assert project.live_url == ''
    assert project.source_url == 'test'
    assert project.demo_url == 'Test'

  def test_project_creates_with_tags(self):
    new_project = ProjectSerializer(
      data={
        'name': 'My new project',
        'description': 'Description',
        'tag_names': ['First', 'Second', 'Third']
      }
    )

    assert new_project.is_valid(raise_exception=True)

    project = new_project.save()

    assert project.tags.count() == 3

  def test_project_creates_with_tags_does_not_duplicate(self):
    factory.tag(
      name='First',
      save=True,
    )

    new_project = ProjectSerializer(
      data={
        'name': 'My new project',
        'description': 'Description',
        'tag_names': ['First', 'Second', 'Third']
      }
    )

    assert new_project.is_valid(raise_exception=True)

    project = new_project.save()

    assert project.tags.count() == 3

    assert Tag.objects.count() == 3
