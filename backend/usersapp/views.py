from rest_framework.viewsets import ModelViewSet

from .models import User
from . serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer
    