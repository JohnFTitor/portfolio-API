
from django.urls import path
from .views import ListCreateProjectView


urlpatterns = [
    path(
      '',
      ListCreateProjectView.as_view(),
      name='projects',
    ),
]
