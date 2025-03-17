from django.test import TestCase
from django.urls import reverse as url_reverse
from rest_framework import status
from project.tests import factory
from project.tests.serializers.mock_serializers import serialize_project


class TestGetProjects(TestCase):
    def setUp(self):
        self.url = url_reverse('projects')

    def test_200_get_projects(self):
        projects = [
            factory.project(
                name=f'Project {i}',
            ) for i in range(10)
        ]

        response = self.client.get(
            self.url,
        )

        assert response.status_code == status.HTTP_200_OK
        
        for project, expected_project in zip(
            response.data,
            projects,
        ):
            self.assertEqual(
                project,
                serialize_project(expected_project)
            )


