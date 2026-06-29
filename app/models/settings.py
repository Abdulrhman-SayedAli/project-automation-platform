from sqlalchemy import JSON, Index, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base, TimestampMixin, UUIDPrimaryKeyMixin


class Setting(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "settings"
    __table_args__ = (Index("ix_settings_key", "key", unique=True),)

    key: Mapped[str] = mapped_column(String(128), nullable=False)
    value: Mapped[dict] = mapped_column(JSON, nullable=False)

