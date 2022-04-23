# users/views.py
from django.contrib.auth import get_user_model

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from .serializers import UserSerializer, UserDisplaySerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "create":
            return [
                AllowAny(),
            ]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            self.serializer_class = UserDisplaySerializer
        return super().get_serializer_class()
