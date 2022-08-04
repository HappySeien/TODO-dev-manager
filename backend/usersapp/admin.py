from django.contrib import admin

from baseapp.admin import BaseAdminSettings
from .models import User


@admin.register(User)
class UserAdmin(BaseAdminSettings):
    list_display = ['pk', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['username', 'first_name', 'last_name', 'email']
