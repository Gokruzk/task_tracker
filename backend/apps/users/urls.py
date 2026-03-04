from rest_framework.routers import DefaultRouter
from apps.users.views import UserViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"users", UserViewSet, basename="users")

urlpatterns = router.urls
