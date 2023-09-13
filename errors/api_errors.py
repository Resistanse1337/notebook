from unittest.mock import Base

from rest_framework import status
from rest_framework.exceptions import APIException


class BaseAPIError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "Something went wrong"
    default_code = "SOMETHING_WENT_WRONG"


class PasswordsDoesNotMatch(BaseAPIError):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Passwords does not match"
    default_code = "PASSWORDS_DOES_NOT_MATCH"


class UserLoginError(BaseAPIError):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Login error"
    default_code = "LOGIN_ERROR"


class InvalidCredentials(BaseAPIError):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "invalid credentials"
    default_code = "INVALID_CREDENTIALS"
