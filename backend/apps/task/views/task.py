from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from apps.task.models import Task
from apps.task.serializers.task import TaskSerializer
from apps.task.views.filters import TaskFilter

class TaskPagination(PageNumberPagination):
    # e.g. ?page=2&page_size=10
    page_size = 5
    page_size_query_param = "page_size"  # e.g. ?page_size=20
    max_page_size = 50

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter
    pagination_class = TaskPagination

    def get_queryset(self):
        qs = Task.objects.select_related("status")

        if self.request.user.is_staff:
            return qs.order_by("-created_at")

        return qs.filter(user=self.request.user).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
