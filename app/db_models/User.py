from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class User(Base):
    __tablename__ = 'Users'
    id: Mapped[int | None]
    name: Mapped[str] = mapped_column(primary_key=True, nullable=False, unique=True )

