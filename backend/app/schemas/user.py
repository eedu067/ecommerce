from pydantic import BaseModel, ConfigDict


class UserResponse(BaseModel):
    username: str
    email: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class CurrentUserRead(BaseModel):
    id: str | None = None
