from rest_framework import serializers
from apps.task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "status",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]
