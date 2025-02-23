from django.test import TestCase
from django.urls import reverse as url_reverse
from rest_framework import status
import factory

class TestLoginView(TestCase):
  def setUp(self):
    self.url = url_reverse('user_login')

  def test_400_error_wrong_credentials(self):
    user = factory.user(
      password='test',
      save=True,
    )

    response = self.client.post(
      self.url,
      data={
        'username': user.username,
        'password': 'wrong pass',
      },
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST

  def test_400_error_wrong_user(self):
    factory.user(
      password='test',
      save=True,
    )

    response = self.client.post(
      self.url,
      data={
        'username': 'random',
        'password': 'wrong pass',
      },
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST

  def test_200_with_good_credentials(self):
    user = factory.user(
      password='Test',
      save=True,
    )

    response = self.client.post(
      self.url,
      data={
        'username': user.username,
        'password': 'Test',
      }
    )

    assert response.status_code == status.HTTP_200_OK

    assert 'token' in response.data


