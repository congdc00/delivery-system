from flask import render_template, redirect, url_for
from application.models.user import User
from application.models.notification import Notification
from application.models.e2u import E2U
from application.models.enterprise import Enterprise
from application.helper.check.check_login import get_type_session
from loguru import logger

def notification_get(session):
    type = get_type_session(session)

    if type == 3:
        return redirect(url_for("index"))
    
    #User
    session_key = session['session_key']
    admin = session['admin']
    
    if type == 1 or type == 0: 
        
        user = User.query.filter_by(email = session_key).first()
        id_user = user.id
        list_notification = Notification.query.filter_by(id_receiver = id_user)
        
        return render_template("notification.html", admin = admin, session_key = session_key, list_notification = list_notification)
    
    #enterprise
    else: 
        id = session['enterprise']
        enterprise = Enterprise.query.filter_by(id = id).first()
        return render_template("notification.html", admin = admin, session_key = session_key, enterprise = enterprise)

def notification_post(session, request):
    pass