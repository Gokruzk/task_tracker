from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.task.models import TaskStatus
from apps.task.serializers import TaskStatusSerializer


class TaskStatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TaskStatus.objects.all().order_by("code")
    serializer_class = TaskStatusSerializer
    permission_classes = [IsAuthenticated]
