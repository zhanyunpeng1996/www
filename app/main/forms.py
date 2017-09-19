from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required


class NameForm(FlaskForm):
    username = StringField()
    sex = StringField()
    telnumber = StringField()
    major = StringField()
    mail = StringField()
    about = TextAreaField()
    submit = SubmitField()
