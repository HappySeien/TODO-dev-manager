from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import User


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'first_name', 'last_name', 'date_of_birth', 'email')


class FastUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
        