from django.contrib.auth.password_validation import validate_password
from django.template.loader import render_to_string
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from errors.api_errors import PasswordsDoesNotMatch
from users.models import User


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, required=True)
    password = serializers.CharField(
        max_length=255, required=True, write_only=True
    )


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
            "password": {
                "write_only": True, "validators": [validate_password]
            },
        }

    def validate(self, data):
        if data.get("password") != data.get("password_confirm"):
            raise PasswordsDoesNotMatch

        return super().validate(data)

    def create(self, validated_data):
        user = User.create_user(validated_data)

        text = render_to_string(
            "email/after_register.html",
            {"username": user.username}
        )
        user.send_mail("Message from notebook service", text)
        
        return user
