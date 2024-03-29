from flask import Flask, request
from threading import Lock
# pip install flask-WTF
from flask_wtf import FlaskForm
from wtforms import StringField, validators, DateField
import datetime
now = datetime.datetime.now()

class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[
        validators.Length(min=4, max=25)
    ])
    email = StringField(label='E-mail', validators=[
        validators.Length(min=6, max=35),
        validators.Email()
    ])
    job = StringField(label='JOB', validators=[
        validators.Required(),
        validators.AnyOf('IT','Bank','HR')
    ])
    birthdate = DateField(label = 'BirthDate', format='%Y-%m-%d')


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form)
        form = ContactForm(request.form)
        print(form.validate())

        if form.validate() and str(form.birthdate).split('-')[1] == str(now.month):
            return ('valid', 200)
        else:
            return ('invalid', 400)

    if request.method == 'GET':
        return 'hello world!', 200


if __name__ == '__main__':
    app.run()
