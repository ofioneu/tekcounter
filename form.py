


#flask-contact/ContactForm.py
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import DateField,TimeField
csrf = CSRFProtect()

class MyForm(FlaskForm):
    data_inicio = DateField('data_inicio', validators=[DataRequired('data inicio não pode ficar vazio')], format='%Y-%m-%d')
    data_fim = DateField('data_fim', validators=[DataRequired('data fim não pode ficar vazio')], format='%Y-%m-%d')
    hora_inicio = TimeField('Hora Inicial', format='%H:%M')
    hora_final = TimeField('Hora Final', format='%H:%M')
    submit=SubmitField('Enviar')
