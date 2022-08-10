from rest_framework.serializers import HyperlinkedModelSerializer
from .models import ToDo_noteModel, ProjectModel

class NotesModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ToDo_noteModel
        fields = '__all__'


class ProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ProjectModel
        fields = '__all__'