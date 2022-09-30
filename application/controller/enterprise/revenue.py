
from flask import render_template, redirect, url_for
from application.models.enterprise import Enterprise
from flask_login import current_user
from loguru import logger


def revenue_get(session):
    if current_user.is_authenticated and session['type'] == 2:
        id_enterprise = session['id_enterprise']
        enterprise = Enterprise.query.filter_by(id = id_enterprise).first()
        return render_template("enterprise/revenue.html", enterprise = enterprise)
    else:
        return redirect(url_for("index"))

def revenue_post(session, request):
    pass