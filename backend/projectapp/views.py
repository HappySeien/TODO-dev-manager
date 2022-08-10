from rest_framework.viewsets import ModelViewSet

from .models import ToDo_noteModel, ProjectModel
from .serializers import NotesModelSerializer, FastNotesSerializer, ProjectModelSerializer, FastProjectSerializer


class NotesModelViewSet(ModelViewSet):
    queryset = ToDo_noteModel.non_delete_objects.all()
    serializer_class = NotesModelSerializer


class FastNotesModelViewSet(ModelViewSet):
    queryset = ToDo_noteModel.non_delete_objects.all()
    serializer_class = FastNotesSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = ProjectModel.non_delete_objects.all()
    serializer_class = ProjectModelSerializer


class FastProjectModelViewSet(ModelViewSet):
    queryset = ProjectModel.non_delete_objects.all()
    serializer_class = FastProjectSerializer
