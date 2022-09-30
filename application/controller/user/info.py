
from distutils.log import info
import email
from flask import render_template, redirect, url_for
from application.models.enterprise import Enterprise
from application.models.user import User
from application.helper.check_session import get_type_session
from flask_login import current_user

def info_get(session):
    type = session['type']
    if current_user.is_authenticated:
        #admin
        if type == 0:
            return redirect(url_for("index"))
        
        #user
        elif type == 1:
            id_user = current_user.get_id()
            user = User.query.filter_by(id = id_user).first()
            return render_template("user/info.html", user = user)

        #enterprise
        else:
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))
        
   
def info_post():
    pass