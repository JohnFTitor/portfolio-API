from django.test import TestCase
from django.urls import reverse as url_reverse
from rest_framework import status
import factory
from knox.models import AuthToken


class TestGetProjects(TestCase):
    def setUp(self):
        self.url = url_reverse('projects')

    def test_200_get_projects(self):
        pass
