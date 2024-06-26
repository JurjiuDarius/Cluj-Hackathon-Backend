from flask_login import current_user
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask import redirect


class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect("/administrator/login")


class SecureIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect("/administrator/login")
