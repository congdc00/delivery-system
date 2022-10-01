from flask import render_template, redirect, url_for
from application.models.user import User
from application.models.notification import Notification
from application.models.e2u import E2U
from application.models.enterprise import Enterprise
from flask_login import current_user
from loguru import logger

def scheduler_map_get(session):
    if current_user.is_authenticated:
        if session['type'] == 0:

            return render_template("admin/scheduler_map.html")
        else:
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))
    

def scheduler_map_post(db, session, request):
    pass