from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.pagination import LimitOffsetPagination

from .models import User
from . serializers import UserModelSerializer


class UserLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class UserModelViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin
):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer
    pagination_class = UserLimitOffsetPagination
    