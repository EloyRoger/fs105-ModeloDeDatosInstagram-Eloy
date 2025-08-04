from typing import List, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from src.database.db import db

if TYPE_CHECKING:
    from src.models.Follower import Follower
    from src.models.Post import Post
    from src.models.Comment import Comment

class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=True)
    firstname: Mapped[str] = mapped_column(String(50), nullable=False)
    lastname: Mapped[str] = mapped_column(String(50), nullable=False)

    posts: Mapped[List["Post"]] = relationship("Post", back_populates="user")
    comments: Mapped[List["Comment"]] = relationship("Comment", back_populates="author")

    # Relaciones con la tabla follower a través del modelo Follower
    followers_assoc: Mapped[List["Follower"]] = relationship(
        "Follower",
        foreign_keys="[Follower.user_to_id]",
        back_populates="user_to",
        lazy="dynamic"
    )

    following_assoc: Mapped[List["Follower"]] = relationship(
        "Follower",
        foreign_keys="[Follower.user_from_id]",
        back_populates="user_from",
        lazy="dynamic"
    )

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
        }
