from database.db import db


class Post (db.Model):

    __tablename__ = "Post"

    UserID = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(250), unique=True, nullable=False)
    Email = db.Column(db.String(50), unique=True)
    PasswordHash = db.Column(db.String(50))
    CreatedAt = db.Column(db.Integer)


    def serialize(self):
        return {
            "UserID": self.id,
            "Username": self.Username,
            "Email": self.Email,
            "PasswordHash": self.PasswordHash,
            "CreatedAt": self.CreatedAt,
        }

