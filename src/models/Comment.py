from database.db import db

class Comment (db.Model):

    __tablename__ = "Comment"

    CommentID = db.Column(db.Integer, primary_key =True)
    PostID = db.Column(db.Integer)
    UserID = db.Column(db.Integer)
    Content = db.Column(db.String)
    CreatedAt = db.Column(db.String)

    def serialize(self):
        return {
       
        }
     

