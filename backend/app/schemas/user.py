from pydantic import BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber


class UserResponse(BaseModel):
    username: str
    email: str
    is_active: bool
    phone_number: PhoneNumber | None = None
    first_name: str | None = None
    last_name: str | None = None

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    phone_number: PhoneNumber | None = None
    first_name: str | None = None
    last_name: str | None = None


class CurrentUserRead(BaseModel):
    id: str | None = None
