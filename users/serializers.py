# users/serializers.py
from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "emp_id",
            "department",
            "first_name",
            "last_name",
            "zone",
            "sub_position",
        )
