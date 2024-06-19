import os

from flask import Flask
from dotenv import load_dotenv

from admin.admin import create_admin

load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

create_admin(app)


if __name__ == '__main__':
    app.run(debug=True)
