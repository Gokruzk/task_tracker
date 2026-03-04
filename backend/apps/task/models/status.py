import uuid
from django.db import models


class TaskStatus(models.Model):
    class Codes(models.TextChoices):
        PENDING = "PENDING", "Pending"
        IN_PROGRESS = "IN_PROGRESS", "In Progress"
        COMPLETED = "COMPLETED", "Completed"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    code = models.CharField(
        max_length=20,
        choices=Codes.choices,
        unique=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "task_status"

    def __str__(self):
        return self.code
