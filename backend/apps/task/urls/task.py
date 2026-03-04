from rest_framework.routers import DefaultRouter
from apps.task.views.task import TaskViewSet

router = DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="tasks")

urlpatterns = router.urls
