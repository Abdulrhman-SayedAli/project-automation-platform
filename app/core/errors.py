from pydantic import BaseModel


class AppError(Exception):
    def __init__(self, code: str, message: str, status_code: int = 400) -> None:
        self.code = code
        self.message = message
        self.status_code = status_code
        super().__init__(message)


class ErrorDetail(BaseModel):
    code: str
    message: str


class ErrorResponse(BaseModel):
    success: bool = False
    error: ErrorDetail

    @classmethod
    def from_error(cls, error: AppError) -> "ErrorResponse":
        return cls(error=ErrorDetail(code=error.code, message=error.message))

