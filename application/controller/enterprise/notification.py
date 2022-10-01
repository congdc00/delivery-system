from flask import render_template, redirect, url_for
from application.models.user import User
from application.models.notification import Notification
from flask_login import current_user
from loguru import logger

def notification_get(session):
    if current_user.is_authenticated:
        if session['type'] == 2:
            id_enterprise = current_user.get_id()
            list_notification = Notification.query.filter_by(id_receiver = id_enterprise, is_user = False)
            
            return render_template("enterprise/notification.html", list_notification = list_notification)
        else:
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))

def notification_post(session, request):
    pass