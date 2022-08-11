from django.db import models
from baseapp.models import BaseModel, NULLABLE
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from usersapp.models import User


class ProjectModel(BaseModel):
    """
    Модель описывающая проект
    """
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='project_author', verbose_name=_('Author'))
    link_to_git = models.URLField(**NULLABLE, verbose_name=_('Link to git'))
    developers = models.ManyToManyField(User, related_name='project_developers', verbose_name=_('Developers'))
    name = models.CharField(verbose_name=_('Project name'), max_length=50)
    discroption = models.TextField(**NULLABLE, verbose_name=_('Discription'))
    

    def __str__(self) -> str:
        return f'{self.author} {self.name}'

    def delete(self, *args) -> None:
        return super().delete(*args)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'



class ToDo_noteModel(BaseModel):
    """
    Модель ToDo заметки к проекту
    """
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_('Author'))
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, related_name='project_notes', verbose_name=_('Project'))
    title = models.CharField(verbose_name=_('Title'), max_length=50)
    discroption = models.TextField(**NULLABLE, verbose_name=_('Discription'))
    closed = models.BooleanField(default=False, verbose_name=_('Closed note'))

    def __str__(self) -> str:
        return f'{self.author} {self.project} {self.title}'

    def delete(self, *args) -> None:
        return super().delete(*args)

    class Meta:
        verbose_name = 'ToDo note'
        verbose_name_plural = 'ToDo notes'
