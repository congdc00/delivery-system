
from flask import render_template, redirect, url_for
from application.models.enterprise import Enterprise
from application.models.user import User
from flask_login import current_user
from loguru import logger


def revenue_get(session):
    if current_user.is_authenticated and session['type'] == 1:
        id_user = current_user.get_id()
        user = User.query.filter_by(id = id_user).first()
        return render_template("user/manage/revenue.html", user = user)
    else:
        return redirect(url_for("index"))

def revenue_post(session, request):
    pass