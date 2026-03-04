from rest_framework import serializers
from apps.task.models import Task
from apps.task.serializers.status import TaskStatusSerializer


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ["id", "created_at", "user"]

class TaskReadSerializer(TaskSerializer):
    status = TaskStatusSerializer(read_only=True)
