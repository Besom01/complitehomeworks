from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import config as config
from datetime import date
from flask_wtf import FlaskForm
from wtforms_alchemy import ModelForm

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


class GuessBookItem(db.Model):
    id = db.Column('id',db.Integer, primary_key = True, autoincrement = True)
    name = db.Column('name', db.String(30), default = 'Anon')
    content = db.Column('content', db.String(500), nullable = False)
    date_create = db.Column('date_create', db.Date, default = date.today, nullable = False)
    is_visible = db.Column('is_visible', db.Boolean, default = True, nullable = False)
    def __str__(self):
        return('<Person id - {}'.format(self.id))
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'content': self.content,
            'is_visible': self.is_visible
        }

class GuessBookItemForm(ModelForm):
    class Meta:
        model = GuessBookItem

@app.route('/create', methods = ['POST'])
def post_create():
    if request.method == 'POST':
        form = GuessBookItemForm(request.args)
        print('i am you request form: ' + str(request.args))
        if form.validate():
            post = GuessBookItem(**request.args)
            db.session.add(post)
            db.session.commit()
            return 'Post created!'
        else:
            print('Form is not valid! Post was not created.')
            return jsonify(form.errors)
    # form.data['name']
    # form.data['content']
            

@app.route('/')
def index():
    posts = GuessBookItem.query.all()
    return jsonify([p.to_dict() for p in posts])


if __name__ == '__main__':
    db.create_all()
    GuessBookItem.query.delete()
    post1 = GuessBookItem(name='ALexxx', content = 'some contentsss')
    db.session.add(post1)
    db.session.commit()
    app.run()
