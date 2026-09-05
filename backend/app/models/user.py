from uuid import UUID, uuid4

from sqlalchemy import UUID as PG_UUID
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
    is_active: Mapped[bool] = mapped_column(default=True)

    def __repr__(self) -> str:
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"
