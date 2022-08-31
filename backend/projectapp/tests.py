from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, APITestCase

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
        view = ProjectModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_project_detail(self) -> None:
        client = APIClient()
        response = client.get(f'/api/projects/{self.project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CRUDTestCase(APITestCase):
    
    def setUp(self) -> None:
        self.admin = User.objects.create_superuser('admin', 'admin@admin.com', '123456')
        self.project = mixer.blend(ProjectModel)
        self.note = mixer.blend(ToDo_noteModel)

    def test_create_project_guest(self) -> None:
        response = self.client.post(f'/api/projects/', {
            'name': 'somethingCreate',
            'author': self.admin.id,
            'developers': [self.admin.id]
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_project_auth(self) -> None:
        self.client.force_login(self.admin)
        response = self.client.post(f'/api/projects/', {
            'name': 'somethingCreate',
            'author': self.admin.id,
            'developers': [self.admin.id]
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        project = ProjectModel.objects.get(id=response.data.get('id'))
        self.assertEqual(project.name, 'somethingCreate')
        self.client.logout()

    def test_create_note_guest(self) -> None:
        response = self.client.post(f'/api/notes/', {
            'title': 'somethingCreate', 
            'discroption': 'Testing', 
            'project': self.project.id,
            'author': self.admin.id
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_note_auth(self) -> None:
        self.client.force_login(self.admin)
        response = self.client.post(f'/api/notes/', {
            'title': 'somethingCreate', 
            'discroption': 'Testing', 
            'project': self.project.id,
            'author': self.admin.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        note = ToDo_noteModel.objects.get(id=response.data.get('id'))
        self.assertEqual(note.title, 'somethingCreate')
        self.client.logout()

    def test_update_project_guest(self) -> None:
        response = self.client.put(f'/api/projects/{self.project.id}/', {'name': 'something'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_project_auth(self) -> None:
        self.client.force_login(self.admin)
        response = self.client.put(f'/api/projects/{self.project.id}/', {
            'name': 'something',
            'author': self.admin.id,
            'developers': [self.admin.id]
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project = ProjectModel.objects.get(id=self.project.id)
        self.assertEqual(project.name, 'something')
        self.client.logout()

    def test_update_note_guest(self) -> None:
        response = self.client.put(f'/api/notes/{self.note.id}/', {'title': 'something'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_note_auth(self) -> None:
        self.client.force_login(self.admin)
        response = self.client.put(f'/api/notes/{self.note.id}/', {
            'title': 'something', 
            'discroption': 'Testing', 
            'project': self.project.id,
            'author': self.admin.id
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        note = ToDo_noteModel.objects.get(id=self.note.id)
        self.assertEqual(note.title, 'something')
        self.client.logout()

    def test_delete_project_guest(self) -> None:
        response = self.client.delete(f'/api/projects/{self.project.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_project_auth(self) -> None:
        self.client.force_login(self.admin)
        response = self.client.delete(f'/api/projects/{self.project.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.client.logout()

    def test_delete_note_guest(self) -> None:
        response = self.client.delete(f'/api/notes/{self.note.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_note_auth(self) -> None:
        self.client.force_login(self.admin)
        response = self.client.delete(f'/api/notes/{self.note.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.client.logout()
