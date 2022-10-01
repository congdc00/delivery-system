from flask import render_template, redirect, url_for
from application.models.device import Device
from flask_login import current_user

def get_dashboard_manager(session):
    if current_user.is_authenticated:
        if session['type'] == 1:
            id_user = current_user.get_id()
            list_device = Device.query.filter_by(id_root = id_user , is_user = True)
            return render_template("user/my_device/manage_device.html", list_device = list_device)
        else:
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))

def update_list_device():
    pass