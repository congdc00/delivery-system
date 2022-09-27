
from distutils.log import info
import email
from flask import render_template, redirect, url_for
from application.models.user import User
def info_post(request, session):
    
    return render_template("info.html")

def info_get(db, session):
    try:
        session_key = session['session_key']
        admin = session['admin']
    except:
        return redirect(url_for("index"))

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