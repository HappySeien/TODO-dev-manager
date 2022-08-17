from rest_framework.viewsets import ModelViewSet

from .models import ToDo_noteModel, ProjectModel
from .serializers import NotesModelSerializer, ProjectModelSerializer
from .filters import ProjectModelFilter, ToDo_noteModelFlter
from rest_framework.pagination import LimitOffsetPagination


class NotneLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class NotesModelViewSet(ModelViewSet):
    queryset = ToDo_noteModel.non_delete_objects.all()
    serializer_class = NotesModelSerializer
    pagination_class = NotneLimitOffsetPagination
    filterset_class = ToDo_noteModelFlter

    def perform_destroy(self, instance):
        instance.closed = True
        instance.deleted = True
        instance.save()


class ProjectModelViewSet(ModelViewSet):
    queryset = ProjectModel.non_delete_objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectModelFilter
