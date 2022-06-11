import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__="user"
    id = Column(Integer, primary_key = True)

    Follower = relationship("follower")
    follower_id = Column(Integer, ForeignKey("follower.id"))
    followed = relationship("followed")
    followed_id = Column(Integer, ForeignKey("followed.id"))
    post = relationship("post")
    post_id = Column(Integer, ForeignKey("post.id"))
    user = Column(String(50), nullable = False, unique = True)
    email = Column(String(50), nullable = False, unique = True)
    sub_date = Column(Date, nullable = False)
    last_name = Column(String(50), nullable = True)

class Follower(Base):
    __tablename__ = "follower"
    id = Column(Integer, primary_key = True)

class Followed(Base):
    __tablename__ = "followed"
    id = Column(Integer, primary_key = True)

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key = True)

    like = relationship("like")
    like_id = Column(Integer, ForeignKey("like.id"))
    comment = relationship("comment")
    comment_id = Column(Integer, ForeignKey("comment.id"))
    saved = relationship("saved")
    saved_id = Column(Integer, ForeignKey("saved.id"))
    caption = Column(String(90), nullable = True)
    media = Column(String(90), nullable = False)

class Like(Base):
    __tablename__ = "like"
    id = Column(Integer, primary_key = True)

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key = True)

    message = Column(String(100))

class Saved(Base):
    __tablename__ = "saved"
    id = Column(Integer, primary_key = True)




## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e