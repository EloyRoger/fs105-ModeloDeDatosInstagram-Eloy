from database.db import db


class Follow (db.Model):

    __tablename__ = "Follow"

    FollowID = db.Column(db.Integer, primary_key=True)
    FollowerUserID = db.Column(db.Integer)
    FollowingUserID = db.Column(db.Integer)
    CreatedAt = db.Column(db.Integer)

    def serialize(self):
        return {
            "FollowID": self.FollowID,
            "FollowUserID": self.FollowerUserID,
            "FollowingUserID": self.FollowingUserID,
            "CreatedAt": self.Created,
        }
