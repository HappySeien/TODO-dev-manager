from django.db import models

from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class BaseManager(models.Manager):
    """
    Базовая настройка менеджера моделей
    """

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)



class BaseModel(models.Model):
    """
    Базовая модель
    """

    objects = models.Manager() # The default manager.
    non_delete_objects = BaseManager()

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'), editable=False)
    updated_at =models.DateTimeField(auto_now=True, verbose_name=_('Updated at'), editable=False)
    deleted = models.BooleanField(default=False, verbose_name=_('Deleted'))

    def delete(self, *args) -> None:
        self.deleted = True
        self.save()


    class Meta:
        abstract = True
