from rest_framework.viewsets import ModelViewSet

from .models import ToDo_noteModel, ProjectModel
from .serializers import NotesModelSerializer, ProjectModelSerializer


class NotesModelViewSet(ModelViewSet):
    queryset = ToDo_noteModel.non_delete_objects.all()
    serializer_class = NotesModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = ProjectModel.non_delete_objects.all()
    serializer_class = ProjectModelSerializer
