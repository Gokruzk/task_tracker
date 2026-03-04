# apps/users/tests/test_users.py
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from apps.users.models import User


class UserAPITest(APITestCase):
    def test_register_user(self):
        url = reverse("register")  # Ajusta según tu URLConf
        data = {"username": "nuevo", "password": "1234"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, "nuevo")
