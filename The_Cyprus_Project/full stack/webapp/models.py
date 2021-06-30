import sqlalchemy
from datetime import timedelta, datetime
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func



class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    articles = db.Column(db.String())
    articletitle = db.Column(db.String())
    author = db.Column(db.String(100))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    time = db.Column(db.DateTime)
    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(150))
    password = db.Column(db.String(150))
    
