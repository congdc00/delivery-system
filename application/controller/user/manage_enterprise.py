from flask import render_template, redirect, url_for
from application.models.user import User
from application.models.e2u import E2U
from application.models.enterprise import Enterprise
from flask_login import current_user
from loguru import logger

def list_enterprise():
    if current_user.is_authenticated:
        id_user = current_user.get_id()
        list_enterprise = E2U.query.filter_by(id_user = id_user)
        
        list_e = []
        for enterprise_tmp in list_enterprise:
            id_enterprise = enterprise_tmp.id
            enterprise = Enterprise.query.filter_by(id = id_enterprise).first()
            list_e.append(enterprise)
        
        return render_template("user/manage/my_enterprise.html", list_e = list_e)
    else:
        return redirect(url_for("index"))

    

def login_enterprise(session, request):
    id_enterprise = request.form['id_enterprise']
    session['id_enterprise'] = id_enterprise
    session['type'] = 2
    return redirect(url_for("index"))

