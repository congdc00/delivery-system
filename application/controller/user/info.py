
from distutils.log import info
import email
from flask import render_template, redirect, url_for
from application.models.enterprise import Enterprise
from application.models.user import User
from application.helper.check_session import get_type_session
def info_post(request, session):
    
    return render_template("info.html")

def info_get(db, session):
    type = get_type_session(session)
    if type == 3 or type == 0: return redirect(url_for("index"))

    session_key = session['session_key']
    admin = session['admin']
    if type == 2:
        id_enterprise = session['enterprise']
        enterprise = Enterprise.query.filter_by(id = id_enterprise).first()
        return render_template("user/info.html",session_key = session_key, admin= admin, enterprise =enterprise)
    else:
        info_user = User.query.filter_by(email = session_key).first()

        
        email = info_user.email
        phone_number = info_user.phone_number
        password = info_user.password

        username = info_user.username
        id_card = info_user.id_card
        dob= info_user.dob
        sex= info_user.sex
        nationality= info_user.nationality
        place_of_origin= info_user.place_of_origin
        place_of_recidence= info_user.place_of_recidence
        date_of_expiry= info_user.date_of_expiry
        tax_id_number= info_user.tax_id_number

        return render_template("user/info.html",session_key = session_key, admin= admin,  username = username, email = email, password=password, name = username, id_card = id_card, dob = dob, sex = sex, nationality = nationality, place_of_origin = place_of_origin, place_of_recidence = place_of_recidence, date_of_expiry = date_of_expiry, tax_id_number = tax_id_number)