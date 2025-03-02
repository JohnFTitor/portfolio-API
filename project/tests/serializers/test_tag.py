from project.serializers import TagSerializer
from project.tests import factory
from django.test import TestCase
from .mock_serializers import serialize_tag


class TestTagRender(TestCase):

    def test_tag_serializes_correctly(self):
        tag = factory.tag(save=True)

        serialized_tag = TagSerializer(
            instance=tag,
        )

        self.assertEqual(
            serialize_tag(tag),
            serialized_tag.data,
        )
