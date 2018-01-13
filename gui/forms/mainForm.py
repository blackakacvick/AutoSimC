from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import Required, Email


class SimPermutForm(FlaskForm):
    simPermutText = TextAreaField(u'Please input your SimPermut text', default="SIMPERMUT TEXT PLEASE")

    submit = SubmitField(u'Simm it!')