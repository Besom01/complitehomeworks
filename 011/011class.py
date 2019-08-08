from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, validators, DateField, IntegerField
import random
import os

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)


class Randomazer(object):
    # #__instance = None
    x = None
    # # def __new__(cls):
    # #     if Randomazer.__instance is None:
    # #         Randomazer.__instance = object.__new__(cls)
    @classmethod
    def frand(cls):
        cls.x = random.randint(1,10)
        print('zagadanoe chislo',cls.x)

class ContactForm(FlaskForm):
    intquest = IntegerField(label='intquest')


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_form = ContactForm(request.form)
        if user_form.validate():
            if user_form.data['intquest'] == Randomazer.x:
                Randomazer.frand()
                z = '= Novoe chislo zagadano'
                return z
            elif user_form.data['intquest'] > Randomazer.x:
                z = '<'
                return z
            elif user_form.data['intquest'] < Randomazer.x:
                z = '>'
                return z
    if request.method == 'GET':
        Randomazer.frand()
        return 'Chislo zagadano', 200


if __name__ == '__main__':
    seed_number = int(os.environ['FLASK_RANDOM_SEED'])
    print(seed_number, '-seed_number')
    random.seed(seed_number)
    app.run()