# users/serializers.py
from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "emp_id",
            "email",
            "password",
            "department",
            "first_name",
            "last_name",
            "zone",
            "sub_position",
        )

    def create(self, validated_data):
        __import__("pprint").pprint(validated_data)
        return get_user_model().objects.create_user(**validated_data)


class UserDisplaySerializer(serializers.ModelSerializer):
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
