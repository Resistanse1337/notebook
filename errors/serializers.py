from rest_framework import serializers, status
from rest_framework.exceptions import APIException

from .api_errors import BaseAPIError, InvalidCredentials, PasswordsDoesNotMatch, UserLoginError


def get_error_enum_and_response_serializer(
    init_api_errors: list[type[APIException]], http_code: int
) -> tuple[type, serializers.Serializer]:
    """Creates enum and serializer for ERROR_SCHEMAS based on input APIExceptions"""

    choices = [e.default_code for e in init_api_errors]

    error_enum = type(f"ErrorCode{http_code}Enum", (object,), dict(choices=choices))
    error_enum.choices = choices

    internal_serializer = type(
        f"InitialSerializer{http_code}",
        (serializers.Serializer,),
        dict(
            code=serializers.ChoiceField(choices=choices),
            detail=serializers.CharField(default="detail"),
            attr=serializers.CharField(default="attribute"),
        ),
    )
    error_serializer = type(
        f"ErrorSerializer{http_code}",
        (serializers.Serializer,),
        dict(errors=internal_serializer(many=True)),
    )
    return error_enum, error_serializer


error400response_enum, error400response_serializer = get_error_enum_and_response_serializer(
    [PasswordsDoesNotMatch, UserLoginError], status.HTTP_400_BAD_REQUEST,
)

error403response_enum, error403response_serializer = get_error_enum_and_response_serializer(
    [InvalidCredentials], status.HTTP_403_FORBIDDEN,
)

error500response_enum, error500response_serializer = get_error_enum_and_response_serializer(
    [BaseAPIError], status.HTTP_500_INTERNAL_SERVER_ERROR,
)
