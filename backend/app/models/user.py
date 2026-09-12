from uuid import UUID, uuid4

from sqlalchemy import UUID as PG_UUID
from sqlalchemy import Unicode
from sqlalchemy.orm import Mapped, mapped_column

from core.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid4
    )
    username: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    phone_number: Mapped[str | None] = mapped_column(Unicode(30), nullable=True)
    first_name: Mapped[str | None] = mapped_column(Unicode(255), nullable=True)
    last_name: Mapped[str | None] = mapped_column(Unicode(255), nullable=True)
    is_active: Mapped[bool] = mapped_column(default=True)

    def __repr__(self) -> str:
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"
