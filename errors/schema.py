from drf_standardized_errors.openapi import AutoSchema


class CustomAutoSchema(AutoSchema):
    def _should_add_error_response(self, responses: dict, status_code: str) -> bool:
        return True
