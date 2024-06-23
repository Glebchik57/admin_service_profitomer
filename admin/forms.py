from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email


class AdminAutorizationForm(FlaskForm):
    '''Форма авторизации'''

    email = StringField("Email: ", validators=[Email()])
    password = PasswordField('Password: ')


class AdminRegistrationForm(FlaskForm):
    '''Форма регистрации'''

    email = StringField("Email: ", validators=[Email()])
    name = StringField("Name: ")
    surname = StringField("Surname: ")
    password = PasswordField('Password: ')
