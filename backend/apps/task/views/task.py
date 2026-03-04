from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.task.models import Task
from apps.task.serializers.task import TaskSerializer
from apps.task.views.filters import TaskFilter


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter

    def get_queryset(self):
        qs = Task.objects.select_related("status")

        if self.request.user.is_staff:
            return qs.order_by("-created_at")

        return qs.filter(user=self.request.user).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
