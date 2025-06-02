from database.db import db


class Like (db.Model):

    __tablename__ = "like"

    LikeID = db.Column(db.Integer, primary_key=True)
    PostID = db.Column(db.String(50))
    UserID = db.Column(db.String(50))
    CreatedAt = db.Column(db.Integer)

    def serialize(self):
        return {
            "id": self.id,
            "PostID": self.PostID,
            "UserID": self.UserID,
            "CreatedAt": self.Created,
        }
