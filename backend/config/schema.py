from pydoc import resolve
import graphene
from graphene_django import DjangoObjectType

from usersapp.models import User
from projectapp.models import ProjectModel, ToDo_noteModel


class UserObjectType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'date_of_birth', 'email', 'project_author', 'project_developers')


class ProjectObjectType(DjangoObjectType):
    class Meta:
        model = ProjectModel
        fields = '__all__'


class ToDo_noteObjectType(DjangoObjectType):
    class Meta:
        model = ToDo_noteModel
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(UserObjectType)
    user_filter_by_name_contains = graphene.List(
        UserObjectType, 
        username=graphene.String(required=False),
        first_name=graphene.String(required=False),
        last_name=graphene.String(required=False)
    )
    get_user_by_id = graphene.Field(UserObjectType, pk=graphene.Int(required=True))

    all_projects = graphene.List(ProjectObjectType)
    project_filter_by_name_contains = graphene.List(ProjectObjectType, name=graphene.String(required=True))
    project_info = graphene.Field(ProjectObjectType, pk=graphene.Int(required=True))

    all_notes = graphene.List(ToDo_noteObjectType)
    get_note_by_id = graphene.Field(ToDo_noteObjectType, pk=graphene.Int(required=True))

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_user_filter_by_name_contains(
        root, info, username=None, first_name=None, last_name=None
    ):
        user=None
        if username:
            user = User.objects.filter(username__contains=username)
        if first_name:
             user = User.objects.filter(first_name__contains=first_name)
        if last_name:
            user = User.objects.filter(last_name__contains=last_name)
        if username or first_name or last_name:
            return user
        return user

    def resolve_get_user_by_id(root, info, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None

    def resolve_all_projects(root, info):
        return ProjectModel.objects.all()

    def resolve_project_filter_by_name_contains(root, info, name):
        return ProjectModel.objects.filter(name__contains=name)

    def resolve_project_info(root, info, pk):
        try:
            return ProjectModel.objects.get(pk=pk)
        except ProjectModel.DoesNotExist:
            return None

    def resolve_all_notes(root, info):
        return ToDo_noteModel.objects.all()

    def resolve_get_note_by_id(root, info, pk):
        try:
            return ToDo_noteModel.objects.get(pk=pk)
        except ToDo_noteModel.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
