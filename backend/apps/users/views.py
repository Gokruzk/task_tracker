from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.users.models import User
from apps.users.serializers import UserSerializer, UserCreateSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return User.objects.all()
        return User.objects.filter(id=self.request.user.id)

    @action(detail=False, methods=["get", "put", "patch"])
    def me(self, request):
        user = request.user

        if request.method in ["PUT", "PATCH"]:
            serializer = self.get_serializer(
                user,
                data=request.data,
                partial=(
                    request.method == "PATCH"
                ),
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        serializer = self.get_serializer(user)
        return Response(serializer.data)

class RegisterView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]