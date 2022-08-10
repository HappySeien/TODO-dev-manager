from rest_framework import serializers

from .models import ToDo_noteModel, ProjectModel
from usersapp.serializers import FastUserSerializer


class NotesModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDo_noteModel
        fields = '__all__'


class FastNotesSerializer(serializers.ModelSerializer):
    author = FastUserSerializer()
    class Meta:
        model = ToDo_noteModel
        exclude = ['deleted']


class ProjectModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectModel
        exclude = ['deleted']


class FastProjectSerializer(serializers.ModelSerializer):
    author = FastUserSerializer()
    developers = FastUserSerializer(many=True)
    class Meta:
        model = ProjectModel
        exclude = ['deleted']
