import django_filters
from apps.task.models import Task


class TaskFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(field_name="status")

    created_after = django_filters.DateTimeFilter(
        field_name="created_at", lookup_expr="gte"
    )

    created_before = django_filters.DateTimeFilter(
        field_name="created_at", lookup_expr="lte"
    )

    class Meta:
        model = Task
        fields = ["status", "created_after", "created_before"]
