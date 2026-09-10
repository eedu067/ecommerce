from fastapi import HTTPException, status


class CustomException(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail: str = "An error occurred",
    ) -> None:
        super().__init__(status_code=status_code, detail=detail)


class BadRequestException(CustomException):
    def __init__(self, detail: str = "Bad request") -> None:
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)


class NotFoundException(CustomException):
    def __init__(self, detail: str = "Resource not found") -> None:
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


class UnauthorizedException(CustomException):
    def __init__(self, detail: str = "Unauthorized") -> None:
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail)


class ForbiddenException(CustomException):
    def __init__(self, detail: str = "Forbidden") -> None:
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=detail)


class InternalServerErrorException(CustomException):
    def __init__(self, detail: str = "Internal server error") -> None:
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail
        )


class ConflictException(CustomException):
    def __init__(self, detail: str = "Conflict") -> None:
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail=detail)


class UnprocessableEntityException(CustomException):
    def __init__(self, detail: str = "Unprocessable entity") -> None:
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=detail
        )


class TooManyRequestsException(CustomException):
    def __init__(self, detail: str = "Too many requests") -> None:
        super().__init__(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail=detail)


class ServiceUnavailableException(CustomException):
    def __init__(self, detail: str = "Service unavailable") -> None:
        super().__init__(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=detail)


class DuplicateEntryException(CustomException):
    def __init__(self, detail: str = "Duplicate entry") -> None:
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail=detail)
