import os

from flask import (
    redirect,
    render_template,
    request,
    url_for,
    flash,
    session as flask_session
)
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
from flask_login import (
    current_user,
    login_user,
    login_required,
    logout_user
)
from dotenv import load_dotenv

from admin import app
from models import Admins
from .forms import (
    AdminAutorizationForm,
    AdminRegistrationForm
)
from db_config import session

load_dotenv()

SPCL_KEY = os.getenv('SPCL_KEY')


@app.route("/admin_registration", methods=['GET', 'POST'])
def admin_registration():
    '''Представление регистрации.
    Включает в себя проверку аворизации пользователя, валидации формы,
    наличия в бд пользователей с аналогичными полями(email, tg, phone).
    После успешной проверки отправляет на почту ссылку для активации.'''

    form = AdminRegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data
            name = form.name.data
            surname = form.surname.data
            password = form.password.data
            special_key = form.special_key.data
            if special_key != SPCL_KEY:
                flash('Неверно введен специальный код', 'error')
                return render_template(
                        'admin_registration.html',
                        form=form
                    )
            else:
                try:
                    new_user = Admins(
                        email=email,
                        name=name,
                        surname=surname,
                        password=generate_password_hash(password),
                    )
                    session.add(new_user)
                    session.commit()
                    return redirect(url_for('admin.index'))
                except Exception as error:
                    session.rollback()
                    flash(f'Ошибка базы данных. Попробуйте позже. {error}', 'error')
                    return render_template(
                        'admin_registration.html',
                        form=form
                    )
        else:
            flash('форма заполнена е верно')
            return render_template(
                        'admin_registration.html',
                        form=form
                    )
    else:
        return render_template('admin_registration.html', form=form)


@app.route("/admin_autorization", methods=['GET', 'POST'])
def admin_autorization():
    '''Представление авторизации.
    Включает проверку авторизации пользователя, валидации формы,
    активации пользователя, соответствия пароля,
    фиксация времени подключения пользователя к сессии'''

    form = AdminAutorizationForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = session.query(Admins).filter_by(email=email).first()
        if not user:
            flash('Неверный email.', 'warning')
            return redirect(url_for('admin_autorization'))
        else:
            try:
                if check_password_hash(user.password, password):
                    login_user(user, remember=True)
                    flask_session['is_admin'] = True
                    return redirect(url_for('admin.index'))
                else:
                    flash('Неверный пароль.', 'warning')
                    return redirect(url_for('admin_autorization'))
            except Exception as error:
                flash(f'проблемы здесь {error}', 'warning')
                return redirect(url_for('admin_autorization'))
    else:
        return render_template('admin_autorization.html', form=form)


@app.route("/admin_logout", methods=['GET', 'POST'])
def admin_logout():
    logout_user()
    flask_session.pop('is_admin', None)
    return redirect(url_for('admin_autorization'))
