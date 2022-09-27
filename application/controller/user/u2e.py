from flask import render_template, redirect, url_for
from application.models.user import User
from application.models.e2u import E2U
from application.models.enterprise import Enterprise
from loguru import logger

def u2e_get(session):
    try:
        session_key = session["session_key"]
        admin = session['admin']
        
    except:
        return redirect(url_for("index"))

    user = User.query.filter_by(email = session_key).first()
    id_user = user.id
    list_enterprise = E2U.query.filter_by(id_user = id_user)
    
    list_e = []
    for enterprise_tmp in list_enterprise:
        id_enterprise = enterprise_tmp.id
        enterprise = Enterprise.query.filter_by(id = id_enterprise).first()
        list_e.append(enterprise)
    
    return render_template("user/u2e.html", session_key = session_key, admin = admin, list_e = list_e)

def u2e_post(session, request):
    enterprise = request.form['enterprise']
    session['enterprise'] = enterprise
    logger.info(f"Chuyển đổi sang chế độ doanh nghiệp có id = {enterprise}")
    return redirect(url_for("index"))

