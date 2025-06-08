from database.db import db
from datetime import datetime

class User (db.Model):

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50),unique=True, nullable=False)
    email = db.Column(db.String(50),unique=True)
    firstname= db.Column(db.String(50),nullable=False)
    lastname= db.Column(db.String(50),nullable=False)

#Relations
    posts = db.relationship("Post", back_populates="user")
    comments = db.relationship("Comment", back_populates="author")

    followers = db.relationship(
        'User',
        secondary='follower',
        primaryjoin='User.id == Follower.user_to_id',
        secondaryjoin='User.id == Follower.user_from_id',
        backref=db.backref('following', lazy='dynamic'),
        lazy='dynamic'
    )

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
        }