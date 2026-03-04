from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from apps.task.models import Task
from apps.task.views.filters import TaskFilter
from apps.task.serializers.task import TaskSerializer
from apps.core.ResponseManager import ResponsesManager


class TaskPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 50


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter
    pagination_class = TaskPagination

    def get_queryset(self):
        qs = Task.objects.select_related("status").order_by("-created_at")
        if not self.request.user.is_staff:
            qs = qs.filter(user=self.request.user)
        return qs

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(
                    ResponsesManager.success(
                        "successfully_retrieved", serializer.data
                    ).data
                )

            serializer = self.get_serializer(queryset, many=True)
            return ResponsesManager.success("successfully_retrieved", serializer.data)

        except Exception as e:
            print(e)
            return ResponsesManager.error("unexpected_error")

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except Exception as e:
            print(e)
            return ResponsesManager.error("unexpected_error")
