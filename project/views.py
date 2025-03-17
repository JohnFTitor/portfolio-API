from rest_framework.generics import ListCreateAPIView
from project.serializers import ProjectSerializer
from .models import Project

class ListCreateProjectView(ListCreateAPIView):
  serializer_class = ProjectSerializer

  def get_queryset(self):
    return Project.objects.prefetch_related(
      'tags',
    )
