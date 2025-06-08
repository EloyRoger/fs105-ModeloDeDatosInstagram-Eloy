from database.db import db


class Comment (db.Model):

    __tablename__ = "comment"


    id = db.Column(db.Integer, primary_key =True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user-id'))
    comment_text= db.Column(db.String(250), nullable=False)

#Relations
    user = db.relationship("User", back_populates="comments")
    post = db.relationship("Post", back_populates="comments")

    def serialize(self):
        return {
            "id": self.id,
            "comment_text": self.comment_id,
            "post_id": self.post_id,
            "user_id": self.user_id,
            "content": self.content,
        }
     

