from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

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


def create_admin(app):
    admin = Admin(app)
    admin.add_view(ModelView(Users, session))
    admin.add_view(ModelView(Sessions, session))
    admin.add_view(ModelView(Wb_Orders, session))
    admin.add_view(ModelView(Wb_Sales, session))
    admin.add_view(ModelView(Wb_Report_Detail, session))
    admin.add_view(ModelView(Wb_Stosks, session))
    admin.add_view(ModelView(Wb_Supplies, session))
    admin.add_view(ModelView(Delivery, session))
    return admin
