from django.db import transaction
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from errors.api_errors import PasswordsDoesNotMatch
from users.models import User


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, required=True)
    password = serializers.CharField(max_length=255, required=True, write_only=True)


class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "password_confirm",
        ]
        extra_kwargs = {
            "email": {
                "required": True,
                "validators": [UniqueValidator(queryset=User.objects.all())],
            },
            "password": {"write_only": True, "validators": [validate_password]},
        }

    def validate(self, data):
        if data.get("password") != data.get("password_confirm"):
            raise PasswordsDoesNotMatch

        return super().validate(data)

    def create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create(
                first_name=validated_data["first_name"],
                last_name=validated_data["last_name"],
                username=validated_data["username"],
                email=validated_data["email"],
            )

            user.set_password(validated_data["password"])
            user.save()

            return user
