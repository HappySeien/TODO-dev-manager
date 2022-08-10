from django.contrib import admin

from baseapp.admin import BaseAdminSettings
from .models import ToDo_noteModel, ProjectModel


@admin.register(ProjectModel)
class UserAdmin(BaseAdminSettings):
    list_display = ['pk', 'author', 'name']
    list_filter = ['author', 'deleted']
    search_fields = ['author', 'name']



@admin.register(ToDo_noteModel)
class UserAdmin(BaseAdminSettings):
    list_display = ['pk', 'author','project', 'title', 'closed']
    list_filter = ['closed', 'deleted']
    search_fields = ['author', 'title']
