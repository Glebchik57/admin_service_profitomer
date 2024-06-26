import re

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import Email
from wtforms.validators import ValidationError


class AdminAutorizationForm(FlaskForm):
    '''Форма авторизации'''

    email = StringField("Email: ", validators=[Email()])
    password = PasswordField('Password: ')


class AdminRegistrationForm(FlaskForm):
    '''Форма регистрации'''

    email = StringField("Email: ", validators=[Email()])
    phone = StringField('Phone Number: ')
    tg = StringField('Telegram: ')
    name = StringField("Name: ")
    surname = StringField("Surname: ")
    password = PasswordField('Password: ')

    def validate_phone_number(form, field):
        '''Валидация номера телефона'''

        if not re.match(r'^\+7\d{10}$', field.data):
            raise ValidationError(
                'Номер должен начинаться с "+7", и содержать 10 цифр после'
            )

    def validate_tg(form, field):
        '''Валидация никак в телеграм'''

        if not field.data.startswith('@'):
            raise ValidationError('Никнейм должен начинаться с символа @.')
        clear_nickname = field.data[1:]
        if not re.match(r'^[a-zA-Z][a-zA-Z0-9_]+$', clear_nickname):
            raise ValidationError('Никнейм должен состоять из латинских букв')
