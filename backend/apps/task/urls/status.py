from rest_framework.routers import DefaultRouter
from apps.task.views.status import TaskStatusViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"status", TaskStatusViewSet, basename="status")

urlpatterns = router.urls
