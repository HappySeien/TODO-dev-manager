from django_filters import rest_framework as filters
from .models import ProjectModel, ToDo_noteModel


class ProjectModelFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = ProjectModel
        fields = ['name']


class ToDo_noteModelFlter(filters.FilterSet):
    date_from = filters.DateFilter(field_name='created_at', lookup_expr='date__gte')
    date_to = filters.DateFilter(field_name='created_at', lookup_expr='date__lte')

    class Meta:
        model = ToDo_noteModel
        fields = ['project', 'date_from', 'date_to']
