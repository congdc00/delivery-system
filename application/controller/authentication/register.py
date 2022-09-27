
import email
from nis import cat
from loguru import logger
from application.models.user import User
from flask import redirect, url_for, render_template, flash
def register_post(request, db):

    
    username = request.form["username"]
    email_address = request.form['emailAddress']
    password = request.form['password']

    list_user = User.query.filter_by(email = email_address).first()
    if list_user:
        logger.warning("Da ton tai user")
    else:
        if username and email_address and password:
            new_user = User(username = username, email=email_address, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash(message = "Bạn đã đăng ký tài khoản thành công!", category = "info")
            logger.info("Add new user")

    return "authentication/register.html"

def register_get():
    return render_template("authentication/register.html")