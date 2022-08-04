from django.contrib import admin

from django.utils.translation import gettext_lazy as _


class BaseAdminSettings(admin.ModelAdmin):
    """
    Базовый функционал для моделей админки
    """
    list_per_page: int = 10
    actions = ['mark_deleted', 'mark_undeleted']

    def mark_deleted(self, request, queryset) -> None:
        queryset.update(deleted=True)

    mark_deleted.short_description = _('Mark as deleted')

    def mark_undeleted(self, request, queryset) -> None:
        queryset.update(deleted=False)

    mark_undeleted.short_description = _('Restore')
