from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from .models import User
from . serializers import UserModelSerializer


class UserModelViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin
):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer
    