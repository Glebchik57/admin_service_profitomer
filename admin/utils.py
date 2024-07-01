from functools import wraps

from flask import request, redirect, url_for, flash
from flask_login import current_user, login_required

from admin import app


def chek_admin(func):
    @login_required
    @wraps(func)
    def wrap(*args, **kwargs):
        if current_user.email in app.config['ADMINS']:
            return func(*args, **kwargs)
        else:
            flash('Вы не являетесь администраторо. Доступ запрещен')
            return redirect(request.referrer or url_for('index'))
    return wrap
