from database.db import db
from datetime import datetime

class Follower (db.Model):

    __tablename__ = "follower"
    __table_args__ = (
        db.PrimaryKeyConstraint('user_from_id', 'user_to_id'),
        {'extend_existing': True}
    )

    user_from_id = db.Column(db.Integer, db.ForeignKey('user.id'),primary_Key=True)
    user_to_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_Key=True)
  
  #Relations
    follower= db.relationship('User',foreign_keys=[user_from_id], back_populates='following')
    following=db.relationship('User',foreign_keys=[user_to_id],back_populates='followers')

    def serialize(self):
        return {
        "user_from_id":self.user_from_id,
        "user_to_id":self.user_to_id,
        }
