from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase

from mixer.backend.django import mixer

from .models import User
from .views import UserModelViewSet


# Create your tests here.

class SmokeUserTestCase(TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def test_get_users_list(self) -> None:
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_detail(self) -> None:
        pass


class CRUDUserTestCase():
    pass
