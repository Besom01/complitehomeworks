from datetime import date
from flask import Flask
import config as config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column('id',db.Integer, primary_key = True, autoincrement = True)
    title = db.Column('name', db.String(30), nullable = False)
    content = db.Column('content', db.String(500), nullable = False)
    date_create = db.Column('date_create', db.Date, default = date.today, nullable = False)
    #is_visible = db.Column('is_visible', db.Boolean, default = True, nullable = False)
    def __str__(self):
        return('<Post id - {}'.format(self.data))
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.name,
            'content': self.content,
            'date_create': self.date_create
            #'is_visible': self.is_visible
            }

class Comment(db.Model):
    id = db.Column('id', db.Integer, primary_key = True, autoincrement = True)
    id_post = db.Column('id_post', db.Integer, db.ForeignKey('post.id'), nullable = False, index = True)
    comment_content = db.Column('comment_content', db.String(140), nullable = False)
    comment_date_create = db.Column('comment_date_create', db.Date, default = date.today, nullable = False)
    post = db.relationship(Post, foreign_keys = [id_post])
    def __str__(self):
        return('Comment id: {}, for post id: {}'.format(self.id, self.id_post))
    def to_dict(self):
        return {
        'id':self.id,
        'id_post':self.id_post,
        'comment_content':self.comment_content,
        'comment_date_create':self.comment_date_create
        }