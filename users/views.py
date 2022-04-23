# users/views.py
from django.contrib.auth import get_user_model

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
