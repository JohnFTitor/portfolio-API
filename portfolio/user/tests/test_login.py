from django.test import TestCase
from django.urls import reverse as url_reverse

class TestLoginView(TestCase):
  def setUp(self):
    self.url = url_reverse('user_login')

  def test_400_error_wrong_credentials(self):
    pass
