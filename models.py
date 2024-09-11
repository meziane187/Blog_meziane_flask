
from sqlalchemy import (Integer,String,Text,DateTime,Boolean,Column,ForeignKey,UniqueConstraint)
from datetime import datetime
from slugify import slugify
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(Integer, primary_key=True)

    title = db.Column(db.String(100),nullable=False)
    slug = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
    is_active = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at=db.Column(db.DateTime)



    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.slug = slugify(self.title,remove=["&",":"],lowercase=False,separator="_")
    def __repr__(self):
        return f'<Post { self.title}>'




    def __repr__(self):
        return f'<{self.title}>'




