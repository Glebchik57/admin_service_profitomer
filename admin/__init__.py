import os

from flask import Flask
from dotenv import load_dotenv
from flask_login import LoginManager

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

templates = os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates'))

app = Flask(__name__, template_folder=templates)

ADMINS = ['g.sevostyanov@inbox.ru']


def filter_valid_latin1_characters(key):
    return ''.join(char for char in key if char.isascii() and char.isprintable())


S_KEY = filter_valid_latin1_characters(SECRET_KEY)

if not SECRET_KEY:
    raise ValueError("SECRET_KEY contains no valid latin-1 characters")
app.config['SECRET_KEY'] = S_KEY
app.config['ADMINS'] = ADMINS

login_manager = LoginManager(app)

from autorization import views
