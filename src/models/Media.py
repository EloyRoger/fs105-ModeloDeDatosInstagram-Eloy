from database.db import db
from datetime import datetime

class Media (db.Model):

    __tablename__ = "media"

    id= db.column(primary_key=True)
    type= db.column(db.String(50), nullable=False)
    url= db.column(db.String(50), nullable=False)
    post_id= db.column(db.Foreign_key('post.id'))
   
   #Relations
    post = db.relationship('Post', back_populates='media')

def serialize(self):
        return {
            "id": self.id,
            "type": self.type,
            "url": self.url,
            "post_id": self.post_id,
        }
