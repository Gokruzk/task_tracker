import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=120, unique=True, null=False, blank=False)
    password = models.CharField(max_length=128, null=False, blank=False)

    REQUIRED_FIELDS = ["password"]

    def __str__(self):
        return self.username
