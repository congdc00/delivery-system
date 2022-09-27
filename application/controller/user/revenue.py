from http.client import MOVED_PERMANENTLY
from flask import render_template, redirect, url_for
from application.models import enterprise
from application.models.user import User
from application.models.enterprise import Enterprise
from application.models.e2u import E2U
from application.models.enterprise import Enterprise
from application.helper.check_session import get_type_session
from application.models.user import User
from loguru import logger

def revenue_get(session):
    type = get_type_session(session)

    if type == 3 or type == 0:
        return redirect(url_for("index"))
    
    #User
    session_key = session['session_key']
    admin = session['admin']
    
    if type == 1: 
        
        user = User.query.filter_by(email = session_key).first()
        money = user.money
        return render_template("user/revenue.html", money = money, admin = admin, session_key = session_key)
    
    #enterprise
    else: 
        id = session['enterprise']
        enterprise = Enterprise.query.filter_by(id = id).first()
        money = enterprise.money
        return render_template("user/revenue.html", money = money, admin = admin, session_key = session_key, enterprise = enterprise)

def revenue_post(session, request):
    pass