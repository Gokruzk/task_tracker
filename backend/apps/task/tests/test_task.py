from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from apps.task.models.status import TaskStatus
from apps.users.models import User
from apps.task.models import Task


class TaskAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="1234")
        # Creating a second user to test isolation logic
        self.other_user = User.objects.create_user(username="other", password="1234")

        # Ensure the status exists (using get_or_create is safer in tests)
        self.status, _ = TaskStatus.objects.get_or_create(code="PENDING")

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.url = "/api/tasks"

    def test_create_task(self):
        data = {
            "title": "Mi tarea",
            "description": "Descripción de prueba",
            "status": self.status.id,  # DRF handles the ID directly
        }
        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Check that the task was assigned to the logged-in user (perform_create logic)
        task = Task.objects.get()
        self.assertEqual(task.user, self.user)
        self.assertEqual(task.title, "Mi tarea")

    def test_get_tasks_isolation(self):
        # Task for current user
        Task.objects.create(title="My Task", user=self.user, status=self.status)
        # Task for someone else
        Task.objects.create(
            title="Other Task", user=self.other_user, status=self.status
        )

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify get_queryset logic: only 1 task should return (the one belonging to self.user)
        data = response.json()
        self.assertIn("results", data)
        self.assertEqual(len(data["results"]), 1)
        self.assertEqual(data["count"], 1)
