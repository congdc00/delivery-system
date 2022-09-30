
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
            return redirect(url_for("index"))

        #enterprise
        else:
            id_enterprise = session['id_enterprise']
            enterprise = Enterprise.query.filter_by(id = id_enterprise).first()
            return render_template("enterprise/info.html", enterprise =enterprise)
    else:
        return redirect(url_for("index"))
        
   
def info_post():
    pass