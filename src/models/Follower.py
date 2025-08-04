from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from src.database.db import db

if TYPE_CHECKING:
    from src.models.User import User

class Follower(db.Model):
    __tablename__ = "follower"

    user_from_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    user_to_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)

    user_from: Mapped["User"] = relationship("User", foreign_keys=[user_from_id], back_populates="following_assoc")
    user_to: Mapped["User"] = relationship("User", foreign_keys=[user_to_id], back_populates="followers_assoc")

    def serialize(self):
        return {
            "user_from_id": self.user_from_id,
            "user_to_id": self.user_to_id,
        }
