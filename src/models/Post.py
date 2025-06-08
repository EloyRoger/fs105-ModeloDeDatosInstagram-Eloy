from database.db import db
from datetime import datetime

class Post (db.Model):

    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    
    #Relations
    user= db.relationship ("User", back_populates="post")
    comments= db.relationship ("Comment", back_populates="post")
    media= db.relationship ("Media", back_populates="post")

    def serialize(self):
        return {
            "id": self.id,
            "post": self.post,
        }

