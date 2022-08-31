from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase

from mixer.backend.django import mixer

from usersapp.models import User
from .models import ProjectModel, ToDo_noteModel
from .views import NotesModelViewSet, ProjectModelViewSet


# Create your tests here.
class SmokeProjectTestCase(TestCase):

    def setUp(self) -> None:
        self.user = mixer.blend(User)
        self.project = mixer.blend(ProjectModel)
        self.note = mixer.blend(ToDo_noteModel)

    def test_get_notes_list(self) -> None:
        factory = APIRequestFactory()
        request = factory.get('/api/notes/')
        view = NotesModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_note_detail(self) -> None:
        client = APIClient()
        response = client.get(f'/api/notes/{self.note.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_project_list(self) -> None:
        factory = APIRequestFactory()
        request = factory.get('/api/projects/')
        view = NotesModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_project_detail(self) -> None:
        client = APIClient()
        response = client.get(f'/api/projects/{self.project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CRUDTestCase(APITestCase):
    
    def setUp(self) -> None:
        self.user = mixer.blend(User)
        self.project = mixer.blend(ProjectModel)
        self.note = mixer.blend(ToDo_noteModel)

    def test_create_project_guest(self) -> None:
        pass

    def test_create_project_auth(self) -> None:
        pass

    def test_create_note_guest(self) -> None:
        pass

    def test_create_note_auth(self) -> None:
        pass

    def test_update_project_guest(self) -> None:
        pass

    def test_update_project_auth(self) -> None:
        pass

    def test_update_note_guest(self) -> None:
        pass

    def test_update_note_auth(self) -> None:
        pass

    def test_delete_project_guest(self) -> None:
        pass

    def test_delete_project_auth(self) -> None:
        pass

    def test_delete_note_guest(self) -> None:
        pass

    def test_delete_note_auth(self) -> None:
        pass
