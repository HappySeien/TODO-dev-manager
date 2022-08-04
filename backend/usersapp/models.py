from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from baseapp.models import NULLABLE
from usersapp.services.users_avatars_path import users_avatars_path


class User(AbstractUser):
    """
    Модель пользователя
    """

    email = models.EmailField(blank=True, unique=True, verbose_name=_('Email'))
    age = models.PositiveBigIntegerField(**NULLABLE, verbose_name=_('Age'))
    avatar = models.ImageField(upload_to=users_avatars_path, **NULLABLE)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
