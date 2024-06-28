from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask import session as flask_session, redirect, url_for
from flask_login import current_user
from . import app


from db_config import session
from models import (
    Users,
    Sessions,
    Wb_Orders,
    Wb_Stosks,
    Wb_Supplies,
    Wb_Report_Detail,
    Wb_Sales,
    Delivery,

)


class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html')

    def is_accessible(self):
        return current_user.is_authenticated and current_user.email in app.config['ADMINS']

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('autorization'))


def create_admin(app):
    admin = Admin(
        app,
        index_view=MyAdminIndexView(),
        name='profit_admin',
        template_mode='bootstrap4'
    )
    admin.add_view(ModelView(Users, session))
    admin.add_view(ModelView(Sessions, session))
    admin.add_view(ModelView(Wb_Orders, session, category="Бизнес"))
    admin.add_view(ModelView(Wb_Sales, session, category="Бизнес"))
    admin.add_view(ModelView(Wb_Report_Detail, session, category="Бизнес"))
    admin.add_view(ModelView(Wb_Stosks, session, category="Бизнес"))
    admin.add_view(ModelView(Wb_Supplies, session, category="Бизнес"))
    admin.add_view(ModelView(Delivery, session, category="Бизнес"))
    return admin
