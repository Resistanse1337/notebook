from drf_standardized_errors.formatter import ExceptionFormatter
from drf_standardized_errors.types import ErrorResponse


class CustomExceptionFormatter(ExceptionFormatter):
    def format_error_response(self, error_response: ErrorResponse) -> dict:
        response: dict = super().format_error_response(error_response)

        for error in response["errors"]:
            attr = error["attr"]
            code = error["code"]

            if attr and attr not in code:
                error["code"] += f"_{attr}"

        return response