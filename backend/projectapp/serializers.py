from rest_framework import serializers

from .models import ToDo_noteModel, ProjectModel


class NotesModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDo_noteModel
        fields = '__all__'


class ProjectModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectModel
        fields = '__all__'
