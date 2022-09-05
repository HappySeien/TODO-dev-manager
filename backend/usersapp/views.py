from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.pagination import LimitOffsetPagination

from .models import User
from . serializers import UserModelSerializer, UserModelSerializerV02


class UserLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class UserModelViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin
):
    queryset = User.objects.filter(is_active=True)
    # serializer_class = UserModelSerializer
    pagination_class = UserLimitOffsetPagination

    def get_serializer_class(self):
        if self.request.version == '0.2':
            return UserModelSerializerV02
        return UserModelSerializer

    