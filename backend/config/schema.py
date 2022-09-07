from pydoc import resolve
import graphene
from graphene_django import DjangoObjectType

from usersapp.models import User
from projectapp.models import ProjectModel, ToDo_noteModel


class UserObjectType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'date_of_birth', 'email')


class ProjectObjectType(DjangoObjectType):
    class Meta:
        model = ProjectModel
        fields = '__all__'


class ToDo_noteObjectType(DjangoObjectType):
    class Meta:
        model = ToDo_noteModel
        fields = '__all__'


class Query(graphene.ObjectType):
    project_info = graphene.Field(ProjectObjectType, pk=graphene.Int(required=True))

    def resolve_project_info(root, info, pk):
        try:
            return ProjectModel.objects.get(pk=pk)
        except ProjectModel.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)