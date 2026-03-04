from rest_framework import serializers
from apps.task.models import TaskStatus


class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = ["id", "code", "created_at"]
        read_only_fields = ["id", "created_at"]
